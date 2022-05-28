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
                      
class Singup_Profiles(db.Model):
    
    #manaul table name
    #__tablename__ = 'loop'
    
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    mobile_number = db.Column(db.Integer)
    email_id = db.Column(db.Text)
    new_password = db.Column(db.Text)
    dateob = db.Column(db.Integer)
    monthob = db.Column(db.Integer)
    yearob = db.Column(db.Integer)
    sex = db.Column(db.Text)
     
        
    def __init__(self, first_name, last_name,mobile_number,email_id, new_password, dateob, monthob, yearob, sex):
        
           self.first_name = first_name
           self.last_name = last_name
           self.mobile_number = mobile_number
           self.email_id = email_id
           self.new_password = new_password
           self.dateob = dateob
           self.monthob = monthob
           self.yearob = yearob
           self.sex = sex
             
    def __repr__(self):
       return f"{self.first_name} {self.last_name} {self.mobile_number} {self.email_id} {self.new_password} {self.dateob} {self.monthob} {self.yearob} {self.sex}"
       
   ############################################################### 

class Friend_Profiles(db.Model):
    
    #manaul table name
    #__tablename__ = 'loop'
    
    id = db.Column('friend_id', db.Integer, primary_key = True)
    
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    email_id = db.Column(db.Text)
   
        
    def __init__(self, first_name, last_name,email_id):
        
           self.first_name = first_name
           self.last_name = last_name
           self.email_id = email_id
             
    def __repr__(self):
       
        return f"{self.first_name} {self.last_name} {self.email_id}"
    
    
     #   $('[data-toggle=dropdown]').each(function() {
     # this.addEventListener('click', function() {}, false);
    # });
