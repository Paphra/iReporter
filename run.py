from flask import Flask, request, Response, url_for, jsonify

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
            "error": "No json object passed"
        }
        return (jsonify(res), 400)
    
def flag_exists(title, comment):
    for flag in all_flags:
        if flag["title"] == title and flag["comment"] == comment:
            return flag["id"]

    return 0

def add_new_flag(data):
    all_flags.append(data)

all_flags = [

]


if __name__ == '__main__':
    app.run()