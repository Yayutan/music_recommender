from sqlalchemy import create_engine
import pandas as pd
import config
import setup_similarity as sim
import psycopg2


def read_data():
    whole_track = pd.read_csv('data/tracks.csv', index_col=0, header=[0, 1])
    genre = pd.read_csv('data/genres.csv')
    echonest = pd.read_csv('data/echonest.csv', index_col=0, header=[0, 1, 2])
    small_track = whole_track[whole_track['set']['subset'] == 'small']
    return small_track, genre, echonest


def split_track_levels(whole_track):
    album = whole_track['album']
    artist = whole_track['artist']
    track = whole_track['track']
    track.reset_index(level=0, inplace=True)
    album.reset_index(level=0, inplace=True)
    artist.reset_index(level=0, inplace=True)
    return track, album, artist


def split_echonest_levels(echonest):
    audio_features = echonest['echonest']['audio_features']
    metadata = echonest['echonest']['metadata']
    ranks = echonest['echonest']['ranks']
    social_features = echonest['echonest']['social_features']
    temporal_features = echonest['echonest']['temporal_features']
    audio_features.reset_index(level=0, inplace=True)
    metadata.reset_index(level=0, inplace=True)
    ranks.reset_index(level=0, inplace=True)
    social_features.reset_index(level=0, inplace=True)
    temporal_features.reset_index(level=0, inplace=True)
    return audio_features, metadata, ranks, social_features, temporal_features


def create_data_tables(whole_track, genre, echonest, conn):
    track, album, artist = split_track_levels(whole_track)
    audio_features, metadata, ranks, social_features, temporal_features = split_echonest_levels(echonest)

    track.to_sql('track', con=conn, if_exists='replace', index=False)
    album.to_sql('album', con=conn, if_exists='replace', index=False)
    artist.to_sql('artist', con=conn, if_exists='replace', index=False)
    genre.to_sql('genre', con=conn, if_exists='replace', index=True, index_label="genre_index")
    audio_features.to_sql('audio_features', con=conn, if_exists='replace', index=False)
    metadata.to_sql('metadata', con=conn, if_exists='replace', index=False)
    ranks.to_sql('ranks', con=conn, if_exists='replace', index=False)
    social_features.to_sql('social_features', con=conn, if_exists='replace', index=False)
    temporal_features.to_sql('temporal_features', con=conn, if_exists='replace', index=False)

    conn.execute("ALTER TABLE track ADD PRIMARY KEY (track_id);")
    conn.execute("ALTER TABLE album ADD PRIMARY KEY (track_id);")
    conn.execute("ALTER TABLE artist ADD PRIMARY KEY (track_id);")
    conn.execute("ALTER TABLE genre ADD PRIMARY KEY (genre_id);")
    conn.execute("ALTER TABLE audio_features ADD PRIMARY KEY (track_id);")
    conn.execute("ALTER TABLE metadata ADD PRIMARY KEY (track_id);")
    conn.execute("ALTER TABLE ranks ADD PRIMARY KEY (track_id);")
    conn.execute("ALTER TABLE social_features ADD PRIMARY KEY (track_id);")
    conn.execute("ALTER TABLE temporal_features ADD PRIMARY KEY (track_id);")
    print("Successfully set up tables from FMA data")


def main():
    track, genre, echonest = read_data()
    engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
    with engine.connect() as conn:
        conn.execute("DROP SCHEMA public CASCADE;")
        conn.execute("CREATE SCHEMA public;")
        create_data_tables(track, genre, echonest, conn)
        sim.setup_sim_table(track, genre, echonest, conn)


if __name__ == "__main__":
    main()