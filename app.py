from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php")

    if response.status_code != 200:
        return "Failed to fetch data from API"

    cards = response.json().get("data", [])
    return render_template("index.html", cards=cards[:50])  # Limit to first 50 cards for performance

@app.route("/card/<int:card_id>")
def card_detail(card_id):
    response = requests.get(f"https://db.ygoprodeck.com/api/v7/cardinfo.php?id={card_id}")

    if response.status_code != 200:
        return f"Card with ID {card_id} not found."

    data = response.json().get("data", [])
    if not data:
        return f"Card with ID {card_id} not found."

    card = data[0]
    return render_template("card.html", card=card)

if __name__ == '__main__':
    app.run(debug=True)






