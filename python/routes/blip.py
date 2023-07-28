import os
from flask import Flask, request
from flask_restful import Resource, Api
from PIL import Image
from transformers import Blip2Processor, Blip2ForConditionalGeneration
import torch
import threading
from io import BytesIO

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b")
model = Blip2ForConditionalGeneration.from_pretrained(
    "Salesforce/blip2-opt-2.7b", torch_dtype=torch.float32
)
model.to(device)

lock = threading.Lock()

class Blip(Resource):
    def post(self):
        file = request.files.get('file')
        if file is None:
            return "No file uploaded", 400
        image = Image.open(BytesIO(file.read()))
        print("Finished loading image")

        prompt = request.form['prompt']
        if prompt == "":
            return 'you need to suply a prompt'
        formatedPrompt = f'Question: {request.form["prompt"]}? Answer:'
        print(prompt)
        
        # Acquire the lock
        lock.acquire()
        
        try:
            inputs = processor(images=image, text=formatedPrompt, return_tensors="pt").to(device, torch.float32)
            inputs = {k: v.to(device) for k, v in inputs.items()}  # Move inputs to GPU
            generated_ids = model.generate(**inputs)
            generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()

            print(generated_text)
            return generated_text
        finally:
            # Release the lock
            lock.release()

