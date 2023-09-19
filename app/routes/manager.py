from app import db
from app.model import User, roles_users
from flask_security import roles_accepted


#@app.route('/Manager')
#@roles_accepted('Admin')
# def Manager():
#     manager = []
#     role_manager = db.session.query(roles_users).filter_by(role_id=2)
#     for manag in role_manager:
#         user = User.query.filter_by(id=manag.user_id).first()
#         manager.append(user)
   
       