from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import random
import os

app = Flask(__name__)
CORS(app) 

@app.route('/get-data/<card_id>', methods=['POST'])
def refresh_data(card_id):
    if card_id == 'national_disasters':
        disaster_data = pd.read_csv('./National Disasters/Cleaned_csv.csv')
        print(disaster_data)
        # Convert the DataFrame to a dictionary
        disaster_data_counts = disaster_data['Year'].value_counts().sort_index()
        return jsonify(disaster_data_counts.to_dict())
    return jsonify({"error": "Invalid card_id"}), 400


@app.route('/eco-data/<card_id>', methods=['POST'])
def economics_data(card_id):
    if card_id == 'economic_deficits':
        try:
            eco_data = pd.read_csv('./Economic Deficits/india_data.csv')
            # Convert the DataFrame to a JSON format
            return jsonify(eco_data.to_dict(orient='records'))  # Convert DataFrame to JSON
        except Exception as e:
            return jsonify({"error": str(e)}), 500  # Handle file read errors
    return jsonify({"error": "Invalid card_id"}), 400

@app.route('/sentiment-data/<card_id>', methods=['POST'])
def sentiment_data(card_id):
    if card_id == 'national_sentiments':
        try:
            reddit_data = pd.read_csv('./News Sentiments/reddit_sentiments_analysis.csv')
            # Convert the DataFrame to a JSON format
            return jsonify(reddit_data.to_dict(orient='records'))  # Convert DataFrame to JSON
        except Exception as e:
            return jsonify({"error": str(e)}), 500  # Handle file read errors
    return jsonify({"error": "Invalid card_id"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
