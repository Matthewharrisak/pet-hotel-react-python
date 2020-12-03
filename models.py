from app import db

# class Pet(db.Model):
#     __tablename__ = 'pets'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String())
#     breed = db.Column(db.String())
#     color = db.Column(db.String())
#     is_checked_in = db.Column(db.String())


#     def __init__(self, name, breed, color, is_checked_in):
#         self.name = name
#         self.breed = breed
#         self.color = color
#         self.is_checked_in = is_checked_in

#     def __repr__(self):
#         return '<id {}>'.format(self.id)
    
#     def serialize(self):
#         return {
#             'id': self.id, 
#             'name': self.name,
#             'breed': self.breed,
#             'color':self.color,
#             'is_checked_in':self.is_checked_in
#         }