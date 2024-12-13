import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        return "Hello from Koyeb!"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
