import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "my_very_own_very_very_secret_key_pleasedon'ttellanyoneineedothidethis"
    RECAPTCHA_PUBLIC_KEY = "6Lev92gUAAAAAKtCp7kOqaAzDAery_79JsPHL8Zb"
    RECAPTCHA_PRIVATE_KEY = "6Lev92gUAAAAAKFsg-UYLPSreqKHoG7_pxZkUD6K"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
