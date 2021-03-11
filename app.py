from config import *
from website import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)