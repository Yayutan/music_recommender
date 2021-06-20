from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import json
from flask import jsonify

from flask_sqlalchemy import SQLAlchemy
import fetch_results
import config

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)


class Genre(db.Model):
    __table__ = db.Model.metadata.tables['genres']


class Track(db.Model):
    __table__ = db.Model.metadata.tables['tracks']


class Album(db.Model):
    __table__ = db.Model.metadata.tables['albums']


class Artist(db.Model):
    __table__ = db.Model.metadata.tables['artists']


class Similarity(db.Model):
    __table__ = db.Model.metadata.tables['similarity']


# class User(db.Model):
#     __table__ = db.Model.metadata.tables['users']
#
#
# class Log(db.Model):
#     __table__ = db.Model.metadata.tables['log']


@app.route("/results", methods=["POST"])
def receive_update_results():
    # if request.method == "POST":
    #     req = request.form
    #     if req['submit_btn'] == 'genre_btn':
    #         genre_list = [int(req[k]) for k in req.keys() if k != 'submit_btn']
    #         track_data = Track.query.all()
    #         music_id = fetch_results.genre_result(track_data, genre_list)
    #     elif req['submit_btn'] == 'music_btn':
    #         music_id = fetch_results.music_result()
    #     else:
    #         return render_template('index.html')
    #     music_path = fetch_results.get_music_path(music_id)
    #     print(music_path)
    return render_template('result.html', music_path=None)


def parse_input(data):
    return None


@app.route("/getresult", methods=["POST"])
def store_user_info():
    user_info = json.loads(request.data)
    # print(user_info)
    genre_list = user_info['genres']
    track_data = Track.query.all()
    music_path = fetch_results.genre_result(track_data, genre_list)
    print(music_path)
    return jsonify({'path0': music_path[0], 'path1': music_path[1],'path2': music_path[2]})


@app.route("/")
def main():
    return None;
    # return render_template('index.html')


if __name__ == "__main__":
    app.run()
