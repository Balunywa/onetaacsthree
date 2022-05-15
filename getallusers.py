#Get All USERS
from dbconnection import db, Singup_Profiles

def get_all_users():
  all_users = Singup_Profiles.query.all()
  print(all_users)

get_all_users()