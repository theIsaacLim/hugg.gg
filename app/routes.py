# Flask
from flask import render_template, flash, redirect, url_for, request, abort
from app import app


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/send')
def send():
    return render_template("form.html")


@app.route('/share')
def share():
    return render_template("share.html")
