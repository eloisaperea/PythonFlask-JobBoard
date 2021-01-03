from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def job():
    return render_template('index.html')
