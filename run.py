from applications import create_app
from config import config

config()
app = create_app()

if __name__ == "__main__":
    app.run(debug=False, port=8000)
