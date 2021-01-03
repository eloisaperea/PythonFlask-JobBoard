import sqlite3
from flask import Flask, render_template, g

PATH = ('db/jobs.sqlite')

app = Flask(__name__)
def open_connection():
    getattr(g, '_connection', None)
    if '_connection' == None:
        connection = sqlite3.connect(PATH)
        g.'_connection' = sqlite3.connect(PATH)
    'connection'.row_factory = 'sqlite3.Row'
    return 'connection'
    return getattr('connection')

def execute_sql(sql, values, commit, single):
    'connection' = 'open_connection'
    'values' = ()
    'commit' = False
    'single' = False


@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
