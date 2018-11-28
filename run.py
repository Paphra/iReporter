from flask import Flask, request, Response, url_for, jsonify
import datetime
import json

app = Flask(__name__, template_folder='/UI/', static_folder='/UI/assets/')

@app.route("/api/v1/red-flags", methods=['POST'])
def post_red_flag():

    try:
        data = request.get_json()
        title = data.get("title")
        comment = data.get("comment")

        local_id = 0

        if len(all_flags) > 0:
            local_id = flag_exists(title, comment)

        if local_id != 0:
            res = {
                "status": 200,
                "data": [
                    {
                        "id": local_id,
                        "message": "Flag Already reported!"
                    }
                ]
            }
            return (jsonify(res), 200)
        else:
            add_new_flag(data)
            res = {
                "status": 201,
                "data": [
                    {
                        "id": data.get("id"),
                        "message":"Created red-flag record"
                    }
                ]
            }
            return (jsonify(res), 201)
    except:
        res = {
            "status": 400,
            "error": "json object error"
        }
        return (jsonify(res), 400)
    
def flag_exists(title, comment):
    for flag in all_flags:
        if flag["title"] == title and flag["comment"] == comment:
            return flag["id"]

    return 0

def add_new_flag(data):
    all_flags.append(data)

all_flags = []

all_users = []

@app.route("/api/v1/red-flags", methods=["GET"])
def get_all_flags():
    try:
        json_data = request.get_json()
        user_id = json_data.get("userId")
        data = get_flags(user_id)
        res = {
            "status": 200,
            "data": data
        }

        return (jsonify(res), 200)
    except:
        res = {
            "status": 400,
            "error": "json object error"
        }

        return (jsonify(res), 400)

def get_flags(user_id):
    if user_is_admin(user_id):
        return all_flags
    else:

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
    try:
        json_data = request.get_json()
        uname = json_data['username']
        email = json_data['email']

        if user_exists(uname, email):
            res = {
                "status": 200,
                "data": [{
                    "id": json_data["id"],
                    "message": "User Already Exists"
                }]
            }
            return (jsonify(res), 200)
        
        add_user(json_data)

        msg = "New User Added!"
        if json_data["isAdmin"]:
            msg = "New Admin Added!"
        res = {
            "status": 201,
            "data": [{
                "id": json_data['id'],
                "message": msg
            }]
        }

        return (jsonify(res), 201)
    except:
        res = {
            "status": 400,
            "error": "json object error"
        }

        return (jsonify(res), 400)

def user_exists(username, email):
    if len(all_users) == 0:
        return False

    for user in all_users:
        if user['username'] == username or user['email'] == email:
            return True
    
    return False

@app.route("/api/v1/users", methods=["GET"])
def get_user_given_username_or_email():
    try:
        json_data = request.get_json()
        username = json_data["username"]
        email = json_data["email"]

        data = get_user_details(username, email)
        res = {
            "status": 200,
            "data": [data]
        }

        return (jsonify(res), 200)

    except:
        res = {
            "status":400,
            "error":"json object error"
        }
        return (jsonify(res), 400)

def get_user_details(username, email):
    if len(all_users) == 0:
        return {"id":0, "message":"User does not exist"}

    for user in all_users:
        if user['username'] == username or user["email"] == email:
            return user

    return {"id":0, "message":"User does not exist"}


def add_user(json_data):
    all_users.append(json_data)


@app.route("/api/v1/red-flags/<flag_id>")
def get_specific_flag(flag_id):

    flag = get_flag(flag_id)
    if flag == None:
        res = {
            "status": 200,
            "data": []
        }
    else:
        res = {
            "status": 200,
            "data": [flag]
        }

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
                "message": "red-flag has been deleted"
            }]
        }
        return (jsonify(res), 200)
    else:
        res = {
            "status": 404,
            "error": "the flag doesn't exist"
        }
        return (jsonify(res), 404)

def delete_flag(flag_id):
    for flag in all_flags:
        if flag['id'] == int(flag_id):
            all_flags.remove(flag)
            return True
    
    return False

@app.route("/api/v1/red-flags/<red_flag_id>/location", methods=["PATCH"])
def edit_red_flag_location(red_flag_id):
    try:
        j_data = request.get_json()
        new_loc = j_data["location"]
        if edit_location(new_loc, red_flag_id):
            res = {
                "data": [{
                    "id": int(red_flag_id),
                    "message": "Updated red-flag record's location"
                }],
                "status":200
            }
            return (jsonify(res), 200)
        res = {
            "error": "No red flag found",
            "status":404
        }
        return (jsonify(res), 404)
    except:
        res = {
            "error": "json object error",
            "status": 400
        }
        return (jsonify(res), 400)
        
def edit_location(new_loc, flag_id):
    for flag in all_flags:
        if flag["id"] == int(flag_id):
            flag['loaction'] = new_loc
            return True
    
    return False


@app.route("/api/v1/red-flags/<red_flag_id>/comment", methods=["PATCH"])
def edit_red_flag_comment(red_flag_id):
    try:
        j_data = request.get_json()
        new_loc = j_data["comment"]
        if edit_location(new_loc, red_flag_id):
            res = {
                "data": [{
                    "id": int(red_flag_id),
                    "message": "Updated red-flag record's comment"
                }],
                "status": 200
            }
            return (jsonify(res), 200)
        res = {
            "error": "No red flag found",
            "status": 404
        }
        return (jsonify(res), 404)
    except:
        res = {
            "error": "json object error",
            "status": 400
        }
        return (jsonify(res), 400)


def edit_comment(new_comm, flag_id):
    for flag in all_flags:
        if flag["id"] == int(flag_id):
            flag['comment'] = new_comm
            return True

    return False


if __name__ == '__main__':
    app.run()
