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
                        "message":"Created a red-flag record"
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

all_users = [
    {
        "id": 3324332234,
        "username": "Paphra",
        "isAdmin": False,
        "email": "paphra.me@gmail.com",
        "phoneNumber": "0701822382",
        "firstname": "Epaphradito",
        "lastname": "Lugayavu",
        "othernames": "Permutit",
        "password": "123456789",
        "registered": datetime.date.today().isoformat(),
        "gender": "Male",
        "occupation": "Software Developer",
        "address": "Nalugala, Wakiso, Uganda"
    },
    {
        "id": 2324331223,
        "username": "Jules",
        "isAdmin": False,
        "email": "julius234@gmail.com",
        "phoneNumber": "0793424212",
        "firstname": "Julius",
        "lastname": "Katamba",
        "othernames": "",
        "password": "223456789",
        "registered": datetime.date.today().isoformat(),
        "gender": "Male",
        "occupation": "Farmer",
        "address": "Lwatu, Nakasongola, Uganda"
    },
    {
        "id": 2324332234,
        "username": "RechealK",
        "isAdmin": False,
        "email": "rechealk2018@gmail.com",
        "phoneNumber": "075900123",
        "firstname": "Recheal",
        "lastname": "Atuhaire",
        "othernames": "Kunihira",
        "password": "323456789",
        "registered": datetime.date.today().isoformat(),
        "gender": "Female",
        "occupation": "Business Woman - Salon operator",
        "address": "Lubaga, Kampala, Uganda"
    },
    {
        "id": 2322904328,
        "username": "Government",
        "isAdmin": True,
        "email": "info.security@mia.go.ug",
        "phoneNumber": "07777522214",
        "firstname": "Adolf",
        "lastname": "Mwesigye",
        "othernames": "",
        "password": "987654321",
        "registered": datetime.date.today().isoformat(),
        "gender": "Male",
        "occupation": "Minister for defence",
        "address": "Entebbe, Wakiso, Uganda"
    }
]

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
        if user["id"] == user_id:
            if user["isAdmin"]:
                return True
    return False

if __name__ == '__main__':
    app.run()