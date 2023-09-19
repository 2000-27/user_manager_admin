from flask import request,jsonify,current_app,Blueprint
from app.model import User
from app.schema import UserSchema 
from datetime import datetime,timedelta
import jwt

new_mold=Blueprint("auth",__name__)

@new_mold.route('/signup', methods =['POST'])
def signup():
    json_body = request.get_json()
    check_record=UserSchema()
    msg = ''
    if request.method == 'POST':
        userpassword = json_body['userpassword']
        email = json_body['email']
        try:  
           check_email=User.query.filter_by(email=email).first()
           result = check_record.dump(check_email)
           if result=={}:
               msg="PLEASE SIGNIN   !!!"
               
           else:    
               msg="SIGN UP SUCCESSFULLY !!!!"

               token = jwt.encode({'public_id': 1,'exp' :str( datetime.utcnow() + timedelta(minutes = 30)) },current_app.config.get('SECRET_KEY'))
               return jsonify(message="  LOGIN SUCCESSFULLY !!! ", access_token=token)
               
        except  Exception as error:
          print(error)
          msg= 'THERE IS NO USER !!!!'
        
        return jsonify({"msg": msg})

