from flask import Flask, render_template
import requests

url = "https://genshin.jmp.blue/characters/characters?lang=en"

response = requests.get(url) 

if response.status_code == 200:
    data = response.json()
    print("Character Info:")
    print(data)

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://genshin.jmp.blue/characters/characters?limit=100")
    data = response.json()
    character_list = data['results']
    
    characters = []
    
    for character in character_list:
        url = character['url']
        parts = url.strip("/").split("/")
        id = parts[-1]
        
        image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png"
        
        characters.append({
            'name': character['name'].capitalize(),
            'id': id,
            'image': image_url
        })
    
    return render_template("index.html", characters=characters)

@app.route("/character/<int:id>")
def character_detail(id):
    # We get detailed info for a specific Pokémon using its id.
    response = requests.get(f"https://genshin.jmp.blue/characters/characters?lang=en{id}")
    data = response.json()
    
    types = [t['type']['name'] for t in data['types']]
    height = data.get('height')
    weight = data.get('weight')
    name = data.get('name').capitalize()
    image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png"
    
    # Get the Pokémon’s base stats (like hp, attack, defense, etc.)
    stat_names = [stat['stat']['name'] for stat in data['stats']]
    stat_values = [stat['base_stat'] for stat in data['stats']]
    
    # We tell Flask to show the 'pokemon.html' page with all these details.
    return render_template("character.html", character={
        'name': name,
        'id': id,
        'image': image_url,
        'types': types,
        'height': height,
        'weight': weight,
        'stat_names': stat_names,
        'stat_values': stat_values
    })

if __name__ == '__main__':
    app.run(debug=True)