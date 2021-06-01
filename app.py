from datetime import datetime
import json
import random
from chatterbot import ChatBot
from flask import Flask, request
from covid import Covid
from iso3166 import countries
app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

if __name__ == "__main__":
    app.run() 