#Get All USERS
from dbconnection import db, Singup_Profiles

def remove_users():  
    delete_users = Singup_Profiles.query.get(3)
    db.session.delete(delete_users)
    db.session.commit()
    
remove_users()
