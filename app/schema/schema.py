from app import ma 

class UserSchema(ma.Schema):
      class Meta:
            fields=('id','username','userpassword','email','role')


class RoleSchema(ma.Schema):
      class Meta:
            fields=('id','userole')


