import json
import unittest

from temporencUtils.temporencUtils import TemporencUtils
from temporencUtils.types.type_dts import TypeDTS
from temporencUtils.types.type_utils import TypeUtils


class TypeDTSTest(unittest.TestCase):

    def setUp(self):
        self.TYPE_DTS_OBJS = {
            TypeUtils.VALID_PRECISION_NAMES[0]: {
                "data": [
                    {"byte_str": TemporencUtils.packb(
                    value=None, type="DTS",
                    year=1983, month=1, day=15,
                    hour=18, minute=25, second=12,
                    millisecond=123, microsecond=None, nanosecond=None,
                    tz_offset=None),
                    "expected": {
                        "hex": "47BF07499307B0",
                        "moment": "1983-01-15 18:25:12.123",
                        "binary": "01" +                     #  2 - Type tag
                                  "00" +                     #  2 - Precision
                                  "011110111111000001110" +  # 21 - Date
                                  "10010011001001100" +      # 17 - Time
                                  "0001111011" +             # 10 - Sub-second
                                  "0000",                    #  4 - Padding
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
                        "s": {
                            "precision": "millisecond",
                            "binary": "0001111011",
                            "subseconds": "123"
                        }
                    }},
                ]},
            TypeUtils.VALID_PRECISION_NAMES[1]: {
                "data": [
                    {"byte_str": TemporencUtils.packb(
                    value=None, type=None,
                    year=1983, month=1, day=15,
                    hour=18, minute=25, second=12,
                    millisecond=None, microsecond=123456, nanosecond=None,
                    tz_offset=None),
                    "expected": {
                        "hex": "57BF074993078900",
                        "moment": "1983-01-15 18:25:12.123456",
                        "binary": "01" +                     #  2 - Type tag
                                  "01" +                     #  2 - Precision
                                  "011110111111000001110" +  # 21 - Date
                                  "10010011001001100" +      # 17 - Time
                                  "0001111000100100000000",  # 22 - Sub-second
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
                        "s": {
                            "precision": "microsecond",
                            "binary": "0001111011",
                            "subseconds": "123456"
                        }
                    }},
                ]},
            TypeUtils.VALID_PRECISION_NAMES[2]: {
                "data": [
                    {"byte_str": TemporencUtils.packb(
                    value=None, type=None,
                    year=1983, month=1, day=15,
                    hour=18, minute=25, second=12,
                    millisecond=None, microsecond=None, nanosecond=123456789,
                    tz_offset=None),
                    "expected": {
                        "hex": "67BF074993075BCD15",
                        "moment": "1983-01-15 18:25:12.123456789",
                        "binary": "01" +                     #  2 - Type tag
                                  "10" +                     #  2 - Precision
                                  "011110111111000001110" +  # 21 - Date
                                  "10010011001001100" +      # 17 - Time
                                  "000111010110111" +        # 10 - Sub-second
                                  "100110100010101",
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
                        "s": {
                            "precision": "nanosecond",
                            "binary": "000111010110111100110100010101",
                            "subseconds": "123456789"
                        }
                    }},
                ]},
            TypeUtils.VALID_PRECISION_NAMES[3]: {
                "data": [
                    {"byte_str": TemporencUtils.packb(
                    value=None, type="DTS",
                    year=1983, month=1, day=15,
                    hour=18, minute=25, second=12,
                    millisecond=None, microsecond=None, nanosecond=None,
                    tz_offset=None),
                    "expected": {
                        "hex": "77BF07499300",
                        "moment": "1983-01-15 18:25:12",
                        "binary": "01" +                     #  2 - Type tag
                                  "11" +                     #  2 - Precision
                                  "011110111111000001110" +  # 21 - Date
                                  "10010011001001100" +      # 17 - Time
                                  "000000",                  #  6 - Sub-second
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
                        "s": {
                            "precision": "none",
                            "binary": "000000",
                            "subseconds": "None"
                        }
                    }}
                ], }
        }

    def test_ctor_byte_str(self):
        test_data = TypeUtils.VALID_PRECISION_NAMES
        for ss_name in test_data:
            hive = self.TYPE_DTS_OBJS[ss_name]
            i = 0
            while i < len(hive["data"]):
                expected = hive["data"][i]["byte_str"]
                i += 1
                obj = TypeDTS(expected)
                actual = obj._byte_str
                self.assertEqual(expected, actual)

    def test_as_binary(self):
        test_data = TypeUtils.VALID_PRECISION_NAMES
        for ss_name in test_data:
            hive = self.TYPE_DTS_OBJS[ss_name]
            i = 0
            while i < len(hive["data"]):
                byte_string = hive["data"][i]["byte_str"]
                obj = TypeDTS(byte_string)
                expected = TemporencUtils.byte_str_2_bin_str(byte_string)
                actual = obj.as_binary()
                self.assertEqual(expected, actual)
                i += 1

    def test_as_json(self):
        test_data = TypeUtils.VALID_PRECISION_NAMES
        for ss_name in test_data:
            hive = self.TYPE_DTS_OBJS[ss_name]
            i = 0
            while i < len(hive["data"]):
                byte_string = hive["data"][i]["byte_str"]
                moment = TemporencUtils.unpackb(byte_string)
                test_data = hive["data"][i]["expected"]
                i += 1
                actual = TypeDTS(byte_string)
                template_hex = TemporencUtils.hexify_byte_str(actual._byte_str)
                expected = \
                    {template_hex:
                         {"binary": test_data["binary"],
                          "s": {},
                          "bytes": str(len(actual._byte_str)),
                          "o": {},
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
                # Load s info
                obj = json.loads(actual._component_s.as_json())
                expected[template_hex]["s"] = obj["s"]
                actual_obj = json.loads(actual.as_json())
                key = expected.keys()[0]
                # Check hex values match
                self.assertEqual(key, actual_obj.keys()[0])
                keys = expected[key].keys()
                # Check same number of attributes
                self.assertEqual(len(keys), len(actual_obj[key].keys()))
                # Check each attribute
                for attr in keys:
                    self.assertIn(
                        attr, actual_obj[key].keys(),
                        "The key '{attr}' is not in the key list of ({keys})"
                            .format(attr=attr,
                                    keys=", ".join(actual_obj[key].keys())))
                    self.assertEqual(expected[key][attr], actual_obj[key][attr],
                                     "Where key is '{key}'".format(key=key))
