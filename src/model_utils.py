from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import os

model_path = "RUSpam/spam_deberta_v4"
tokenizer = None
model = None

def load_model():
    global tokenizer, model
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)

def download_model():
    if not os.path.exists(model_path):
        # Logic to download the model can be added here if necessary
        load_model()

def predict(text):
    if tokenizer is None or model is None:
        load_model()
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=256)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()
    return predicted_class == 1  # 1 - spam, 0 - not spam