from flask import Flask
from flask import jsonify

import random
import string


app = Flask(__name__)

@app.route("/acronym", methods=['GET'])
def getAcronym():
    return jsonify(f"{randomString(4)}")




@app.route("/leaderboard", methods=['GET'])
def getLeaderboard():


    leaders = [("Jerry", 5000), ("Nancy", 4650) ("Samantha", 4200), ("Cornpop", 3500)
    ("Terrence", 2985) ("Lawrence", 2600) ("Gary", 2200) ("Martin", 2000) ("Aerodonis", 500)]
    return jsonify(leaders)


@app.route('/')
def index():
    return "<h1>Mock Server</h1>"


def randomString(stringLength=4, methods=['GET']):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))



if __name__ == "__main__":
    app.run()