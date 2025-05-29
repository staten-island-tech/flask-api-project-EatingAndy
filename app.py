from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    try:
        response = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php")
    except:
        print("Unable to recieve data")
    data = response.json()
    card_list = data.get("data", [])
    cards = []
    for card in card_list[:50]:
        cards.append({
            'id': card.get('id'),
            'name': card.get('name'),
            'image': card['card_images'][0]['image_url'] if 'card_images' in card and card['card_images'] else None,
            'type': card.get('type')
        })
    return render_template("index.html", cards=cards)

@app.route("/card/<int:card_id>")
def card_detail(card_id):
    response = requests.get(f"https://db.ygoprodeck.com/api/v7/cardinfo.php?id={card_id}")
    data = response.json().get("data", [])
    if not data:
        return f"Card ID {card_id} not found"
    card = data[0]
    name = card.get('name')
    type_ = card.get('type')
    desc = card.get('desc')
    image_url = card['card_images'][0]['image_url'] if 'card_images' in card and card['card_images'] else None
    atk = card.get('atk')
    def_ = card.get('def')
    level = card.get('level')
    race = card.get('race')
    attribute = card.get('attribute')
    return render_template("card.html", card={
        'id': card_id,
        'name': name,
        'type': type_,
        'desc': desc,
        'image': image_url,
        'atk': atk,
        'def': def_,
        'level': level,
        'race': race,
        'attribute': attribute
    })
if __name__ == '__main__':
    app.run(debug=True)
