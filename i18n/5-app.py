#!/usr/bin/env python3
''' Flask app '''

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    ''' App config for languages '''
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
    ''' Will be excuted before any request '''
    g.user = get_user()



def get_user():
    ''' Retrive user info form users dict'''
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    else:
        return None


@babel.localeselector
def get_locale():
    """Determine the user's preferred language.

    Returns:
        str: The language code ('en' for English, 'fr' for French, etc.).
    """
    locale = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=["GET"], strict_slashes=False)
def index():
    ''' Render the main index template.

    Returns:
        str: Rendered HTML template.
    '''
    login = False
    if g.get('user'):
        login = True
    return render_template('5-index.html', login=login)


if __name__ == '__main__':
    app.run()
