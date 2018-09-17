# Flask
from flask import render_template

# app modules
from app import app


@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html'), 404
