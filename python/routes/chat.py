import openai
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json
import os

openai.api_key = os.environ.get('API_KEY')

messages = [{'role': 'system', 'content': 'you are an ai assistant'}]

class Chat(Resource):
    def get(self):
        headers = request.headers
        
        prompt = headers.get('prompt')
        messages.append({'role': 'user', 'content': prompt})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=1,
            max_tokens=100,
        )

        response_message = response.choices[0]['message']
        messages.append({ 'role': response_message['role'], 'content': response_message['content'] })

        return response_message