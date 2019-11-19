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


    leaders = {}
    leaders["Gary"] = 5000
    leaders["Samantha"] = 4650
    leaders["Intrepid"] = 4200
    leaders["Sally"] = 3650
    leaders["Terrence"] = 3200
    leaders["Phil"] = 2800
    leaders["Treyvon"] = 2500
    leaders["Cornpop"] = 2000
    
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