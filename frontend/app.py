from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')


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
    try:
        # Request data from the backend
        response = requests.post('http://backend:8000/eco-data/economic_deficits')
        if response.status_code == 200:
            eco_data = response.json()  # Parse JSON response into Python data structure
        else:
            eco_data = []
            print(f"Backend returned an error: {response.status_code}")
    except Exception as e:
        eco_data = []
        print(f"Error connecting to backend: {e}")

    # Pass the data to the template
    return render_template('economicdeficits.html', eco_data=eco_data)

@app.route('/nationalsentiments')
def nationalsentiments():
    response = requests.post('http://backend:8000/sentiment-data/national_sentiments')
    if response.status_code == 200:
        reddit_data = response.json()
    else:
        reddit_data = []
    return render_template('nationalsentiments.html', reddit_data=reddit_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
