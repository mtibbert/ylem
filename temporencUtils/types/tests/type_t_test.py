import json
import unittest

from temporencUtils.temporencUtils import TemporencUtils
from temporencUtils.types.tests.base_type_test import BaseTypeTest
from temporencUtils.types.typeT import TypeT
from temporencUtils.types.type_utils import TypeUtils


class TypeTTest(BaseTypeTest):

    def setUp(self):
        self.TYPE_T_OBJS = {"type": TypeUtils.TYPE_T["_type_name"], "data": [
            {"byte_str": TemporencUtils.packb(
                value=None, type=None,
                year=None, month=None, day=None,
                hour=18, minute=25, second=12,
                millisecond=None, microsecond=None, nanosecond=None,
                tz_offset=None),
                "expected": {
                    "value": "18:25:12",
                    "binary": {
                        "hour": "10010",
                        "minute": "011001",
                        "second": "001100"
                    }
                }},
            {"byte_str": TemporencUtils.packb(
                value=None, type=None,
                year=None, month=None, day=None,
                hour=18, minute=25, second=None,
                millisecond=None, microsecond=None, nanosecond=None,
                tz_offset=None),
                "expected": {
                    "value": "18:25",
                    "binary": {
                        "hour": "10010",
                        "minute": "011001",
                        "second": "111111"
                    }
                }}
        ]}

    def test_ctor(self):
        for item in self.TYPE_T_OBJS["data"]:
            actual_obj = TypeT(item["byte_str"])
            expected_values = item["expected"]["binary"]
            self.assertEquals(
                actual_obj.binary_hour(), expected_values["hour"],
                msg="Binary hour mis-match")
            self.assertEquals(
                actual_obj.binary_minute(), expected_values["minute"],
                msg="Binary minute mis-match")
            self.assertEquals(
                actual_obj.binary_second(), expected_values["second"],
                msg="Binary second mis-match")
            expected = (expected_values["hour"] +
                        expected_values["minute"] +
                        expected_values["second"])
            self.assertTrue(actual_obj.as_binary().endswith(expected),
                            msg="Binary mis-match")

    def test_as_json(self):
        obj = TypeT(self.TYPE_T_OBJS["data"][0]["byte_str"])
        byte_str = obj._byte_str
        moment = TemporencUtils.unpackb(byte_str)
        actual = obj.as_json()
        expected = {
            "t": {
                "hour": str(moment.hour),
                "minute": str(moment.minute),
                "second": str(moment.second),
                "binary": {
                    "hour": obj.binary_hour(),
                    "minute": obj.binary_minute(),
                    "second": obj.binary_second(),
                }
            }}
        self.assertEqual(actual, json.dumps(expected))

    def test_as_json_verbose(self):
            obj = TypeT(self.TYPE_T_OBJS["data"][0]["byte_str"])
            byte_str = obj._byte_str
            moment = TemporencUtils.unpackb(byte_str)
            actual = json.loads(obj.as_json(verbose=True))
            expected = {
                TemporencUtils.hexify_byte_str(byte_str): {
                    "binary": str(TemporencUtils.byte_str_2_bin_str(byte_str)),
                    "bytes": str(len(byte_str)),
                    "moment": moment.__str__(),
                    "type": str(TypeUtils.byte_str_2_type_name(byte_str)),
                    "type_tag": str(TypeUtils.type_name_2_type_tag(
                        TypeUtils.byte_str_2_type_name(byte_str))),
                    "d": {},
                    "s": {},
                    "t": {
                        "hour": str(moment.hour),
                        "minute": str(moment.minute),
                        "second": str(moment.second),
                        "binary": {
                            "hour": obj.binary_hour(),
                            "minute": obj.binary_minute(),
                            "second": obj.binary_second(),
                        }
                    },
                    "o": {}
                }}
            self.assertEquals(actual, expected)

    def test_as_json_matches_as_json_verbose_mode_false(self):
        obj = TypeT(self.TYPE_T_OBJS["data"][0]["byte_str"])
        self.assertEquals(obj.as_json(), obj.as_json(verbose=False))


if __name__ == "__main__":
    # noinspection PyUnresolvedReferences
    unittest.main()
