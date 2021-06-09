import numpy as np
from sklearn.metrics import pairwise as pw
import pandas as pd
from setup_similarity import extract_genre_list


# def genre_id_to_index(genre_table, target_id):
#     for i in range(len(genre_table)):
#         if genre_table[i][1] == target_id:
#             return i
#     return -1
#
#
# def setup_genre_list(genre_table, selected_genre):
#     out = np.zeros(len(genre_table))
#     for g in selected_genre:
#         index = genre_id_to_index(genre_table, g)
#         if index >= 0:
#             out[index] = 1
#     return out


def genre_result(track_data, genre_list):
    track_genre = [extract_genre_list(track_data[i].genres_all) for i in range(len(track_data))]
    sim_list = []
    for i in track_genre:
        sim_list.append(len(list(set(track_data) & set(genre_list))))
    max_index = sorted(range(len(sim_list)), key=lambda j: sim_list[j])[-3:]
    return [track_data[i].track_id for i in max_index]


def music_result():
    return [2]


def get_music_path(music_id):
    path = []
    for m in music_id:
        base = '/fma_small/'
        folder_name = (str(m) + "000")[:3]
        end = '/' + str(m) + '.mp3'
        path.append(base+folder_name+end)
    return path
