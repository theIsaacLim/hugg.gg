# Flask
from flask import render_template, flash, redirect, url_for, request, abort

@app.route('/')
def index():
    return render_template()
