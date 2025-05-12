from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://api.disneyapi.dev/character")
    
    if response.status_code != 200:
        return "Failed to fetch data from Disney API"
    
    data = response.json()
    character_list = data.get("data", [])

    characters = []

    for character in character_list:
        characters.append({
            'name': character.get('name', 'Unknown'),
            'id': character.get('_id'),
            'image': character.get('imageUrl', '')
        })
    
    return render_template("index.html", characters=characters)

@app.route("/character/<id>")
def character_detail(id):
    response = requests.get(f"https://api.disneyapi.dev/character/{id}")

    if response.status_code != 200:
        return f"Character with ID {id} not found."
    
    data = response.json()
    
    character = {
        'name': data.get('name', 'Unknown'),
        'id': data.get('_id'),
        'image': data.get('imageUrl', ''),
        'films': data.get('films', []),
        'tvShows': data.get('tvShows', []),
        'videoGames': data.get('videoGames', []),
        'parkAttractions': data.get('parkAttractions', []),
        'allies': data.get('allies', []),
        'enemies': data.get('enemies', [])
    }

    return render_template("character.html", character=character)

if __name__ == '__main__':
    app.run(debug=True)