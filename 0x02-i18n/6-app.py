#!/usr/bin/env python3
"""
    Create a get_locale function with the babel.localeselector decorator.
    Use request.accept_languages to determine the best match with our
    supported languages.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from typing import Union, Dict


app = Flask(__name__)
babel = Babel(app)
app.url_map.strict_slashes = False


class Config:
    """
        Class Config for the basic flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


# Mock user data
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """
        detect and return based on locale
    """
    user_locale = None

    if 'locale' in request.args:
        if request.args['locale'] in app.config['LANGUAGES']:
            user_locale = request.args.get('locale')

    if g.user and g.user.get("locale") in app.config['LANGUAGES']:
        user_locale = g.user.get("locale")

    if request.accept_languages:
        best_match = request.accept_languages.best_match(
                app.config['LANGUAGES'])
        if best_match:
            user_locale = best_match

    if user_locale is None:
        user_locale = app.config['BABEL_DEFAULT_LOCALE']

    return user_locale


def get_user(user_id) -> Union[Dict, None]:
    """
        Method to get user using user id passed as parameter
    """
    return users.get(user_id)


@app.before_request
def before_request() -> None:
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None
    # print(g.user)


@app.route('/')
def index() -> str:
    """
        root index page
    """
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
