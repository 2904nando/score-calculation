from flask import Flask, request
from functions import insurance_handler

app = Flask(__name__)

@app.route('/calculate-scores', methods=['POST'])
def calculate_scores():
    try:
        userData = request.json
        return insurance_handler.calculate_scores(userData), 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)