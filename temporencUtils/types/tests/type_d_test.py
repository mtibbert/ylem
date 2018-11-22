import json
import unittest

from temporencUtils.temporencUtils import TemporencUtils
from temporencUtils.types.tests.base_type_test import BaseTypeTest
from temporencUtils.types.typeD import TypeD


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
        actual = json.loads(self.obj.as_json())
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
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    # noinspection PyUnresolvedReferences
    unittest.main()
