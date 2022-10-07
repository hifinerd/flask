from flask import Flask, jsonify, request
import csv

all_movies = []
with open('movies.csv', "utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
like_movies = []
not_like_movies = []
did_not_watch = []

app = Flask(__name__)
@app.route("/get-movies")
def get_movies():
    return jsonify({
        "data": all_movies[0],
        "status": "success",
    })

@app.route("/like-movies", methods = ["POST"])
def like_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    like_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/not-like-movies", methods = ["POST"])
def not_like_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_like_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/did-not-watch", methods = ["POST"])
def did_not_watch():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    did_not_watch.append(movie)
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
    app.run()