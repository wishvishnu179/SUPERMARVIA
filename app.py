from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":
    # Use the port from the environment or default to 8000
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
