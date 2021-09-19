from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Poop'

    from .views import views
    from .secure import secure

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(secure, url_prefix='/')
    
    return app

     