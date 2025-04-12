from flask import Flask, request, jsonify
from model_utils import predict, download_model
import sys

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def classify_text():
    data = request.get_json()
    text = data.get('text', '')
    result = predict(text)
    return jsonify({'is_spam': result})


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "download-model":
        download_model()
    else:
        app.run(host='0.0.0.0', port=8080)
