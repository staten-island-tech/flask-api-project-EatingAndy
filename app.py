from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://completecriminalchecks.com/Developers/limit=100")
    print(response.text)
    data = response.json()
    criminal_list = data['results']
    criminals = []

    for criminal in criminal_list:
        url = criminal['url']
        parts = url.strip("/").split("/")
        id = parts[-1]
        image_url = image_url = f"https://completecriminalchecks.com/Developers/{id}.png"
        criminals.append({
            'name' : criminal['name'].capitalize(),
            'id' : id,
            'image' : image_url
        })
    return render_template("index.html", criminals = criminals)

@app.route("/criminal/<id>")
def criminal_detail(id):
    response = requests.get(f"https://completecriminalchecks.com/Developers/{id}")
    data = response.json()
    height = data.get('height')
    weight = data.get('weight')
    name = data.get('name').capitalize()
    image_url = f"https://completecriminalchecks.com/Developers/{id}.png"

    return render_template("criminals.html", criminal={
        'name': name,
        'id': id,
        'image': image_url,
        'height': height,
        'weight': weight
    })
if __name__ == '__main__':
    app.run(debug=True)