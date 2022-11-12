from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def main():
        return "Hello World"

    @app.route("/version")
    def version():
        return "1.0"

    return app
