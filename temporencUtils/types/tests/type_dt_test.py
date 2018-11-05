import json
import unittest

from temporencUtils.temporencUtils import TemporencUtils
from temporencUtils.types.type_dt import TypeDT
from temporencUtils.types.type_utils import TypeUtils


class TypeDTTest(unittest.TestCase):

    def setUp(self):
        self.TYPE_DT_OBJS = {
            "type": TypeUtils.TYPE_DT["_type_name"],
            "data": [
                {"byte_str": TemporencUtils.packb(
                    value=None, type=None,
                    year=1983, month=1, day=15,
                    hour=18, minute=25, second=12,
                    millisecond=None, microsecond=None, nanosecond=None,
                    tz_offset=None),
                    "expected": {
                        "hex": "1EFC1D264C",
                        "moment": "1983-01-15 18:25:12",
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
                            }}}},
                {"byte_str": TemporencUtils.packb(
                    value=None, type=None,
                    year=1983, month=1, day=15,
                    hour=18, minute=25, second=None,
                    millisecond=None, microsecond=None, nanosecond=None,
                    tz_offset=None),
                    "expected": {
                        "hex": "1EFC1D264C",
                        "moment": "1983-01-15 18:25",
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
                            "second": "",
                            "binary": {
                                "hour": "10010",
                                "minute": "011001",
                                "second": "111111",
                            }}}}, ]}
        self.byte_string = self.TYPE_DT_OBJS["data"][0]["byte_str"]
        self.obj = TypeDT(self.byte_string)
        pass

    def test_ctor(self):
        for item in self.TYPE_DT_OBJS["data"]:
            expected = item["byte_str"]
            obj = TypeDT(expected)
            actual = obj._byte_str
            self.assertEqual(actual, expected)
            print obj.as_binary()

    def test_as_binary(self):
        actual = self.obj.as_binary()
        expected = TemporencUtils.byte_str_2_bin_str(self.obj._byte_str)
        self.assertEquals(actual, expected)

    def test_as_json(self):
        moment = TemporencUtils.unpackb(self.byte_string)
        actual = TypeDT(self.byte_string)
        d = json.loads(actual._type_d.as_json()),
        t = json.loads(actual._type_t.as_json())
        expected = {TemporencUtils.hexify_byte_str(actual._byte_str): {
            "moment": moment.__str__(),
            "bytes": str(len(actual._byte_str)),
            "type": str(TypeUtils.byte_str_2_type_name(actual._byte_str)),
            "type_tag": str(TypeUtils.type_name_2_type_tag(
                TypeUtils.byte_str_2_type_name(actual._byte_str))),
            "binary": str(TemporencUtils.byte_str_2_bin_str(actual._byte_str)),
            "d": d[0]["d"],
            "t": t["t"]
        }}
        self.assertEqual(actual.as_json(), json.dumps(expected))


if __name__ == "__main__":
    # noinspection PyUnresolvedReferences
    unittest.main()
