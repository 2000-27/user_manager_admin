import re 
from app.schema import RoleSchema
from app.model import Role
def email_check(email):
    if not re.match(r'[^@]+@[^@]+\.[^@]+',email):  
           msg = 'INVALID EMAIL ADDRESS !!!!'
    else :
          msg =True
    return msg       
    
def user_check(username):
        if not (re.match(r'[a-zA-Z0-9\s]+$',username)): 
           msg = 'Username must contain only characters , digit  and space !!!!!'    
        else:
           msg=True   
        return msg


def set_role_id(user_role):
     single_role=RoleSchema()
     check_role=Role.query.filter_by(role_name=user_role).first()
     result = single_role.dump(check_role)
     print("your user is",result)