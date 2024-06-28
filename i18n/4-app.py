#!/usr/bin/env python3
''' Flask app '''

from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config:
    ''' App config for languages '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


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
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
