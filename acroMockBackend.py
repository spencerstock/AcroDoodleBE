
from flask import jsonify, json, Flask

import random
import string


app = Flask(__name__)

@app.route("/acronym", methods=['GET'])
def getAcronym():
    return jsonify(f"{randomString(4)}")

def highscore(name, score):
    name = name
    score = score




@app.route("/leaderboard", methods=['GET'])
def getLeaderboard():



    scoreList = []

    tempScore = 5000
    for i in range(0,10):
        myDict = {
        'userName': randomString(8),
        'Score': tempScore}
        scoreList.append(myDict)
        tempScore -= 250

    # convert to json data
    jsonStr = json.dumps(scoreList)
    return jsonStr

    



@app.route('/')
def index():
    return "<h1>Mock Server</h1>"


def randomString(stringLength=4, methods=['GET']):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))



if __name__ == "__main__":
    app.run()