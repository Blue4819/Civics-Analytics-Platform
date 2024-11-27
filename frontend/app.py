from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/nationalsentiments')
def nationalsentiments():
    return render_template('nationalsentiments.html')

@app.route('/nationaldisasters')
def nationaldisasters():
    # Fetch data from the backend
    response = requests.post('http://backend:8000/get-data/national_disasters_count')
    if response.status_code == 200:
        disaster_data_count = response.json()
    else:
        disaster_data_count = []

    response2 = requests.post('http://backend:8000/get-data/covid_data')
    if response2.status_code == 200:
        covid_data = response2.json()
        min_date = min(item['Date'] for item in covid_data) if covid_data else None
        max_date = max(item['Date'] for item in covid_data) if covid_data else None
    else:
        covid_data = []
    return render_template('nationaldisasters.html', disaster_data=disaster_data_count, covid_data = covid_data, min_date = min_date, max_date=max_date)

@app.route('/economicdeficits')
def economicdeficits():
    return render_template('economicdeficits.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
