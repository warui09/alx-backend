#!/usr/bin/env python3
"""basic Flask app"""

from flask import Flask, render_template, g, request
from flask_babel import Babel, _


class Config:
    """config class for app"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """get language that best matches supported ones"""

    language = request.args.get('locale')
    if language and language in Config.LANGUAGES:
        return language

    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/")
def index() -> str:
    """render the index page"""

    return render_template("4-index.html", title=_('home_title'), header=_('home_header'))


if __name__ == "__main__":
    app.run()
