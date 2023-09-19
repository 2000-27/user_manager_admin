from flask import request,jsonify,Blueprint
from app.model import User,Role
from app.util import email_check,user_check
from app.dob import insert_role,insert_user
second=Blueprint("/second",__name__)

@second.route('/login', methods =['POST'])
def login():
  try:
    json_body = request.get_json()
    msg = ''
    if request.method == 'POST'  :
        username = json_body['username']
        email = json_body['email']
        userpassword = json_body['userpassword']
        roles=json_body['roles']
        email_ans=email_check(email)
        user_ans=user_check(username)
        if email_ans==True and user_ans==True:
             msg = 'Registeration successfull'
             print("yur role is ",roles)
             print("your other details are ",user_ans,email_ans,username,userpassword)
             new_User = User(email, userpassword,username )
             print("innnndfkjdkfjdlkfjl")
             insert_user(new_User,roles)
             return jsonify({})
        else :
            msg=email_ans
            return jsonify({"message : ": msg})    
              

  except Exception as error :
    msg="there is error "
    print("your error is ",error)
    return jsonify({"msg": msg})
    

