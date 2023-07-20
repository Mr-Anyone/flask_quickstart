from flask import Flask 

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"
    app.config["SECRET_KEY"] = "thisisasecretkey"

    from model.encryption import bcrypt
    bcrypt.init_app(app)

    from model import init_db
    init_db(app)

    from views.home import home_blueprint
    app.register_blueprint(home_blueprint)
    return app

if __name__ == "__main__":
    app = create_app()
    
    app.run(debug=True)
