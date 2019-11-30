from unittest import TestCase

from test_wework.api.department import Department
from test_wework.utils.utils import Utils


class TestDepartment:
    def test_list(self):
        department = Department()
        r = department.list("")
        print(Utils.format(r))
        assert department.list("")["errcode"] == 0
        assert department.list("")["department"][0]["name"] == "皮皮"

    def test_create(self):
        department = Department()
        r = department.creat("testpipi", 1, 10)
        assert r["errcode"] == 0

    def test_delete(self):
        department = Department()
        r = department.delete(3)
        assert r["errcode"] == 0


class TestDepartment(TestCase):
    def test_creat(self):
        self.fail()
