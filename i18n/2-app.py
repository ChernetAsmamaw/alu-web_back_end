#!/usr/bin/env python3
""" Setup a basic Flask app  """
from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ determine the best match with our supported languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

class Config:
    """ Config class for Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ index function to render a simple html template """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
