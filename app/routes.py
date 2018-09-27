# Flask
from flask import render_template, flash, redirect, url_for, request, abort, send_from_directory
from app import app
from app.links import *
from app.forms import *
import os
domain = "hugg-gg.herokuapp.com"


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/send', methods=["GET", "POST"])
def send():
    form = hug()

    # If form submitted and valid
    if form.validate_on_submit():
        message = form.message.data
        print(message)
        if message is '':
            return redirect(url_for('sendSilent'))
        return redirect(url_for('share', num=hex(add_newrl(message))))
    else:
        return render_template("form.html", form=form)


@app.route('/share/<num>')
def share(num):
    return render_template("share.html", url=domain + url_for('receive', num=int(num, 0)))


@app.route('/share/s')
def sendSilent():
    return render_template('share.html', url=domain + url_for('receiveSilent'))


@app.route('/receive/s')
def receiveSilent():
    return render_template('receive.html')


@app.route('/receive/<num>')
def receive(num):
    try:
        url_id = int(num, 0)
    except ValueError:
        abort(404)

    try:
        url_data = get_existing_url(url_id)
    except StopIteration:
        abort(404)
    try:
        return render_template("receive.html", message=url_data["message"])
    except KeyError:
        return render_template("receive.html")
