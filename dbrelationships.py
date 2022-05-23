import os
import pyodbc
from flask import Flask
import urllib.parse 
from flask_sqlalchemy import SQLAlchemy

params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=cbserver-one.database.windows.net;DATABASE=onetaacs;UID=balunlu;PWD=Test#123450")

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URL'] = 'sqllite:///'+os.path.join(basedir, 'data.sqlite')
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

###################################################
 #Cretes a class and inherits a class db.model                     
class Bike(db.Model):
    
    #manaul table name
    __tablename__ = 'bikes'
    
    #uses that imported class to creae cloums with an intiall primart key (unique through out the tale)
    id = db.Column('bikes_id', db.Integer, primary_key = True)
    bike_make = db.Column(db.Text)
    bike_color = db.Column(db.Text)
    
    #One to Many Relationship
    #The table will be a parent table with oen row having accessing to more than one row in another table
    #This creates relationship between bike table and the service table
    #Bike to Many Services..
    services = db.relationship('service', backref='bike', lazy='dynamic')
    
    #One to One Relatioship
    #This table will have one row connecting to only one row in the other DB table
    #One Bike & One Owner
    owner = db.relationship ('Owner', backref='bike', uselist=False)
       
       #initalizes the class vairbaled
    def __init__(self, bike_make, bike_color):
        
        
           self.bike_make = bike_make
           self.bike_color = bike_color
             
    def __repr__(self):
        if self.owner:
         return f" Bike Make Is {self.bike_make} and owner {self.first_name}"
        else:
          return f"Bike Make is {self.bike_make} and has no owner yet!"
     
    def report_service(self):
        print("Her are your services")
        for ser in self.service:
            print(service.service_name)
                   
############################################################### 

class service(db.Model):
    
    #manaul table name
    __tablename__ = 'services'
    
    id = db.Column('services_id', db.Integer, primary_key = True)
    
    service_name = db.Column(db.Text)
    service_type = db.Column(db.Text)
    #map a forgein key from the bike table - priary key in another table - this key will be entered to specific entries
    bike_id = db.Column(db.Integer, db.ForeignKey('bikes.bikes_id'))
        
    def __init__(self, service_name, bike_id, service_type):
        
           self.service_name = service_name
           self.bike_id = bike_id
           self.service_type = service_type
           
             
    def __repr__(self):
       
        return f"{self.service_name} {self.bike_id} {self.service_type}"
    
#####################################################

class Owner(db.Model):
    
    #manaul table name
    __tablename__ = 'owners'
    
    id = db.Column('owners_id', db.Integer, primary_key = True)
    
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    bike_id = db.Column(db.Integer, db.ForeignKey('bikes.bikes_id'))
    
        
    def __init__(self, first_name, bike_id, last_name):
        
           self.first_name = first_name
           self.bike_id = bike_id
           self.last_name = last_name
             
    def __repr__(self):
       
        return f"{self.first_name} {self.bike_id} {self.last_name}"
    
    