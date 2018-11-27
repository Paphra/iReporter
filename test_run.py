import unittest as ut
from flask import jsonify, request, Response, url_for
from run import app
import datetime

class RunTestCase(ut.TestCase):

    def setUp(self):

        self.test_new_flag_record_data = {
            "id": 23219,
            "title": "Corruption much",
            "comment": "please, help us. We are dying.",
            "type": "Red-Flag",
            "createdOn": datetime.date.today().isoformat(),
            "createdBy": 3324332234,
            "location": "0.3421, 32.2231",
            "status": "Draft",
            "Images": ["image1", "image2"],
            "Videos": ["video1", "video2"],
            "otherFiles": ["file1","file2"]
        }
        self.test_get_flag_records_inter = {
            "id": 23210,
            "title": "Roads are not okay",
            "comment": "The bridge from kitaga to nyamitobola is down",
            "type": "Intervention",
            "createdOn": datetime.date.today().isoformat(),
            "createdBy": 3324332234,
            "location": "2.4232, 33.2231",
            "status": "Draft",
            "Images": ["image1", "image2"],
            "Videos": ["video1", "video2"],
            "otherFiles": ["file1","file2"]
        }

        self.test_get_flag_records_under_inv = {
            "id": 23212,
            "title": "Thief or the SACCO money",
            "comment": "There is someone stealing our sacco money",
            "type": "Red-Flag",
            "createdOn": datetime.date.today().isoformat(),
            "createdBy": 3324332234,
            "location": "2.4232, 33.2231",
            "status": "Under Investigation",
            "Images": ["image1", "image2"],
            "Videos": ["video1", "video2"],
            "otherFiles": ["file1","file2"]
        }
        self.test_get_flag_records_not_for_user = {
            "id": 23239,
            "title": "Our Village is under siege",
            "comment": "We have corrupt official on ground",
            "type": "Red-Flag",
            "createdOn": datetime.date.today().isoformat(),
            "createdBy": 2324332223,
            "location": "1.4232, 23.2231",
            "status": "Under Investigation",
            "Images": ["image1", "image2"],
            "Videos": ["video1", "video2"],
            "otherFiles": ["file1","file2"]
        }

        self.test_get_flag_records_resolved_not_for_user = {
            "id": 23230,
            "title": "The crops are dying off",
            "comment": "We need some water for irrigations",
            "type": "Red-Flag",
            "createdOn": datetime.date.today().isoformat(),
            "createdBy": 2324331223,
            "location": "3.4232, 30.2231",
            "status": "Resolved",
            "Images": ["image1", "image2"],
            "Videos": ["video1", "video2"],
            "otherFiles": ["file1","file2"]
        }

        self.successful_create = {"data":[{"id":23219,"message":"Created a red-flag record"}],"status":201}
        self.successful_create2 = {"data":[{"id":23210,"message":"Created a red-flag record"}],"status":201}
        self.successful_create3 = {"data":[{"id":23212,"message":"Created a red-flag record"}],"status":201}
        self.successful_create4 = {"data":[{"id":23239,"message":"Created a red-flag record"}],"status":201}
        self.successful_create5 = {"data": [{"id": 23230, "message": "Created a red-flag record"}], "status": 201}
        
        self.new_user1 = {
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
        }
        self.new_user1_repeat_email = {
            "id": 3209932214,
            "username": "Xypindo",
            "isAdmin": False,
            "email": "paphra.me@gmail.com",
            "phoneNumber": "0700928392",
            "firstname": "Martha",
            "lastname": "Nakalyango",
            "othernames": "",
            "password": "923456789",
            "registered": datetime.date.today().isoformat(),
            "gender": "Female",
            "occupation": "Security Guard",
            "address": "Gaba, Kampala, Uganda"
        }
        self.new_user1_repeat_username = {
            "id": 7209932218,
            "username": "Paphra",
            "isAdmin": False,
            "email": "xyz1990@gmail.com",
            "phoneNumber": "0778289201",
            "firstname": "Bemerdine",
            "lastname": "Birengeso",
            "othernames": "Bire",
            "password": "623456789",
            "registered": datetime.date.today().isoformat(),
            "gender": "Male",
            "occupation": "Teacher",
            "address": "Kisubi, Wakiso, Uganda"
        }
        self.new_user2 = {
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
        }
        self.new_user3 = {
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
        }
        self.new_user_admin = {
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

        self.test_user_name_exists = {"username":'Paphra', "email":"ppaapp@gmail.com"}
        self.test_user_name_does_not_exist ={"username":"Lamwaka", "email":"lamwa@yahoo.com"}
        self.test_email_exists = {"email":'paphra.me@gmail.com', "username":"Paparo"}
        self.test_email_does_not_exist = {"email": "marian256@yahoo.com", "username": "Mariana"}
        self.test_all_user_info_exists = {"username":'Paphra', "email":"paphra@gmail.com"}
        


    def tearDown(self):
        pass

    def test_create_red_flag_record_call(self):
        with app.test_request_context("/api/v1/red-flags", method='POST'):

            assert request.method == 'POST'
            assert request.path == '/api/v1/red-flags'
            assert request.get_json() == None

    def test_create_red_flag_record_data(self):
        with app.test_client() as c:
            
            rv = c.post("/api/v1/red-flags", json=self.test_new_flag_record_data)
            rv2 = c.post("/api/v1/red-flags", json=self.test_get_flag_records_inter)
            rv3 = c.post("/api/v1/red-flags", json=self.test_get_flag_records_under_inv)
            rv4 = c.post("/api/v1/red-flags", json=self.test_get_flag_records_not_for_user)
            rv5 = c.post("/api/v1/red-flags", json=self.test_get_flag_records_resolved_not_for_user)

            assert Response.get_json(rv) == self.successful_create
            assert Response.get_json(rv2) == self.successful_create2
            assert Response.get_json(rv3) == self.successful_create3
            assert Response.get_json(rv4) == self.successful_create4
            assert Response.get_json(rv5) == self.successful_create5

    # test repeated data
    def test_create_red_flag_record_data_repeat(self):
        with app.test_client() as d:
            rv2 = d.post("/api/v1/red-flags", json=self.test_new_flag_record_data)

            assert Response.get_json(rv2) == {"data":[{"id":23219,"message":"Flag Already reported!"}],"status":200}

    def test_create_red_flag_record_no_data(self):
        with app.test_client() as d:
            rv2 = d.post("/api/v1/red-flags", json=None)

            assert Response.get_json(rv2) == {"error":"json object error","status":400}

    def test_add_new_user_call(self):
        with app.test_client() as au:
            au.post("/api/v1/users")
            assert request.method == 'POST'
            assert request.path == "/api/v1/users"
            assert request.get_json() == None
            
    def test_add_user_with_json_object(self):
        with app.test_client() as au:
            rv = au.post("/api/v1/users", json=self.new_user1)
            rv2 = au.post("/api/v1/users", json=self.new_user2)
            rv3 = au.post("/api/v1/users", json=self.new_user3)
            rv4 = au.post("/api/v1/users", json=self.new_user_admin)

            assert Response.get_json(rv) == {
                "data": [{"id": self.new_user1['id'], "message": "New User Added!"}], "status":201
            }
            assert Response.get_json(rv2) == {
                "data": [{"id": self.new_user2['id'], "message": "New User Added!"}], "status":201
            }
            assert Response.get_json(rv3) == {
                "data": [{"id": self.new_user3['id'], "message": "New User Added!"}], "status":201
            }
            assert Response.get_json(rv4) == {
                "data": [{"id": self.new_user_admin['id'], "message": "New Admin Added!"}], "status": 201
            }

    def test_add_user_no_json(self):
        with app.test_client() as c:
            rv = c.post("/api/v1/users")
            assert Response.get_json(rv) == {"error": "json object error", "status": 400}

    
    def test_add_users_repeat(self):
        with app.test_client() as au:
            rv = au.post("/api/v1/users", json=self.new_user1_repeat_email)
            assert Response.get_json(rv) == {
                "data": [{'id': self.new_user1_repeat_email['id'], 'message': "User Already Exists"}],
                "status": 200
            }
            rv2 = au.post("/api/v1/users", json=self.new_user1_repeat_username)
            assert Response.get_json(rv2) == {
                "data": [{'id': self.new_user1_repeat_username['id'], 'message': "User Already Exists"}],
                "status": 200
            }
            rv3 = au.post("/api/v1/users", json=self.new_user1) #repeating all values
            assert Response.get_json(rv3) == {
                "data": [{'id': self.new_user1['id'], 'message': "User Already Exists"}],
                "status": 200
            }
            
    def test_get_all_red_flags_call(self):
        with app.test_client() as c:
            rv = c.get("/api/v1/red-flags")
            assert request.method == 'GET'
            assert request.path == "/api/v1/red-flags"
            assert request.get_json() == None

    def test_get_all_red_flags_ordinary_user(self):
        with app.test_client() as c:
            
            rv = c.get("/api/v1/red-flags", json={"userId": 2324332223})
            rv2 = c.get("/api/v1/red-flags", json={"userId": 2324331223})
            rv3 = c.get("/api/v1/red-flags", json={"userId": 3324332234})
            
            assert len(Response.get_json(rv)['data']) == 1
            assert len(Response.get_json(rv2)['data']) == 1
            assert len(Response.get_json(rv3)['data']) == 3

            
    def test_get_all_red_flags_admin(self):
        with app.test_client() as c:
            rv0 = c.get("/api/v1/red-flags", json={"userId": 2322904328})  # passed the admin id
            assert len(Response.get_json(rv0)['data']) == 5
            

    def test_get_all_red_flags_no_json(self):
        with app.test_client() as c:
            rv = c.get("/api/v1/red-flags")
            assert Response.get_json(rv) == {"error": "json object error", "status": 400}

    def test_get_user_call(self):
        with app.test_client() as t:
            rvv = t.get("/api/v1/users")
            assert request.method == 'GET'
            assert request.path == '/api/v1/users'
            assert request.get_json() == None

    def test_get_user_given_username(self):
        with app.test_client() as cc:
            rv = cc.get("/api/v1/users", json=self.test_user_name_exists)
            rv2 = cc.get("/api/v1/users", json=self.test_user_name_does_not_exist)

            assert Response.get_json(rv) == {
                "data": [self.new_user1],
                "status": 200
            }
            assert Response.get_json(rv2) == {"data":[{"id":0, "message":"User does not exist"}], "status":200}

    def test_get_user_given_email(self):
        with app.test_client() as cc:
            rv = cc.get("/api/v1/users", json=self.test_email_exists)
            rv2 = cc.get("/api/v1/users", json=self.test_email_does_not_exist)

            assert Response.get_json(rv) == {
                "data": [self.new_user1],
                "status": 200
            }
            assert Response.get_json(rv2) == {"data":[{"id":0, "message":"User does not exist"}], "status":200}

if __name__ == '__main__':
    ut.main()