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
    

if __name__ == '__main__':
    ut.main()