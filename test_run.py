
import unittest as ut
import datetime

from flask import jsonify, request, Response

from run import app


class RunTestCase(ut.TestCase):

    def setUp(self):
        self.flag_record_red = {
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
            "otherFiles": ["file1", "file2"]}
        self.flag_record_inter = {
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
            "otherFiles": ["file1", "file2"]}
        self.flag_record_under_inv = {
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
            "otherFiles": ["file1", "file2"]}
        self.flag_record_not_for_user = {
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
            "otherFiles": ["file1", "file2"]}
        self.flag_record_resolved_not_for_user = {
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
            "otherFiles": ["file1", "file2"]}

        self.c_rf = "Created red-flag record"
        self.successful_create1 = {
            "data": [{"id": 23219, "message": self.c_rf}], "status": 201}
        self.successful_create2 = {
            "data": [{"id": 23210, "message": self.c_rf}], "status": 201}
        self.successful_create3 = {
            "data": [{"id": 23212, "message": self.c_rf}], "status": 201}
        self.successful_create4 = {
            "data": [{"id": 23239, "message": self.c_rf}], "status": 201}
        self.successful_create5 = {
            "data": [{"id": 23230, "message": self.c_rf}], "status": 201}

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
            "address": "Nalugala, Wakiso, Uganda"}
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
            "address": "Gaba, Kampala, Uganda"}
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
            "address": "Kisubi, Wakiso, Uganda"}
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
            "address": "Entebbe, Wakiso, Uganda"}

        self.existing_user_name = {
            "username": 'Paphra', "email": "ppaapp@gmail.com"}
        self.abscent_user_name = {
            "username": "Lamwaka", "email": "lamwa@yahoo.com"}
        self.existing_email = {
            "email": 'paphra.me@gmail.com', "username": "Paparo"}
        self.abscent_email = {
            "email": "marian256@yahoo.com", "username": "Mariana"}

        self.flag_id = 23219
        self.flag_id_abscent = 23244

        self.new_location = "23.1232 100.0938"
        self.new_comment = "There is a snake in the garden"
        self.new_title = "There is a snake in the garden"
        self.new_type = "Red-Flag"
        self.new_status = "Resolved"

        self.json_error = {"error": "json object error", "status": 400}
        self.no_flag_found = {"error": "No red flag found", "status": 404}

        self.context = app.test_client()

    def test_create_red_flag_record_data(self):
        with self.context as a:
            rv1 = a.post("/api/v1/red-flags", json=self.flag_record_red)
            rv2 = a.post("/api/v1/red-flags", json=self.flag_record_inter)
            rv3 = a.post("/api/v1/red-flags", json=self.flag_record_under_inv)
            rv4 = a.post(
                "/api/v1/red-flags", json=self.flag_record_not_for_user)
            rv5 = a.post(
                "/api/v1/red-flags",
                json=self.flag_record_resolved_not_for_user)
            assert Response.get_json(rv1) == self.successful_create1
            assert Response.get_json(rv2) == self.successful_create2
            assert Response.get_json(rv3) == self.successful_create3
            assert Response.get_json(rv4) == self.successful_create4
            assert Response.get_json(rv5) == self.successful_create5

    def test_create_red_flag_record_data_repeat(self):
        with self.context as b:
            rv1 = b.post("/api/v1/red-flags", json=self.flag_record_red)
            assert Response.get_json(rv1) == {
                "data": [{"id": 23219, "message": "Flag Already reported!"}],
                "status": 200}

    def test_create_red_flag_record_no_data(self):
        with self.context as c:
            rv1 = c.post("/api/v1/red-flags", json=None)
            assert Response.get_json(rv1) == self.json_error

    def test_add_user_with_json_object(self):
        with self.context as d:
            rv1 = d.post("/api/v1/users", json=self.new_user1)
            rv2 = d.post("/api/v1/users", json=self.new_user_admin)
            assert Response.get_json(rv1) == {
                "data": [{
                    "id": self.new_user1['id'],
                    "message": "New User Added!"}], "status": 201}
            assert Response.get_json(rv2) == {
                "data": [{
                    "id": self.new_user_admin['id'],
                    "message": "New Admin Added!"}], "status": 201}

    def test_add_user_no_json(self):
        with self.context as e:
            rv1 = e.post("/api/v1/users")
            assert Response.get_json(rv1) == self.json_error

    def test_add_users_repeat(self):
        with self.context as f:
            rv1 = f.post(
                "/api/v1/users", json=self.new_user1_repeat_email)
            rv2 = f.post("/api/v1/users", json=self.new_user1_repeat_username)
            rv3 = f.post("/api/v1/users", json=self.new_user1)
            assert Response.get_json(rv1) == {
                "data": [{
                    'id': self.new_user1_repeat_email['id'],
                    'message': "User Already Exists"}], "status": 200}
            assert Response.get_json(rv2) == {
                "data": [{
                    'id': self.new_user1_repeat_username['id'],
                    'message': "User Already Exists"}], "status": 200}
            assert Response.get_json(rv3) == {
                "data": [{
                    'id': self.new_user1['id'],
                    'message': "User Already Exists"}], "status": 200}

    def test_get_all_red_flags_ordinary_user(self):
        with self.context as g:
            rv1 = g.get("/api/v1/red-flags", json={"userId": 2324332223})
            rv2 = g.get("/api/v1/red-flags", json={"userId": 2324331223})
            rv3 = g.get("/api/v1/red-flags", json={"userId": 3324332234})
            assert len(Response.get_json(rv1)['data']) == 1
            assert len(Response.get_json(rv2)['data']) == 1
            assert len(Response.get_json(rv3)['data']) == 3

    def test_get_all_red_flags_admin(self):
        with self.context as h:
            rv1 = h.get("/api/v1/red-flags", json={"userId": 2322904328})
            assert len(Response.get_json(rv1)['data']) == 5

    def test_get_all_red_flags_no_json(self):
        with self.context as i:
            rv1 = i.get("/api/v1/red-flags")
            assert Response.get_json(rv1) == self.json_error

    def test_get_user_given_username(self):
        with self.context as j:
            rv1 = j.get("/api/v1/users", json=self.existing_user_name)
            rv2 = j.get("/api/v1/users", json=self.abscent_user_name)
            assert Response.get_json(rv1) == {
                "data": [self.new_user1], "status": 200}
            assert Response.get_json(rv2) == {
                "data": [{
                    "id": 0, "message": "User does not exist"}], "status": 200}

    def test_get_user_given_email(self):
        with self.context as k:
            rv1 = k.get("/api/v1/users", json=self.existing_email)
            rv2 = k.get("/api/v1/users", json=self.abscent_email)
            assert Response.get_json(rv1) == {
                "data": [self.new_user1], "status": 200}
            assert Response.get_json(rv2) == {
                "data": [{
                    "id": 0, "message": "User does not exist"}], "status": 200}

    def test_get_specific_red_flag_given_id(self):
        with self.context as l:
            rv1 = l.get("/api/v1/red-flags/{}".format(str(self.flag_id)))
            rv2 = l.get("/api/v1/red-flags/{}".format(
                str(self.flag_id_abscent)))
            assert Response.get_json(rv1)["data"] == [self.flag_record_red]
            assert Response.get_json(rv2)["data"] == []

    def test_red_flag_deletion(self):
        with self.context as m:
            rv1 = m.delete("/api/v1/red-flags/{}".format(str(self.flag_id)))
            rv2 = m.delete("/api/v1/red-flags/{}".format(
                str(self.flag_id_abscent)))
            assert Response.get_json(rv1) == {
                "data": [{
                    "id": self.flag_id,
                    "message": "red-flag has been deleted"}], "status": 200}
            assert Response.get_json(rv2) == self.no_flag_found

    def test_red_flag_change_location(self):
        with self.context as n:
            self.edit_test_all(n, "location", self.new_location)

    def test_red_flag_change_comment(self):
        with self.context as o:
            self.edit_test_all(o, "comment", self.new_comment)

    def test_red_flag_change_title(self):
        with self.context as p:
            self.edit_test_all(p, "type", self.new_title)

    def test_red_flag_change_type(self):
        with self.context as q:
            self.edit_test_all(q, "type", self.new_type)

    def test_red_flag_change_status(self):
        with self.context as r:
            self.edit_test_all(r, "status", self.new_status)

    def edit_test_all(self, ctxt, item, new_cont):
        rv1 = ctxt.patch(
            "/api/v1/red-flags/{0}/{1}".format(self.flag_id, item),
            json={item: new_cont})
        rv2 = ctxt.patch(
            "/api/v1/red-flags/{0}/{1}".format(self.flag_id_abscent, item),
            json={item: new_cont})
        assert Response.get_json(rv1) == {
            "data": [{
                "id": self.flag_id,
                "message": "Updated red-flag record's {0}".format(item)}],
            "status": 200}
        assert Response.get_json(rv2) == self.no_flag_found

    def test_user_signin(self):
        pass

    def tearDown(self):
        del self.context

if __name__ == '__main__':
    ut.main()
