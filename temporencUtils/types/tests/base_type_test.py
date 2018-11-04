import json
import unittest

from temporencUtils.temporencUtils import TemporencUtils
from temporencUtils.types.baseType import BaseType
from temporencUtils.types.typeUtils import TypeUtils


class BaseTypeTest(unittest.TestCase):

    def setUp(self):

        BaseTypeTest.byte_string = TemporencUtils.packb(
            value=None, type=None, year=1983, month=None,
            day=None, hour=None, minute=None, second=None,
            millisecond=None, microsecond=None, nanosecond=None,
            tz_offset=None)
        BaseTypeTest.base_type_obj = BaseType(BaseTypeTest.byte_string)

    def test_ctor(self):
        expected = BaseTypeTest.byte_string
        actual = BaseTypeTest.base_type_obj._byte_str
        self.assertEqual(actual, expected)

    def test_as_json(self):
        obj = BaseTypeTest.base_type_obj
        byte_str = obj._byte_str
        moment = TemporencUtils.unpackb(byte_str)
        actual = obj.as_json()
        hex = str(TemporencUtils.hexify_byte_str(byte_str))
        expected = {
            str(hex): {
                "type_tag":
                    str(TypeUtils.type_name_2_type_tag(
                        TypeUtils.byte_str_2_type_name(byte_str))),
                "type": str(TypeUtils.byte_str_2_type_name(byte_str)),
                "bytes": str(len(byte_str)),
                "binary": str('{:0b}'.format(int(hex, 16))),
                "moment": str(moment),
                "d": {},
                "s": {},
                "t": {},
                "z": {},
            }}
        self.assertEqual(actual, json.dumps(expected))

    def test_as_json_case_7_fix(self):
        obj = BaseTypeTest.base_type_obj
        with self.assertRaises(Exception) as context:
            obj.asJson()
        self.assertTrue("BaseType instance has no attribute 'asJson'"
                        in context.exception)


if __name__ == "__main__":
    # noinspection PyUnresolvedReferences
    unittest.main()
