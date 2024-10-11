from models import db, Affirmations
from app import app
from faker import Faker 
from random import choice as rc


with app.app_context():
    fake=Faker()
    
    Affirmations.query.delete()
    
    affirmations=[]
    affirmation_names=['I am awesome', 'I am strong', 'I am wise', 'I am loved', 'I am genius']
    dates=['9:00AM','12:00PM', '12:30PM', '4:00PM' ]
    
    for n in range (100):
        affirmation=Affirmations(hashtag=rc(affirmation_names), affirmation=fake.text(100), date=rc(dates))
        affirmations.append(affirmation)
        
        db.session.add_all(affirmations)
        db.session.commit()
    