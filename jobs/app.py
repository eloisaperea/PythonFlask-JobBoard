import sqlite3
from flask import Flask, render_template, g

PATH = db/jobs.sqlite

app = Flask(__name__)
def open_connection():
    getattr(flask.g, '_connection', None)
    return getattr(connection)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
