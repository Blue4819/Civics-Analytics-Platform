from flask import Flask, request, jsonify
import pandas as pd
import random
import os

app = Flask(__name__)

@app.route('/get-data/<card_id>', methods=['POST'])
def refresh_data(card_id):
    # Assuming card_id corresponds to the CSV file you want to read
    if card_id == 'national_disasters':
        csv_file_path = os.path.join('./National Disasters', 'Cleaned_csv.csv')
        disaster_data = pd.read_csv(csv_file_path)
        # Convert the DataFrame to a dictionary
        return jsonify(disaster_data.to_dict(orient='records'))
    return jsonify({"error": "Invalid card_id"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
