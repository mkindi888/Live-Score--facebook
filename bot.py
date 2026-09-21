import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

PAGE_ID = os.getenv("PAGE_ID")
PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")


def post_to_facebook(message):
    url = f"https://graph.facebook.com/{PAGE_ID}/feed"

    data = {
        "message": message,
        "access_token": PAGE_ACCESS_TOKEN
    }

    response = requests.post(url, data=data)
    print(response.json())


@app.route("/goal", methods=["POST"])
def goal():
    data = request.json

    home = data.get("home_team", "Home")
    away = data.get("away_team", "Away")
    home_score = data.get("home_score", "?")
    away_score = data.get("away_score", "?")
    minute = data.get("minute", "?")
    player = data.get("player", "")

    message = (
        f"🚨⚽ GOOOOOOAL! ‼️\n\n"
        f"⏰ {minute}'\n"
        f"🔥 {home} {home_score}-{away_score} {away}\n"
    )

    if player:
        message += f"⚽ Mfungaji: {player}\n"

    message += "\n#LiveScore #Football"

    post_to_facebook(message)

    return jsonify({"status": "posted"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
