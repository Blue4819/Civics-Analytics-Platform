from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')



@app.route('/nationaldisasters')
def nationaldisasters():
    # Fetch data from the backend
    response = requests.post('http://backend:8000/get-data/national_disasters')
    if response.status_code == 200:
        disaster_data = response.json()
    else:
        disaster_data = []
    return render_template('nationaldisasters.html', disaster_data=disaster_data)

@app.route('/economicdeficits')
def economicdeficits():
    response = requests.post('http://backend:8000/eco-data/economic_deficits')
    if response.status_code == 200:
        eco_data = response.json()
    else:
        eco_data = []
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
