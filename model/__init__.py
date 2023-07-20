from .model import db 

def init_db(app):
    from .product import ProductTable
    
    db.init_app(app)
    with app.app_context():
        db.create_all()