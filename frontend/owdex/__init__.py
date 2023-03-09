import os

import flask as f
from dotenv import load_dotenv

from .usermanager import UserManager
from .assets import asset
from .static import static_page
from .search import search
from .add import add
from .users import users


def create_app():
    app = f.Flask("owdex")

    load_dotenv()
    app.config.update(SECRET_KEY=os.environ.get("secret_key"))

    app.um = UserManager(dev_mode=app.config["DEBUG"])

    with app.app_context():
        app.register_blueprint(asset, url_prefix="/assets")
        app.register_blueprint(static_page)
        app.register_blueprint(search)
        app.register_blueprint(add)
        app.register_blueprint(users)

    return app
