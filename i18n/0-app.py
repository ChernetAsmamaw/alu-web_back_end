#!/usr/bin/env python3
""" setup a basic Flask app  """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
"""index function to render the 0-index.html template"""
def index():
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
