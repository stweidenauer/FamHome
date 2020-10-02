class Config:
    # todo Bring all the variables to environmental variables
    # in ubuntu ~/.profile see yt corey shaefer
    SECRET_KEY = "hard to guess string"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'codessteffen'
    MAIL_PASSWORD = 'fl@5kcode'
