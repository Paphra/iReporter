
from flask import Flask, request, Response, url_for, jsonify
from ..v1.models import flags, users

app = Flask(__name__)

json_error = {"status": 400, "error": "json object error"}
no_flag_found = {"error": "No red flag found", "status": 404}

all_flags = flags.all_flags
all_users = users.all_users
fmodel = flags.FlagsModel()
umodel = users.UsersModel()


@app.route("/api/v1/red-flags", methods=['POST'])
def post_red_flag():
    data = request.get_json()
    try:
        flag_is_there = False
        if len(all_flags) > 0:
            flag_is_there = fmodel.flag_exists(data.get("title"),
                                               data.get("comment"))
        if flag_is_there:
            res = {
                "status": 200,
                "data": [{"id": 0, "message": "Flag Already reported!"}]}
            return (jsonify(res), 200)
        fmodel.add_new_flag(data)
        res = {
            "status": 201,
            "data": [{
                "id": data.get("id"),
                "message": "Created red-flag record"}]}
        return (jsonify(res), 201)
    except (TypeError, KeyError, AttributeError):
        return (jsonify(json_error), 400)


@app.route("/api/v1/red-flags", methods=["GET"])
def get_all_flags():
    jdata = request.get_json()
    try:
        user_id = jdata.get("userId")
        data = []
        if umodel.is_admin(user_id):
            data = all_flags
        else:
            data = fmodel.get_user_flags(user_id)
        res = {"status": 200, "data": data}
        return (jsonify(res), 200)
    except (KeyError, AttributeError, TypeError):
        return (jsonify(json_error), 400)


@app.route("/api/v1/users", methods=["POST"])
def add_new_user():
    jdata = request.get_json()
    try:
        if umodel.user_exists(jdata["username"], jdata["email"])["id"] != 0:
            res = {
                "status": 200,
                "data": [{
                    "id": jdata["id"],
                    "message": "User Already Exists"}]}
            return (jsonify(res), 200)
        umodel.add_user(jdata)
        msg = "New User Added!"
        if jdata["isAdmin"]:
            msg = "New Admin Added!"
        res = {
            "status": 201,
            "data": [{"id": jdata['id'], "message": msg}]}
        return (jsonify(res), 201)
    except (TypeError, KeyError, AttributeError):
        return (jsonify(json_error), 400)


@app.route("/api/v1/users", methods=["GET"])
def get_user_for_sign_in():
    jdata = request.get_json()
    try:
        return umodel.get_details(jdata["name"], jdata["password"])
    except (TypeError, KeyError, AttributeError):
        return (jsonify(json_error), 400)


@app.route("/api/v1/red-flags/<flag_id>")
def get_specific_flag(flag_id):
    flag = fmodel.get_flag(flag_id)
    if flag is not None:
        res = {"status": 200, "data": [flag]}
    else:
        res = {"status": 200, "data": []}
    return (jsonify(res), 200)


@app.route("/api/v1/red-flags/<red_flag_id>", methods=["DELETE"])
def delete_red_flag(red_flag_id):
    if fmodel.delete_flag(red_flag_id):
        res = {
            "status": 200,
            "data": [{
                "id": int(red_flag_id),
                "message": "red-flag has been deleted"}]}
        return (jsonify(res), 200)
    else:
        return (jsonify(no_flag_found), 404)


@app.route("/api/v1/red-flags/<red_flag_id>/location", methods=["PATCH"])
def edit_red_flag_location(red_flag_id):
    return fmodel.edit(red_flag_id, "location", request)


@app.route("/api/v1/red-flags/<red_flag_id>/comment", methods=["PATCH"])
def edit_red_flag_comment(red_flag_id):
    return fmodel.edit(red_flag_id, "comment", request)


@app.route("/api/v1/red-flags/<red_flag_id>/title", methods=["PATCH"])
def edit_red_flag_title(red_flag_id):
    return fmodel.edit(red_flag_id, "title", request)


@app.route("/api/v1/red-flags/<red_flag_id>/type", methods=["PATCH"])
def edit_red_flag_type(red_flag_id):
    return fmodel.edit(red_flag_id, "type", request)


@app.route("/api/v1/red-flags/<red_flag_id>/status", methods=["PATCH"])
def edit_red_flag_status(red_flag_id):
    return fmodel.edit(red_flag_id, "status", request)


if __name__ == '__main__':
    app.run()
