from flask import Flask
from extensions import db
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    CORS(app)

    app.config.from_pyfile('config.py', silent=True)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app

app = create_app()

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=4000,
    )
