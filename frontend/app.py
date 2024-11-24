from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/nationalsentiments')
def nationalsentiments():
    return render_template('nationalsentiments.html')

@app.route('/nationaldisasters')
def nationaldisasters():
    return render_template('nationaldisasters.html')

@app.route('/economicdeficits')
def economicdeficits():
    return render_template('economicdeficits.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
