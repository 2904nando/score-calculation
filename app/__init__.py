from flask import Flask, request
from functions import insurance_handler

app = Flask(__name__)

@app.route('/calculate-score', methods=['POST'])
def calculate_score():
    userData = request.json
    return insurance_handler.calculate_scores(userData)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)