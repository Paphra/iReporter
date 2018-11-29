
from flask import Flask, request, Response, url_for, jsonify

app = Flask(
    __name__,
    template_folder='/UI/',
    static_folder='/UI/assets/')

json_error = {"status": 400, "error": "json object error"}
no_flag_found = {"error": "No red flag found", "status": 404}


@app.route("/api/v1/red-flags", methods=['POST'])
def post_red_flag():
    data = request.get_json()
    if data is not None:
        flag_is_there = False
        if len(all_users) > 0:
            flag_is_there = flag_exists(data.get("title"), data.get("comment"))
        if flag_is_there:
            res = {
                "status": 200,
                "data": [{"id": 0, "message": "Flag Already reported!"}]}
            return (jsonify(res), 200)
        add_new_flag(data)
        res = {
            "status": 201,
            "data": [{
                "id": data.get("id"),
                "message": "Created red-flag record"}]}
        return (jsonify(res), 201)
    return (jsonify(json_error), 400)


def flag_exists(title, comment):
    for flag in all_flags:
        if flag["title"] == title and flag["comment"] == comment:
            return True
    return False


def add_new_flag(data):
    all_flags.append(data)

all_flags = []
all_users = []


@app.route("/api/v1/red-flags", methods=["GET"])
def get_all_flags():
    jdata = request.get_json()
    if jdata is not None:
        user_id = jdata.get("userId")
        data = []
        if user_is_admin(user_id):
            data = all_flags
        else:
            data = get_flags(user_id)
        res = {"status": 200, "data": data}
        return (jsonify(res), 200)
    return (jsonify(json_error), 400)


def get_flags(user_id):
    flags = []
    for flag in all_flags:
        if flag["createdBy"] == user_id:
            flags.append(flag)
    return flags


def user_is_admin(user_id):
    for user in all_users:
        if user["id"] == user_id and user["isAdmin"]:
                return True
    return False


@app.route("/api/v1/users", methods=["POST"])
def add_new_user():
    jdata = request.get_json()
    if jdata is not None:
        if get_user_details(jdata["username"], jdata["email"])["id"] != 0:
            res = {
                "status": 200,
                "data": [{
                    "id": jdata["id"],
                    "message": "User Already Exists"}]}
            return (jsonify(res), 200)
        add_user(jdata)
        msg = "New User Added!"
        if jdata["isAdmin"]:
            msg = "New Admin Added!"
        res = {
            "status": 201,
            "data": [{"id": jdata['id'], "message": msg}]}
        return (jsonify(res), 201)
    return (jsonify(json_error), 400)


@app.route("/api/v1/users", methods=["GET"])
def get_user_given_username_or_email():
    jdata = request.get_json()
    if jdata is not None:
        data = get_user_details(jdata["username"], jdata["email"])
        res = {"status": 200, "data": [data]}
        return (jsonify(res), 200)
    return (jsonify(json_error), 400)


def get_user_details(username, email):
    user_doesnot_exist_json = {"id": 0, "message": "User does not exist"}
    if len(all_users) == 0:
        return user_doesnot_exist_json
    for user in all_users:
        if user['username'] == username or user["email"] == email:
            return user
    return user_doesnot_exist_json


def add_user(jdata):
    all_users.append(jdata)


@app.route("/api/v1/red-flags/<flag_id>")
def get_specific_flag(flag_id):
    flag = get_flag(flag_id)
    if flag is not None:
        res = {"status": 200, "data": [flag]}
    else:
        res = {"status": 200, "data": []}
    return (jsonify(res), 200)


def get_flag(flag_id):
    for flag in all_flags:
        if flag["id"] == int(flag_id):
            return flag
    return None


@app.route("/api/v1/red-flags/<red_flag_id>", methods=["DELETE"])
def delete_red_flag(red_flag_id):
    if delete_flag(red_flag_id):
        res = {
            "status": 200,
            "data": [{
                "id": int(red_flag_id),
                "message": "red-flag has been deleted"}]}
        return (jsonify(res), 200)
    else:
        return (jsonify(no_flag_found), 404)


def delete_flag(flag_id):
    for flag in all_flags:
        if flag['id'] == int(flag_id):
            all_flags.remove(flag)
            return True
    return False


@app.route("/api/v1/red-flags/<red_flag_id>/location", methods=["PATCH"])
def edit_red_flag_location(red_flag_id):
    return edit_works(red_flag_id, "location", request)


def edit_works(flag_id, item, request_obj):
    jdata = request_obj.get_json()
    if jdata is not None:
        new_content = jdata[item]
        if edit_item(new_content, item, flag_id):
            res = {
                "data": [{
                    "id": int(flag_id),
                    "message": "Updated red-flag record's {}".format(item)
                }], "status": 200}
            return (jsonify(res), 200)
        return (jsonify(no_flag_found), 404)
    return (jsonify(json_error), 400)


def edit_item(new_content, item, flag_id):
    for flag in all_flags:
        if flag["id"] == int(flag_id):
            flag[item] = new_content
            return True
    return False


@app.route("/api/v1/red-flags/<red_flag_id>/comment", methods=["PATCH"])
def edit_red_flag_comment(red_flag_id):
    return edit_works(red_flag_id, "comment", request)


@app.route("/api/v1/red-flags/<red_flag_id>/title", methods=["PATCH"])
def edit_red_flag_title(red_flag_id):
    return edit_works(red_flag_id, "title", request)


@app.route("/api/v1/red-flags/<red_flag_id>/type", methods=["PATCH"])
def edit_red_flag_type(red_flag_id):
    return edit_works(red_flag_id, "type", request)


@app.route("/api/v1/red-flags/<red_flag_id>/status", methods=["PATCH"])
def edit_red_flag_status(red_flag_id):
    return edit_works(red_flag_id, "status", request)


if __name__ == '__main__':
    app.run()
