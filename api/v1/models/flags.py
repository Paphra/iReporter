from flask import jsonify

all_flags = []


class FlagsModel():
    '''Flags Model Class

    This class contains the model for the flags submitted by the user
    during their interaction with the platform.
    All the fields required for every element of the flag is hereby
    established.'''

    def __init__(self, *args, **kwargs):
        self.json_error = {"status": 400, "error": "json object error"}
        self.no_flag_found = {"error": "No red flag found", "status": 404}
        return super().__init__(*args, **kwargs)

    def add_new_flag(self, data):
        new_flag = {
            "id": data["id"],
            "createdBy": data["createdBy"],
            "createdOn": data["createdOn"],
            "title": data["title"],
            "comment": data["comment"],
            "status": data["status"],
            "type": data["type"],
            "location": data["location"],
            "Images": data["Images"],
            "Videos": data["Videos"],
            "otherFiles": data["otherFiles"]}
        all_flags.append(new_flag)

    def flag_exists(self, title, comment):
        for flag in all_flags:
            if flag["title"] == title and flag["comment"] == comment:
                return True
        return False

    def get_user_flags(self, user_id):
        flags = []
        for flag in all_flags:
            if flag["createdBy"] == user_id:
                flags.append(flag)
        return flags

    def get_flag(self, flag_id):
        for flag in all_flags:
            if flag["id"] == int(flag_id):
                return flag
        return None

    def delete_flag(self, flag_id):
        for flag in all_flags:
            if flag['id'] == int(flag_id):
                all_flags.remove(flag)
                return True
        return False

    def edit(self, flag_id, item, request_obj):
        jdata = request_obj.get_json()
        try:
            new_content = jdata[item]
            if self.edit_flag(new_content, item, flag_id):
                res = {
                    "data": [{
                        "id": int(flag_id),
                        "message": "Updated red-flag record's {}".format(item)
                    }], "status": 200}
                return (jsonify(res), 200)
            return (jsonify(self.no_flag_found), 404)
        except (TypeError, KeyError, AttributeError):
            return (jsonify(self.json_error), 400)

    def edit_flag(self, new_content, item, flag_id):
        for flag in all_flags:
            if flag["id"] == int(flag_id):
                flag[item] = new_content
                return True
        return False
