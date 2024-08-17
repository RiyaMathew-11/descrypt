# app.py
import torch
import torch.nn as nn
from transformers import BertModel, BertTokenizer
from model import SiameseBERT
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd 

final_score = 0
i = 0
data = pd.read_csv('data/data_draft.csv')
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)

model = SiameseBERT(model_name)

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes



@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message']
    response = generate_response(message)
    return jsonify({'message': response})


def generate_response(message):
    
    global i
    global final_score
    
    if message.lower() == 'stop':
        return f"Your final score is {str(round(final_score,2))}"
    elif message.lower() == 'start':
        return data.Question[i]
    elif message.lower() == 'next':
        i += 1
        return data.Question[i]
    else:
        
        text1 = data.Model_Answer[i]
        text2 = message
        inputs1 = tokenizer(text1, return_tensors="pt", padding=True,
                            truncation=True, max_length=128)
        inputs2 = tokenizer(text2, return_tensors="pt", padding=True,
                            truncation=True, max_length=128)
        
        with torch.no_grad():
            similarity_score = model(
            input_ids1=inputs1["input_ids"],
            attention_mask1=inputs1["attention_mask"],
            input_ids2=inputs2["input_ids"],
            attention_mask2=inputs2["attention_mask"]
        )
            
        if similarity_score.item() >= 0.9:
            score = 2
            
        elif similarity_score.item() >= 0.7 or similarity_score.item() < 0.9:
            score = 2*round(similarity_score.item(),2)
            
        else: 
            score = 0
        
        final_score += score
        return f"Your score is {str(score)}"
        
    


if __name__ == '__main__':
    app.run(port=5600, debug=True)
