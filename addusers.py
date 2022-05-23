#ADD USERS
from dbconnection import db, Singup_Profiles

def add_users():
    db.create_all()
    new_user_singnup = Singup_Profiles('Wa','Hu',256789032,'WH@gamil.com','Test',2,9,1988,'female')
    db.session.add_all([new_user_singnup])
    db.session.commit()
    print("Welcome to the InThaLoop " + new_user_singnup.first_name)

add_users()



