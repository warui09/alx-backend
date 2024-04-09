#!/usr/bin/env python3
"""basic Flask app"""

from flask import Flask, render_template, g, request
from flask_babel import Babel, _
from typing import Dict, Optional

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """config class for app"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user() -> Optional[Dict]:
    """get user if user exists"""

    user_id = request.args.get("login_as")

    if user_id:
        return users.get(int(user_id))

    return None


@app.before_request
def before_request():
    """set user as a global variable"""

    g.user = get_user()
    print(g.user)


@babel.localeselector
def get_locale() -> str:
    """get language that best matches supported ones"""

    language = request.args.get("locale")
    if language and language in Config.LANGUAGES:
        return language

    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/")
def index() -> str:
    """render the index page"""

    return render_template(
        "5-index.html",
        title=_("home_title"),
        header=_("home_header"),
    )


if __name__ == "__main__":
    app.run()
