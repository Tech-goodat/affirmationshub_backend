from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

metadata=MetaData()
db=SQLAlchemy(metadata=metadata)

class Affirmations(db.Model, SerializerMixin):
    __tablename__='affirmations'
    
    id=db.Column(db.Integer, primary_key=True)
    hashtag=db.Column(db.String)
    affirmation=db.Column(db.String(200))
    date=db.Column(db.String)
    
    def __repr__(self):
        return f'<Affirmations {self.id}, {self.hashtag}, {self.affirmation}>'
    
class User(db.Model, SerializerMixin):
    __tablename__='user'
    
    id=db.Column(db.Integer, primary_key=True)
    user_name=db.Column(db.String)
    age=db.Column(db.Integer)
    
    def __repr__(self):
        return f'<User {self.id}, {self.user_name}, {self.age} >'
        