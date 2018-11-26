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
            "createdBy": 2324332234,
            "location": "0.3421, 32.2231",
            "status": "Draft",
            "Images": ["image1", "image2"],
            "Videos": ["video1", "video2"],
            "otherFiles": ["file1","file2"]
        }

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

            assert Response.get_data(rv) == b'{"data":[{"id":23219,"message":"Created a red-flag record"}],"status":201}\n'

    # test repeated data
    def test_create_red_flag_record_data_repeat(self):
        with app.test_client() as d:
            rv2 = d.post("/api/v1/red-flags", json=self.test_new_flag_record_data)

            assert Response.get_data(rv2) == b'{"data":[{"id":23219,"message":"Flag Already reported!"}],"status":200}\n'

    def test_create_red_flag_record_no_data(self):
        with app.test_client() as d:
            rv2 = d.post("/api/v1/red-flags", json=None)

            assert Response.get_data(rv2) == b'{"error":"No json object passed","status":400}\n'


if __name__ == '__main__':
    ut.main()