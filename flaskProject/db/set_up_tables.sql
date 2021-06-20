-- Script to set up the database for music recommendation
-- Should include creations of the following tables
-- Music, User, Record(?

\c music_recommender;

CREATE TABLE IF NOT EXISTS genres (
                                      genre_id integer PRIMARY KEY,
                                      title VARCHAR);

CREATE TABLE IF NOT EXISTS albums (
                                      album_id integer PRIMARY KEY,
                                      date_created TIMESTAMP,
                                      listens integer,
                                      favorites integer,
                                      type VARCHAR,
                                      tracks_included integer[]);


CREATE TABLE IF NOT EXISTS artists (
                                       artist_id integer PRIMARY KEY,
                                       favorites integer,
                                       name VARCHAR);

CREATE TABLE IF NOT EXISTS tracks (
                                      track_id integer PRIMARY KEY,
                                      genre_id varchar,
                                      album_id integer REFERENCES albums (album_id),
                                      artist_id integer REFERENCES artists (artist_id),
                                      date_created TIMESTAMP,
                                      favorites integer,
                                      interest integer,
                                      listens integer,
                                      title VARCHAR);

CREATE TABLE IF NOT EXISTS users (
                                     user_id integer PRIMARY KEY,
                                     user_name VARCHAR,
                                     date_created TIMESTAMP,
                                     email VARCHAR,
                                     age integer,
                                     gender boolean,
                                     nationality VARCHAR,
                                     member_status VARCHAR);

CREATE TABLE IF NOT EXISTS log (
                                   log_id integer PRIMARY KEY,
                                   time TIMESTAMP,
--      user_id integer REFERENCES users (user_id),
                                   track_id integer REFERENCES tracks (track_id),
                                   source_tracks integer[],
                                   result boolean);

CREATE TABLE IF NOT EXISTS similarity (
                                          track_a integer REFERENCES tracks (track_id),
                                          track_b integer REFERENCES tracks (track_id),
                                          score float,
                                          PRIMARY KEY (track_a, track_b));

COPY genres (genre_id, title)
    FROM '/Users/mchuang/PycharmProjects/react-flask-app/flaskProject/data/genres_compressed.csv'
    DELIMITER ','
    CSV HEADER;

COPY albums (album_id, date_created, listens, favorites, type, tracks_included)
    FROM '/Users/mchuang/PycharmProjects/react-flask-app/flaskProject/data/albums_compressed.csv'
    DELIMITER ','
    CSV HEADER;

COPY artists (artist_id, favorites, name)
    FROM '/Users/mchuang/PycharmProjects/react-flask-app/flaskProject/data/artist_compressed.csv'
    DELIMITER ','
    CSV HEADER;

COPY tracks (track_id, genre_id, album_id, artist_id, date_created, favorites, interest, listens, title)
    FROM '/Users/mchuang/PycharmProjects/react-flask-app/flaskProject/data/tracks_compressed.csv'
    DELIMITER ','
    CSV HEADER;

COPY similarity (track_a, track_b, score)
    FROM '/Users/mchuang/PycharmProjects/react-flask-app/flaskProject/data/similarity.csv'
    DELIMITER ','
    CSV HEADER;