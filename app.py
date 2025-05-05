from flask import Flask, render_template
import requests

app = Flask(__name__)

def index():
    response = requests.get("https://completecriminalchecks.com/Developers/limit=100")
    data = response.json()
    criminal_list = data['results']
    criminals = []

    for criminal in criminal_list:
        url = criminal['url']
        parts = url.strip("/").split("/")
        id = parts[-1]
        image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png"
        criminals.append({
            'name' : criminal['name'].capitalize(),
            'id' : id,
            'image' : image_url
        })
    return render_template("index.html", criminals = criminals)

def criminal_detail(id):
    response = requests.get(f"https://completecriminalchecks.com/Developers/{id}")
    data = response.json