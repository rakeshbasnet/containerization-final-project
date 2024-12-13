from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS

app = Flask(__name__, template_folder="../templates", static_folder="../static")

# Load environment variables from .env file
load_dotenv()
CORS(app)

from app import routes
