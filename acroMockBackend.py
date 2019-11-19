from flask import Flask
from flask import jsonify

import random
import string


app = Flask(__name__)

@app.route("/acronym", methods=['GET'])
def getAcronym():
    return f"{randomString(4)}"




@app.route("/leaderboard", methods=['GET'])
def getLeaderboard():


    leaders = ["Jerry", "Nancy", "Samantha", "Cornpop",
    "Terrence", "Lawrence", "Gary", "Martin", "Aerodonis"]
    return jsonify(leaders)


@app.route('/')
def index():
    return "<h1>Mock Server</h1>"


def randomString(stringLength=4):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))



if __name__ == "__main__":
    app.run()