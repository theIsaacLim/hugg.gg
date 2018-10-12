"""
Your task: look for all the TODOS here and read them. Try and figure out how these work
"""

# Flask
from flask import render_template, flash, redirect, url_for, request, abort, send_from_directory
# app modules
from app import app
from app.links import *
from app.forms import *
import os
domain = "hugg.gg"


# Ignore this, it's just a favicon(the little icon at the top of your browser)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


# This will return receive.html when /receive/s/ is opened
@app.route('/receive/s')
def receiveSilent():
    # This is how you return a HTML file to the view.
    return render_template('receive.html')


@app.route('/')
def index():
    # TODO: Okay your first task ( return HTML file to the view )-Delete line 28
    pass
# TODO: Look at this function, then build the function below to share for a custom url
# This is the share function for silent hugs with no message
@app.route('/share/s')
def sendSilent():
    url = domain + url_for('receiveSilent') # url_for will get the url for a certain method
    return render_template('share.html', url=url)


# Share link for regular ids, num being the ID
@app.route('/share/<num>')
def share(num):
    pass
    # Fill this in based on the share link above


@app.route('/receive/<num>')
def receive(num):
    # TODO: Look at this
    """
    You may not have seen this type of statement in your earlier programming. In Python this is called a try/except statement
     but in other languages it goes by different names. Basically, this is how it works:

     try:
        do_something()
    except ErrorType:
        try_something_else()

    First, the program tries to do something(the code within the try block). If that fails with an ErrorType specified, then it tries something else.
    This is helpful for fool-proofing programs(making sure they cannot be broken)
    """
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


# TODO: look at this function. This is how you deal with forms, for reference
# Also look in the forms.py file
# This is the send function. The difference here is the GET and POST function.
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
        # Redirect to the share url with a num of a new url hex

    else:  # Form isn't submitted
        # Render the form
        return render_template("form.html", form=form)


# TODO: Look at this
# This is what an error handler looks like. Essentially, this handles a 404 error
# which is when a url is not found
@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html'), 404
