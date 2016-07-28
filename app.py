from flask import Flask, Response
import os
import requests

token = os.environ['TELEGRAM_API_TOKEN']
tg_url = 'https://api.telegram.org/bot{token}/'.format(token=token)
me_url = 'cardzbot.herokuapp.com/'

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/{token}'.format(token=token))
def token_route():
    return Response(status=200)

if __name__ == "__main__":

    app.run()