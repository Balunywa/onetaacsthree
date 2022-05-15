
from dbconnection import db, Friend_Profiles

def add_users():
    db.create_all()
    invite_new_friend = Friend_Profiles ('Wa','Hu','WH@gamil.com')
    db.session.add_all([invite_new_friend])
    db.session.commit()
    print("Invite Sent to " + invite_new_friend.first_name)

add_users()