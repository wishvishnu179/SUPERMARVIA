import logging
import os
import requests
from flask import Flask

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route("/")
def hello():
    try:
        # Your application logic here
        return "Hello from Koyeb!"
    except requests.exceptions.RequestException as e:
        logging.error(f"Network error: {e}")
        return f"Network error occurred: {e}"
    except Exception as e:
        logging.exception(f"An unexpected error occurred: {e}")
        return f"An unexpected error occurred."

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get("PORT", 8000)))
