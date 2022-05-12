from dbconnection import db, Singup_Profiles


#Creates all the tables transform the model class to a db table
db.create_all()

new_user_singnup = Singup_Profiles('Luke','Kaso',256789032,'Luke@gamil.com','Test',2,9,1988,'male')


db.session.add_all([new_user_singnup])
db.session.commit()


if new_user_singnup.first_name == 'Luke':
    
    print('Hello '+  new_user_singnup.first_name, 'Welcome to InThaLoop')
    
else:
    print("Please check with the administrator")
    