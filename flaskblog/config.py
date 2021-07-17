import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')  
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'imap.web.de'
    MAIL_PORT = 993
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    MONGODB_SETTINGS = {
        'username': os.environ.get("MONGODB_BLOG_USERNAME"),
        'password': os.environ.get("MONGODB_BLOG_PASSWORD"),
        'host': os.environ.get("MONGODB_DATABASE_BLOG_URI")
    }
# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY')
#     #SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    
#     MAIL_SERVER = 'smtp.googlemail.com'
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = os.environ.get('EMAIL_USER')
#     MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
#     MONGODB_SETTINGS = {
#         'username': os.environ.get("MONGODB_BLOG_USERNAME"),
#         'password': os.environ.get("MONGODB_BLOG_PASSWORD"),
#         'host': os.environ.get("MONGODB_DATABASE_BLOG_URI")
#     }