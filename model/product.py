from .model import db 
import sqlalchemy as sa

class ProductTable(db.Model):
    id = sa.Column(sa.Integer(), unique=True, primary_key=True)
    name = sa.Column(sa.String(100), nullable=False)