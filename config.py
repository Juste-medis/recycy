import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '68g6(-_54146e4-njt8zerynj_$*yryg68zrryjb)'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER =  os.path.join(basedir, 'app/static/uploads/') 
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
 
 
    JWT_SECRET_KEY= '*PFiPoWY1vT]v6bL-Ty-?U)[L(}/yF)'
    MAIL_SERVER= 'nubie.o2switch.net'
    MAIL_PORT= 465
    MAIL_USE_TLS= True
    MAIL_USE_SSL= False
    MAIL_USERNAME= 'yambro@adidome.com'
    MAIL_PASSWORD= '5ChA6d~ojr9!'
    MAIL_DEFAULT_SENDER= 'visionrec@example.com'