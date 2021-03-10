from flask import Flask
from config import *
from website import api, frontend

app = Flask(__name__, static_folder=None)
app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(frontend)

if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)