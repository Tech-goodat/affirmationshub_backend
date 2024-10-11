from flask import Flask, request, make_response
from models import db, Affirmations, User
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
CORS(app)

@app.route('/')
def index():
    response_body = {
        'message': 'Welcome to React, served by Flask'
    }
    return make_response(response_body, 200)

@app.route('/affirmations', methods=['GET', 'POST'])
def affirmations():
    if request.method == 'GET':
        affirmations = [affirmation.to_dict() for affirmation in Affirmations.query.all()]
        return make_response(affirmations, 200)

    elif request.method == 'POST':
        data = request.get_json()  # Use get_json to fetch data from request body
        new_affirmation = Affirmations(
            hashtag=data.get('hashtag'),
            affirmation=data.get('affirmation'),
            date=data.get('date')
        )
        db.session.add(new_affirmation)
        db.session.commit()
        return make_response(new_affirmation.to_dict(), 201)

@app.route('/affirmations/<int:id>', methods=['GET', 'DELETE', 'PATCH'])
def affirmations_by_id(id):
    affirmation = Affirmations.query.filter_by(id=id).first()
    
    if not affirmation:
        return make_response({"error": "Affirmation not found"}, 404)

    if request.method == 'GET':
        return make_response(affirmation.to_dict(), 200)

    elif request.method == 'DELETE':
        db.session.delete(affirmation)
        db.session.commit()
        return make_response({"message": "Affirmation deleted successfully"}, 204)

    elif request.method == 'PATCH':
        for attr in request.form:
            setattr(affirmation, attr, request.form.get(attr))
        db.session.commit()
        return make_response(affirmation.to_dict(), 200)
    
@app.route('/users', methods=[ 'POST'])
def users():
    if request.method == 'POST':
        data=request.get_json()
        new_user=User(
            user_name=data.get('user_name'),
            age=data.get('age')
        )
        
        db.session.add(new_user)
        db.session.commit()
        return make_response(new_user.to_dict(), 201)
    
    
    
@app.route('/users_by_id/<int:id>', methods=['GET'])
def users_by_id(id):
    if request.method == 'GET':
         user=[user.to_dict() for user in User.query.filter_by(User.id == id).first()]
         response=make_response(user, 200)
         return response
              

if __name__ == '__main__':
    app.run(port=5555, debug=True)
