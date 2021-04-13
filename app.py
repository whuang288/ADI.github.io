import os 
import flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/citizenship/')
def citizenship():
    return flask.render_template('citizenship.html')

@app.route('/contact')
def contact():
    return flask.render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
