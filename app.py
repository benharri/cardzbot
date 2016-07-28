from flask import Flask, Response, request
import os
from requests import post, get

token = os.environ['TELEGRAM_API_TOKEN']
tg_url = 'https://api.telegram.org/bot{token}/'.format(token=token)
me_url = 'bot.benhh.com/'

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/{token}'.format(token=token))
def token_route():
    read_update(request.json)
    return Response(status=200)

def read_update(update):
    chat_id = update['message']['chat']['id']
    msg = {'chat_id': chat_id, 'text': str(update)}
    post(tg_url+'sendMessage', data=msg)

def set_webhook():
    url = me_url+token
    data = {'url':url}
    post(tg_url+'setWebhook', data=data)

if __name__ == "__main__":
    set_webhook()
    app.run()