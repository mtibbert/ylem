import unittest

from temporencUtils.temporencUtils import TemporencUtils
from temporencUtils.types.baseType import BaseType


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
        actual = obj.as_json()
        expected = '{"100011110111111111111111": {"bytes": "3", ' + \
                   '"moment": "1983-??-??", "d": {}, "hex": "8F7FFF", ' + \
                   '"type_tag": "100", "z": "None", "type": "D", "s": {}, ' + \
                   '"t": {}}}'  # Old template
        self.assertEqual(actual, expected)

    def test_as_json_case_7_fix(self):
        obj = BaseTypeTest.base_type_obj
        with self.assertRaises(Exception) as context:
            obj.asJson()
        self.assertTrue("BaseType instance has no attribute 'asJson'"
                        in context.exception)


if __name__ == "__main__":
    # noinspection PyUnresolvedReferences
    unittest.main()
