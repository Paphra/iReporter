from flask import jsonify

all_users = []


class UsersModel():
    '''Users Model Class

    This class is used to setup the storage for the users of the
    platform.
    The user model, containing all the fields is in this class.'''

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def add_user(self, jdata):
        new_user = {
            "id": jdata["id"],
            "username": jdata["username"],
            "firstname": jdata["firstname"],
            "lastname": jdata["lastname"],
            "othernames": jdata["othernames"],
            "email": jdata["email"],
            "password": jdata["password"],
            "phoneNumber": jdata["phoneNumber"],
            "address": jdata["address"],
            "isAdmin": jdata["isAdmin"],
            "registered": jdata["registered"],
            "occupation": jdata["occupation"],
            "gender": jdata["gender"]}
        all_users.append(new_user)

    def is_admin(self, user_id):
        for user in all_users:
            if user["id"] == user_id and user["isAdmin"]:
                return True
        return False

    def user_exists(self, username, email):
        if len(all_users) == 0:
            return {"id": 0}
        for user in all_users:
            if user["email"] == email or user["username"] == username:
                return user
        return {"id": 0}

    def get_details(self, name, password):
        user_does_not_exist = (jsonify({
            "error": "User does not exist", "status": 404}), 404)
        if len(all_users) == 0:
            return user_does_not_exist
        for user in all_users:
            if self.check_name(user, name) and \
                    self.check_password(user, password):
                return (jsonify({"status": 200, "data": [user]}), 200)
            elif self.check_name(user, name) and not \
                    self.check_password(user, password):
                return (jsonify({
                    "error": "invalid password", "status": 401}), 401)
        return user_does_not_exist

    def check_name(self, user, name):
        if (user['username'] == name or user["email"] == name):
            return True
        return False

    def check_password(self, user, password):
        if user["password"] == password:
            return True
        return False
