import json
import unittest
from temporencUtils.types.tests.type_dt_test import TypeDTTest

from temporencUtils.temporencUtils import TemporencUtils
from temporencUtils.types.type_dt import TypeDT
from temporencUtils.types.type_dtz import TypeDTZ
from temporencUtils.types.type_utils import TypeUtils


class TypeDTZTest(TypeDTTest):

    def setUp(self):
        # self.TYPE_DTZ_OBJS = super(TypeDTTest, self).TYPE_DT_OBJS
        self.TYPE_DTZ_OBJS = {
            "type": TypeUtils.TYPE_DT["_type_name"], "data": [
                {"byte_str": TemporencUtils.packb(
                    value=None, type=None,
                    year=1983, month=1, day=15,
                    hour=18, minute=25, second=12,
                    millisecond=None, microsecond=None, nanosecond=None,
                    tz_offset=0),
                    "expected": {
                        "hex": "CF7E0E8B2640",
                        "moment": "1983-01-15 18:25:12",
                        "binary": "110" +                    #  3 - Type tag
                                  "011110111111000001110" +  # 21 - Date
                                  "10010011001001100" +      # 17 - Time
                                  "1000000",                 #  7 - TZ Offset
                        "d": {
                            "year": "1983",
                            "month": "1",
                            "day": "15",
                            "binary": {
                                "year": "001100",
                                "month": "0000",
                                "day": "01110"}
                        },
                        "t": {
                            "hour": "18",
                            "minute": "25",
                            "second": "12",
                            "binary": {
                                "hour": "10010",
                                "minute": "011001",
                                "second": "001100",
                            }},
                        "z": {
                            "binary": "1000000",
                            "decimal": "64",
                            "increments": "0",
                            "minutes": "0"
                        }
                    }},
                {"byte_str": TemporencUtils.packb(
                    value=None, type=None,
                    year=1983, month=1, day=15,
                    hour=18, minute=25, second=12,
                    millisecond=None, microsecond=None, nanosecond=None,
                    tz_offset=60),
                    "expected": {
                        "hex": "CF7E0E8B2640",
                        "moment": "1983-01-15 18:25:12",
                        "binary": "110" +                    #  3 - Type tag
                                  "011110111111000001110" +  # 21 - Date
                                  "10010011001001100" +      # 17 - Time
                                  "1000100",                 #  7 - TZ Offset
                        "d": {
                            "year": "1983",
                            "month": "1",
                            "day": "15",
                            "binary": {
                                "year": "001100",
                                "month": "0000",
                                "day": "01110"}
                        },
                        "t": {
                            "hour": "18",
                            "minute": "25",
                            "second": "12",
                            "binary": {
                                "hour": "10010",
                                "minute": "011001",
                                "second": "001100",
                            }},
                        "z": {
                            "binary": "1000100",
                            "decimal": "68",
                            "increments": "4",
                            "minutes": "60"
                        }
                    }},
                {"byte_str": TemporencUtils.packb(
                    value=None, type=None,
                    year=1983, month=1, day=15,
                    hour=18, minute=25, second=12,
                    millisecond=None, microsecond=None, nanosecond=None,
                    tz_offset=-360),
                    "expected": {
                        "hex": "CF7E0E8B2640",
                        "moment": "1983-01-15 18:25:12",
                        "binary": "110" +                    #  3 - Type tag
                                  "011110111111000001110" +  # 21 - Date
                                  "10010011001001100" +      # 17 - Time
                                  "0101000",                 #  7 - TZ Offset
                        "d": {
                            "year": "1983",
                            "month": "1",
                            "day": "15",
                            "binary": {
                                "year": "001100",
                                "month": "0000",
                                "day": "01110"}
                        },
                        "t": {
                            "hour": "18",
                            "minute": "25",
                            "second": "12",
                            "binary": {
                                "hour": "10010",
                                "minute": "011001",
                                "second": "001100",
                            }},
                        "z": {
                            "binary": "0101000",
                            "decimal": "40",
                            "increments": "-24",
                            "minutes": "-360"
                        }
                    }},
        ]}
        self.byte_string = self.TYPE_DTZ_OBJS["data"][0]["byte_str"]
        self.obj = TypeDT(self.byte_string)

    def test_ctor(self):
        for item in self.TYPE_DTZ_OBJS["data"]:
            expected = item["byte_str"]
            obj = TypeDTZ(expected)
            actual = obj._byte_str
            self.assertEqual(actual, expected)
            self.assertEquals(TemporencUtils.byte_str_2_bin_str(actual),
                              item["expected"]["binary"])

    def test_as_binary(self):
        for item in self.TYPE_DTZ_OBJS["data"]:
            obj = TypeDTZ(item["byte_str"])
            actual = obj.as_binary()
            expected = TemporencUtils.byte_str_2_bin_str(item["byte_str"])
            self.assertEquals("" + expected, actual)

    def test_as_json(self):
        moment = TemporencUtils.unpackb(self.byte_string)
        actual = TypeDTZ(self.byte_string)
        template_hex = TemporencUtils.hexify_byte_str(actual._byte_str)
        expected = \
            {template_hex:
                 {"binary": TemporencUtils.byte_str_2_bin_str(actual._byte_str),
                  "s": {},
                  "bytes": str(len(actual._byte_str)),
                  "tz_offset": "0",
                  "moment": str(moment),
                  "type_tag": TypeUtils.type_name_2_type_tag(
                      TypeUtils.byte_str_2_type_name(actual._byte_str)),
                  "type": TypeUtils.byte_str_2_type_name(actual._byte_str)}}
        # Load time info
        obj = json.loads(actual._type_t.as_json())
        expected[template_hex]["t"] = obj["t"]
        # Load date info
        obj = json.loads(actual._type_d.as_json())
        expected[template_hex]["d"] = obj["d"]
        # Load tz info
        obj = json.loads(actual._component_tz.as_json())
        expected[template_hex]["z"] = obj["z"]
        actual_obj = json.loads(actual.as_json())
        key = expected.keys()[0]
        # Check hex values match
        self.assertEqual(key, actual_obj.keys()[0])
        keys = expected[key].keys()
        # Check same number of attributes
        self.assertEqual(len(keys), len(actual_obj[key].keys()))
        # Check each attribute
        for attr in keys:
            self.assertIn(attr, actual_obj[key].keys())
            self.assertEqual(expected[key][attr], actual_obj[key][attr])


if __name__ == "__main__":
    # noinspection PyUnresolvedReferences
    unittest.main()
