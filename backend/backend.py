from flask import Flask, request, jsonify
import pandas as pd
import random
import os

app = Flask(__name__)

@app.route('/get-data/<card_id>', methods=['POST'])
def refresh_data(card_id):
    if card_id == 'national_disasters':
        disaster_data = pd.read_csv('./National Disasters/Cleaned_csv.csv')
        print(disaster_data)
        # Convert the DataFrame to a dictionary
        disaster_data_counts = disaster_data['Year'].value_counts().sort_index()
        return jsonify(disaster_data_counts.to_dict())
    return jsonify({"error": "Invalid card_id"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
