from flask import Flask, send_from_directory, jsonify
import random, json

app = Flask(__name__)

import cows_bulls as game


# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('public', path)

# Create secret number API
@app.route("/getSN", methods=['GET'])
def return_secret_number():
    data = json.dumps(game.create_secret_number())
    return jsonify(data)

# @app.route("/rand")
# def hello():
#     return str(random.randint(0, 100))

if __name__ == "__main__":
    app.run(debug=True, port=5001)
