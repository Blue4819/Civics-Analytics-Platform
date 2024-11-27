from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import random
import os

app = Flask(__name__)
CORS(app) 

@app.route('/get-data/<card_id>', methods=['POST'])
def refresh_data(card_id):
    if card_id == 'national_disasters_count':
        disaster_data = pd.read_csv('./National Disasters/Cleaned_csv.csv')
        # Convert the DataFrame to a dictionary
        disaster_data_counts = disaster_data['Year'].value_counts().sort_index()
        return jsonify(disaster_data_counts.to_dict())
    
    if card_id == 'covid_data':
        covid_data = pd.read_csv('./National Disasters/Covid_cleaneddata .csv')
        return jsonify(covid_data.to_dict(orient='records'))

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
            reddit_data = pd.read_csv('./News Sentiments/reddit_sentiment_analysis.csv')
            print(reddit_data.head())
            if reddit_data.empty:
                return jsonify({"error": "No data found"}), 404
        
        # Convert DataFrame to JSON
            return jsonify(reddit_data.to_dict(orient='records'))  # Convert DataFrame to JSON
        except Exception as e:
            print(f"Error: {e}")  # Print error for debugging
            return jsonify({"error": str(e)}), 500  # Handle file read errors

@app.route('/fetch-news', methods=['GET'])
def fetch_news():
    try:
        # Replace this with your actual news extraction logic
        news_data = extract_top_five_news()  # Implement this function to fetch news
        return jsonify(news_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def extract_top_five_news():
    # Example logic to fetch news
    # This should be replaced with your actual news extraction logic
    news = [
        {"title": "News Article 1"},
        {"title": "News Article 2"},
        {"title": "News Article 3"},
        {"title": "News Article 4"},
        {"title": "News Article 5"},
    ]
    return news

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
