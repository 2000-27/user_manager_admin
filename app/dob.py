from app import db
from app.schema import UserSchema,RoleSchema
from app.model import Role

def insert_user(new_user,roles):
    print("data come in new product is =>>>>   ",new_user)
    Single_user=UserSchema()
    check_role=RoleSchema()
    check_role=Role.query.filter_by(role_name=roles).first()
    result = check_role.dump(check_role)
    print("your dkjfldskf",result)
    #db.session.add(new_user)
    #db.session.commit()
    return Single_user.jsonify(new_user)


def insert_role(new_role):
    print("your new role is ",new_role)
    Single_user=RoleSchema()
    db.session.add(new_role)
    db.session.commit()
    return Single_user.jsonify(new_role)
