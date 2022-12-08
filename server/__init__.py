from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def main():
        return "Hello World Testing Branch"

    @app.route("/version")
    def version():
        return "1.0"

    with app.app_context():
        CORS(app)

    return app
