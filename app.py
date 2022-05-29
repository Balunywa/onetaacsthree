import os
import pyodbc
from flask import Flask, render_template, url_for, redirect
from LoopForms import PostEventForm, DelEventForm
import urllib.parse 
from flask_sqlalchemy import SQLAlchemy
from applicationinsights.flask.ext import AppInsights



params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=cbserver-one.database.windows.net;DATABASE=onetaacs;UID=balunlu;PWD=Test#123450;Connection Timeout=60")
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)


app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URL'] = 'sqllite:///'+os.path.join(basedir, 'data.sqlite')
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

###################################
### SQL Data Basse ###
###################################


app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

########################################
#### Application Insights ########
########################################

app.config['APPINSIGHTS_INSTRUMENTATIONKEY'] = 'b9955837-006a-4eb0-bb9c-360a7e7da449;IngestionEndpoint=https://centralus-2.in.applicationinsights.azure.com/;LiveEndpoint=https://centralus.livediagnostics.monitor.azure.com/'
# log requests, traces and exceptions to the Application Insights service
appinsights = AppInsights(app)


###################################################

 #Cretes a Class/Model and inherits a class db.model
 ###Models.PY as possible file### 
 
 ### Event Type Model #####
 
##################################################

                  
class EventType(db.Model):
    
    #manaul table name
    __tablename__ = 'eventtype'
    
    #uses that imported class to creae cloums with an intiall primart key (unique through out the tale)
    id = db.Column('eventtype_id', db.Integer, primary_key = True)
    event_types = db.Column(db.Text)
    
    #One to Many Relationship
    #The table will be a parent table with oen row having accessing to more than one row in another table
    #This creates relationship between event types  table and the event name
    #Bike to Many Services..
    eventname = db.relationship('EventName', backref='EventType', lazy='dynamic')
    
    #One to One Relatioship
    #This table will have one row connecting to only one row in the other DB table
    #One Bike & One Owner
    owner = db.relationship ('Owner', backref='EventType', uselist=False)
       
       #initalizes the class vairbaleS
    def __init__(self, event_types):
         self.event_types = event_types
                   
    def check_event_access(self):
       if self.owner:
            return f" Welcome to the  {self.event_name} and try to have some fun at our {self.first_location}"
       else:
         return f"You not regsitered for this {self.event_name} today"
                       
    def __repr__(self):
              return f"{self.event_types}"
          
    
    
################################################################

#### Event Name Model ######
                   
############################################################### 

class EventName(db.Model):
    
    #manaul table name
    __tablename__ = 'eventname'
    
    id = db.Column('eventname_id', db.Integer, primary_key = True)
    
    event_name = db.Column(db.Text)
    event_location = db.Column(db.Text)
    #map a forgein key from the bike table - priary key in another table - this key will be entered to specific entries
    eventtype_id = db.Column(db.Integer, db.ForeignKey('eventtype.eventtype_id'))
        
    def __init__(self, event_name, eventtype_id, event_location):
        
           self.event_name = event_name
           self.eventtype_id = eventtype_id
           self.event_location = event_location
                    
    def __repr__(self):
       
        return f"{self.event_name} {self.eventtype_id} {self.event_location}"
    
#####################################################

##### Owner Model ################

#################################################

class Owner(db.Model):
    
    #manaul table name
    __tablename__ = 'owners'
    
    id = db.Column('owners_id', db.Integer, primary_key = True)
    
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    evnettype_id = db.Column(db.Integer, db.ForeignKey('eventtype.eventtype_id'))
    
        
    def __init__(self, first_name, event_types, last_name):
        
           self.first_name = first_name
           self.event_types = event_types
           self.last_name = last_name
             
    def __repr__(self):
       
        return f"{self.first_name} {self.eventtypes_id} {self.last_name}"
    

############################################

#### View Function Take in user infomration and save/update

##### Map Bussines Logic to the HTML and CSS templates ########

###########################################  

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/post',methods=['GET', 'POST'] )
def post_event():
    form = PostEventForm()
    
    if form.validate_on_submit():
        
        post = form.event_types.data
        new_post = EventType(post)
        db.session.add(new_post)
        db.session.commit()
        
        return redirect(url_for('list_events'))
    
    return render_template('post_event.html', form = form )   
        
       
@app.route('/listevents')
def list_events(): 
    event_list = EventType.query.all()
    return render_template('list_events.html', event_list = event_list)
    

@app.route('/delete', methods=['GET','POST'])
def del_event_type():
    form =  DelEventForm()
    
    if form.validate_on_submit():
        eventid = form.eventtype_id.data
        eventtype = EventType.query.get(eventid)
        db.session.delete((eventtype))
        db.session.commit
        
        return redirect(url_for('list_events'))
    
    return render_template('delete_event.html', form = form )
    
    
if __name__ == '__main__':
    app.run(debug=True)
    
    
    
        
        
        
    
    

        
        
        
    
    
    
    


    
    