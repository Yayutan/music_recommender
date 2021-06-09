import numpy as np
import pandas as pd
from sklearn.metrics import pairwise as pw
import psycopg2


def extract_tracks(tracks):
    # Set up subset of track dataset
    track_simplified = pd.DataFrame(
        {'track_comments': tracks[('track', 'comments')],
         'track_favorites': tracks[('track', 'favorites')],
         'track_genre': tracks[('track', 'genres_all')],
         'track_interest': tracks[('track', 'interest')],
         'track_listen': tracks[('track', 'listens')]})
    return track_simplified


def extract_echonest(echonest):
    # Set up subset of echonest dataset
    echonest_no_level = echonest.copy()
    no_level_columns = echonest_no_level.columns.droplevel(0).droplevel(0)
    echonest_no_level.columns = no_level_columns
    echonest_no_level = pd.DataFrame(echonest_no_level.iloc[:, :25])

    audio_columns = 'audio_' + no_level_columns[:8]
    metadata_columns = 'metadata_' + no_level_columns[8:15]
    ranks_columns = 'ranks_' + no_level_columns[15:20]
    social_columns = 'social_' + no_level_columns[20:25]
    echonest_no_level.columns = audio_columns.append(metadata_columns).append(ranks_columns).append(social_columns)
    echonest_simplified = pd.merge(echonest_no_level.iloc[:, :8], echonest_no_level.iloc[:, 20:], on='track_id')
    return echonest_simplified


def extract_genre_list(list_str):
    out = []
    elements = list_str[1:-1].split(',')
    for e in elements:
        out.append(int(e))
    return out


def add_genre_columns(data, genres):
    for g in genres['title']:
        code = genres[genres['title'] == g]['genre_id']
        genre_col = np.zeros(len(data))
        for i in range(len(data)):
            genre_list = extract_genre_list(data.iloc[i]['track_genre'])
            for element in genre_list:
                if int(element) == int(code):
                    genre_col[i] = 1
        data[g] = genre_col
    return data


def setup_data(tracks, genres, echonest):
    track_simplified = extract_tracks(tracks)
    echonest_simplified = extract_echonest(echonest)
    data = pd.merge(track_simplified, echonest_simplified, on='track_id')
    data.drop_duplicates()
    data = add_genre_columns(data, genres)
    data = data.drop(labels=['track_genre'], axis=1)
    return data


def similarity_df(data):
    sim_list = []
    cosine_similarities = pw.cosine_similarity(data, data)
    for i in range(len(cosine_similarities) - 1):
        for j in range(i+1, len(cosine_similarities)):
            sim_list.append((data.index[i], data.index[j], cosine_similarities[i][j]))
    sim_table = pd.DataFrame(sim_list, columns=["track1", "track2", "score"])
    return sim_table


def setup_sim_table(tracks, genres, echonest, conn):
    data = setup_data(tracks, genres, echonest)
    sim = similarity_df(data)
    sim.to_sql('similarity', con=conn, if_exists='replace', index=True, index_label="sim_id")
    conn.execute("ALTER TABLE similarity ADD PRIMARY KEY (sim_id);")
    conn.execute("""ALTER TABLE similarity 
    ADD CONSTRAINT constraint_t1 FOREIGN KEY (track1) 
    REFERENCES track(track_id)
    ON DELETE CASCADE;""")
    conn.execute("""ALTER TABLE similarity 
        ADD CONSTRAINT constraint_t2 FOREIGN KEY (track2) 
        REFERENCES track(track_id)
        ON DELETE CASCADE;""")

    conn.execute("SELECT * FROM similarity LIMIT 5;")


