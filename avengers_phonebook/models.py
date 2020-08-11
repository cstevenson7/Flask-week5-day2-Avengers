from avengers_phonebook import app,db 
from werkzeug.security import generate_password_hash, check_password_hash 

from datetime import datetime 

#inheriting from the __init__ db
class User(db.Model):
    # setting id to primary key
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone_number = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
   
    post = db.relationship('Post', backref='author', lazy=True )

    def __init__(self,username,email,phone_number,password):
        self.username= username
        self.email = email
        self.phone_number = phone_number
        self.password = self.set_password(password)
    
    # don't want passwords in our database
    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
     

    def __repr__(self):
        return f'{self.username} has been created with {self.email} and {self.phone_number}'


