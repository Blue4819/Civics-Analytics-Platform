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
    response = requests.post('http://backend:8000/get-data/national_disasters')
    if response.status_code == 200:
        disaster_data = response.json()
    else:
        disaster_data = []
    return render_template('nationaldisasters.html', disaster_data=disaster_data)

@app.route('/economicdeficits')
def economicdeficits():
    return render_template('economicdeficits.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
