import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
#__file__db.py set /basiclaly grabbing the full path name

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = 'sqllite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

###################################################

class Loop(db.Model):
    
    #manaul table name
    __tablename__ = 'loop'
    
    id = db.Cloumn(db.Integer,primary_key=True)
    name = db.Cloumn(db.Text)
    location = db.Cloumn(db.Text)
    carnoplate = db.Column(db.Interger)
    
    def __init__(self,name,location,carnoplate):
        
           self.name = name
           self.location = location
           self.carnoplate = carnoplate
           
    def __repr__(self):
       
       return f"Loop {self.name} is going to {self.location} in car no plate {self.carnoplate}"
        
        
        
    





