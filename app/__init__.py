# Flask
from flask import Flask

# app modules
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes, errors
