# Flask
from flask import render_template, flash, redirect, url_for, request, abort, send_from_directory
from app import app
from app.links import *
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
        return redirect(url_for('share', num=add_newrl(message)))
    else:
        return render_template("form.html")


@app.route('/share/<num>')
def share(num):
    return render_template("share.html", url="hugg.gg" + url_for('receive', num=hex(int(num))))


@app.route('/receive/<num>')
def receive(num):
    try:
        url_id = int(num, 0)
    except ValueError:
        abort(404)

    try:
        url_data = get_existing_url(url_id)
    except TypeError:
        abort(404)

    print(url_data)
    try:
        return render_template("receive.html", message=url_data["message"])
    except KeyError:
        return render_template("receive.html")
