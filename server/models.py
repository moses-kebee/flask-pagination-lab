from flask_sqlalchemy import SQLAlchemy
from config import db
from marshmallow import Schema, fields

class Book(db.Model):
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    
    def __repr__(self):
        return f'<Book {self.title}>'

class BookSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    author = fields.Str()
    description = fields.Str()