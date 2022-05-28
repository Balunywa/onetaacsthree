#Get All USERS
from app import db, EventType, EventName

def get_all_events():
  event_types = EventType.query.all()
  print(event_types)
  
  
def get_all_names():
  event_names = EventName.query.all()
  print(event_names)
  
get_all_events()
get_all_names()