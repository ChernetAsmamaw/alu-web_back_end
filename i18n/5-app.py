#!/usr/bin/env python3
""" Setup a basic Flask app  """

from flask import Flask, request, render_template, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Config class for Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request():
    """ call get_user function before each request """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """ determine the best match with our supported languages """
    locale = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(app.config.LANGUAGES)
                                               

@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ index function to render a simple html template """
    return render_template('5-index.html')


def get_user():
    """ get user from request """
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users.get(int(user_id))
    return None


if __name__ == '__main__':
    app.run()
