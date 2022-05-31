#ADD USERS
from app import db, EventType, EventName

def add_event():
    db.create_all()
    new_event = EventType('online','test','test','one')
    db.session.add_all([new_event])
    db.session.commit()
    print("Welcome to this " + new_event.event_types + " Event")
   

def add_eventname():
    db.create_all()
    new_name= EventName('Lunch', 'itlay')
    db.session.add_all([new_name])
    db.session.commit()
    print("Welcome to the " + new_name.event_name)
    #test

add_event()
add_eventname()


