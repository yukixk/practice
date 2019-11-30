from unittest import TestCase

import requests

from test_wework.utils.utils import Utils


class TestUtils(TestCase):
    def test_format(self):
        print(Utils.format({"a": 1, "b": {"c": "xxx"}}))
    def test_fromat_json(self):
        r = requests.get("https://testerhome.com/api/v3/topics.json?limit=2").json()
        print(Utils.format(r))
