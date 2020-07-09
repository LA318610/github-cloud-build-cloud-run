import socket
import random
import os
import json
import requests

from flask import Flask
from flask import render_template

app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

SUPPORTED_COLORS = ",".join(color_codes.keys())

# Get color from Environment variable
PROJECT_NAME = os.environ.get('PROJECT', None) or 'vikcolor'
ENV_NAME = os.environ.get('ENV', None) or 'dev'
KEY_NAME = os.environ.get('KEY_NAME', None) or 'APP_COLOR'
API_URL = os.environ.get('API_URL', None) or 'https://config-service-zywui4kirq-uc.a.run.app'
URL = f'{API_URL}/project/{PROJECT_NAME}/env/{ENV_NAME}/key/{KEY_NAME}'


@app.route("/")
def main():
    response = requests.get(URL)
    color = json.loads(response.content.decode('utf-8'))['value']

    if color and color in SUPPORTED_COLORS:
        COLOR = color
    else:
        COLOR = random.choice(["red", "green", "blue", "blue2", "darkblue", "pink"])

    return render_template('welcome.html', name=socket.gethostname(), color=color_codes[COLOR])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
