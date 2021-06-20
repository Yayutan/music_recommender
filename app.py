from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import fetch_results
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)


class Genre(db.Model):
    __table__ = db.Model.metadata.tables['genre']


class Track(db.Model):
    __table__ = db.Model.metadata.tables['track']


class Album(db.Model):
    __table__ = db.Model.metadata.tables['album']


class Artist(db.Model):
    __table__ = db.Model.metadata.tables['artist']


class Similarity(db.Model):
    __table__ = db.Model.metadata.tables['similarity']


@app.route("/results", methods=["GET", "POST"])
def receive_update_results():
    if request.method == "POST":
        req = request.form
        if req['submit_btn'] == 'genre_btn':
            genre_list = [int(req[k]) for k in req.keys() if k != 'submit_btn']
            track_data = Track.query.all()
            music_id = fetch_results.genre_result(track_data, genre_list)
        elif req['submit_btn'] == 'music_btn':
            music_id = fetch_results.music_result()
        else:
            return render_template('index.html')
        music_path = fetch_results.get_music_path(music_id)
        print(music_path)
    return render_template('result.html', music_path=music_path)


@app.route("/")
def main():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
