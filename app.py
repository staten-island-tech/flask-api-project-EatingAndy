from flask import Flask, render_template
import requests

# Example: Get information about the character Albedo
url = "https://genshin.jmp.blue/characters/Lisa?lang=en"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Character Info:")
    print(data)