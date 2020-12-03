from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

## postgres:postgres was looking for the route of postgres which didn't exist. 
app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/pet-hotel-python"
migrate = Migrate(app, db)

## this is our route to connect to DB 
class PetModel(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    breed = db.Column(db.String())
    color = db.Column(db.String())
    is_checked_in = db.Column(db.String())


    def __init__(self, name, breed, color, is_checked_in):
        self.name = name
        self.breed = breed
        self.color = color
        self.is_checked_in = is_checked_in

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    # def serialize(self):
    #     return {
    #         'id': self.id, 
    #         'name': self.name,
    #         'breed': self.breed,
    #         'color':self.color,
    #         'is_checked_in':self.is_checked_in
    #     }

@app.route('/pet', methods=['GET'])
def pet_get():
    if request.method == 'GET':
        pets = PetModel.query.all()
        results = [
            {   "id": pet.id,
                "name": pet.name,
                "breed": pet.breed,
                "color": pet.color,
                "is_checked_in": pet.is_checked_in
            } for pet in pets]
        
    return {"pets": results}


    

app.config['DEBUG'] = True


if __name__ == '__main__':
    app.run()
