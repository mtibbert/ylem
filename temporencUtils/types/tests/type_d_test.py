import json
import unittest

from temporencUtils.temporencUtils import TemporencUtils
from temporencUtils.types.tests.base_type_test import BaseTypeTest
from temporencUtils.types.typeD import TypeD
from temporencUtils.types.typeUtils import TypeUtils


class TypeDTest(BaseTypeTest):

    def setUp(self):
        self.byte_string = TemporencUtils.packb(
            value=None, type=None, year=1983, month=None,
            day=None, hour=None, minute=None, second=None,
            millisecond=None, microsecond=None, nanosecond=None,
            tz_offset=None)
        self.obj = TypeD(self.byte_string)

    def test_ctor(self):
        expected = self.byte_string
        actual = self.obj._byte_str
        self.assertEqual(actual, expected)

    def test_as_json(self):
        moment = TemporencUtils.unpackb(self.byte_string)
        actual = self.obj.as_json()
        expected = {
            "d": {
                "year": str(moment.year),
                "month": str(moment.month),
                "day": str(moment.day),
                "binary": {
                    "year": str(self.obj.binary_year()),
                    "month": str(self.obj.binary_month()),
                    "day": str(self.obj.binary_day())}
            }}
        self.assertEqual(actual, json.dumps(expected))

    def test_as_json_case_7_fix(self):
        with self.assertRaises(Exception) as context:
            self.obj.asJson()
        self.assertTrue("TypeD instance has no attribute 'asJson'"
                        in context.exception)

    def test_as_binary_case_7_fix(self):
        with self.assertRaises(Exception) as context:
            self.obj.asBinary()
        self.assertTrue("TypeD instance has no attribute 'asBinary'"
                        in context.exception)


if __name__ == "__main__":
    # noinspection PyUnresolvedReferences
    unittest.main()
