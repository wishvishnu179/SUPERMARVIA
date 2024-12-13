import logging
import os
import requests
from flask import Flask

app = Flask(__name__)

# More robust logging configuration
logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(levelname)s - %(message)s',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'level': logging.ERROR,  # Adjust logging level as needed
        }
    },
    'root': {
        'handlers': ['console'],
        'level': logging.ERROR,  # Adjust logging level as needed
    }
})


@app.route("/")
def hello():
    try:
        return "Hello from Koyeb!"
    except requests.exceptions.RequestException as e:
        logging.exception(f"Network error: {e}")  # Use logging.exception to include traceback
        return f"Network error occurred: {e}"
    except Exception as e:
        logging.exception(f"An unexpected error occurred: {e}")  # Use logging.exception to include traceback
        return f"An unexpected error occurred."


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get("PORT", 8000)))
