
import unittest as ut
import datetime

from flask import jsonify, request, Response

from ..v1 import app


class ApiTestCase2(ut.TestCase):

    def setUp(self):

        self.flag_id_2 = 23210
        self.flag_id_2_abscent = 23244

        self.new_location = "23.1232 100.0938"
        self.new_comment = "There is a snake in the garden"
        self.new_title = "There is a snake in the garden"
        self.new_type = "Red-Flag"
        self.new_status = "Resolved"

        self.json_error = {"error": "json object error", "status": 400}
        self.no_flag_found = {"error": "No red flag found", "status": 404}

        self.context = app.app.test_client()

    def test_red_flag_change_location(self):
        self.edit_test_all("location", self.new_location)

    def test_red_flag_change_comment(self):
        self.edit_test_all("comment", self.new_comment)

    def test_red_flag_change_title(self):
        self.edit_test_all("type", self.new_title)

    def test_red_flag_change_type(self):
        self.edit_test_all("type", self.new_type)

    def test_red_flag_change_status(self):
        self.edit_test_all("status", self.new_status)

    def edit_test_all(self, item, new_cont):
        with self.context as ctxt:
            rv1 = ctxt.patch(
                "/api/v1/red-flags/{0}/{1}".format(self.flag_id_2, item),
                json={item: new_cont})
            rv2 = ctxt.patch(
                "/api/v1/red-flags/{0}/{1}".format(
                    self.flag_id_2_abscent, item),
                json={item: new_cont})
            assert Response.get_json(rv1) == {
                "data": [{
                    "id": self.flag_id_2,
                    "message": "Updated red-flag record's {0}".format(item)}],
                "status": 200}
            assert Response.get_json(rv2) == self.no_flag_found

    def test_user_signin(self):
        pass
