import openai
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

# import routes
from routes.chat import Chat
from routes.blip import Blip

app = Flask("ai_api")
api = Api(app)
CORS(app)

api.add_resource(Chat, '/chat')
api.add_resource(Blip, '/blip')

if __name__ == '__main__':
    app.run()