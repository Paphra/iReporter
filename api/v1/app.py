
from flask import Flask, request, Response, url_for, jsonify

app = Flask(
    __name__,
    template_folder='/UI/',
    static_folder='/UI/assets/')

json_error = {"status": 400, "error": "json object error"}
no_flag_found = {"error": "No red flag found", "status": 404}
all_flags = []
all_users = []


@app.route("/api/v1/red-flags", methods=['POST'])
def post_red_flag():
    data = request.get_json()
    try:
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
    except (TypeError, KeyError, AttributeError):
        return (jsonify(json_error), 400)


def flag_exists(title, comment):
    for flag in all_flags:
        if flag["title"] == title and flag["comment"] == comment:
            return True
    return False


def add_new_flag(data):
    all_flags.append(data)


@app.route("/api/v1/red-flags", methods=["GET"])
def get_all_flags():
    jdata = request.get_json()
    try:
        user_id = jdata.get("userId")
        data = []
        if user_is_admin(user_id):
            data = all_flags
        else:
            data = get_flags(user_id)
        res = {"status": 200, "data": data}
        return (jsonify(res), 200)
    except (KeyError, AttributeError, TypeError):
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
    try:
        if user_exists(jdata["username"], jdata["email"])["id"] != 0:
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
    except (TypeError, KeyError, AttributeError):
        return (jsonify(json_error), 400)


def user_exists(username, email):
    if len(all_users) == 0:
        return {"id": 0}
    for user in all_users:
        if user["email"] == email or user["username"] == username:
            return user
    return {"id": 0}


@app.route("/api/v1/users", methods=["GET"])
def get_user_for_sign_in():
    jdata = request.get_json()
    try:
        return get_user_details(jdata["name"], jdata["password"])
    except (TypeError, KeyError, AttributeError):
        return (jsonify(json_error), 400)


def get_user_details(name, password):
    user_does_not_exist = (jsonify({
        "error": "User does not exist", "status": 404}), 404)
    if len(all_users) == 0:
        return user_does_not_exist
    for user in all_users:
        if (user['username'] == name or
                user["email"] == name) and \
                user["password"] == password:
            return (jsonify({"status": 200, "data": [user]}), 200)
        elif (user["username"] == name or
                user["email"] == name) and \
                user["password"] != password:
            return (jsonify({
                "error": "invalid password", "status": 401}), 401)
    return user_does_not_exist


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
    try:
        new_content = jdata[item]
        if edit_item(new_content, item, flag_id):
            res = {
                "data": [{
                    "id": int(flag_id),
                    "message": "Updated red-flag record's {}".format(item)
                }], "status": 200}
            return (jsonify(res), 200)
        return (jsonify(no_flag_found), 404)
    except (TypeError, KeyError, AttributeError):
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
