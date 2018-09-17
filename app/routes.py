# Flask
from flask import render_template, flash, redirect, url_for, request, abort, send_from_directory
from app import app
import os


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/send', methods=["GET", "POST"])
def send():
    if request.method == 'POST':
        message = request.values.get('message')
        print(message)
        return redirect(url_for('share', num=1))
    else:
        return render_template("form.html")


@app.route('/share/<num>')
def share(num):
    return render_template("share.html", url="hugg.gg" + url_for('receive', num=num))


@app.route('/receive/<num>')
def receive(num):
    return num
