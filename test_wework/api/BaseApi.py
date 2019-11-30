from test_wework.utils.utils import Utils
import pprint


class BaseApi:
    printer=pprint.PrettyPrinter(indent=2)
    @classmethod
    def verbose(cls, json_object):
        print(Utils.format(json_object))
         # cls.printer.pprint(json_object)