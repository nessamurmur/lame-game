import json
from flask import Flask, request


app = Flask(__name__)

characters = []


@app.route("/characters", methods=["POST"])
def create_character():
    username = str(request.json.get('username'))
    character = {"username": username}
    characters.append(character)
    return json.dumps(character)


@app.route("/characters", methods=["GET"])
def characters_index():
    return json.dumps(characters)


@app.route("/characters/<username>", methods=["GET"])
def show_character(username):
    character = filter(lambda char: char["username"] == username, characters)[0]
    return json.dumps(character)


@app.route("/characters/<username>", methods=["DELETE"])
def delete_character(username):
    character = filter(lambda char: char["username"] == username, characters)[0]
    characters.remove(character)
    return json.dumps(character)

if __name__ == "__main__":
    app.run()
