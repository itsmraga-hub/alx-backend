#!/usr/bin/env python3
"""
    In order to configure available languages in our app, you will create a
    Config class that has a LANGUAGES class attribute equal to ["en", "fr"].
    Use Config to set Babel’s default locale ("en") and timezone ("UTC").
    Use that class as config for your Flask app.
"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)
app.url_map.strict_slashes = False


class Config:
    """
        Class Config for the basic flask app
        Use Config to set Babel’s default locale ("en") and timezone ("UTC")
        Use that class as config for your Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index() -> str:
    """
        Index root function for root page
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
