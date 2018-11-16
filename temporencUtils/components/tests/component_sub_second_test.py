import unittest
from mock import MagicMock

from temporencUtils.components.sub_second_component import SubSecondComponent
from temporencUtils.temporencUtils import TemporencUtils
from temporencUtils.types.type_utils import TypeUtils


class SubSecondComponentTest(unittest.TestCase):
    COMPONENT_S_OBJS = [
        {"type": TypeUtils.TYPE_DTS_MILLI["_type_name"][:3],
         "byte_str": TemporencUtils.packb(
            value=None, type=None,
            year=1983, month=1, day=15,
            hour=18, minute=25, second=12,
            millisecond=123, microsecond=None, nanosecond=None,
            tz_offset=None)}]

    def test_ctor_w_o_subsecond(self):
        # Test no sub-second
        expected = "{not set}"
        obj = TemporencUtils.packb(
            value=None, type="DTS",
            year=1983, month=1, day=15,
            hour=18, minute=25, second=12,
            millisecond=None, microsecond=None, nanosecond=None,
            tz_offset=None)
        ssc = SubSecondComponent(obj)
        actual = ssc._value
        self.assertEquals(expected, actual)

    def test_ctor_w_subsecond(self):
        ss = [123, 123456, 123456789]
        # Test millisecond
        expected = ss[0]
        obj = TemporencUtils.packb(
            value=None, type=None,
            year=1983, month=1, day=15,
            hour=18, minute=25, second=12,
            millisecond=expected, microsecond=None, nanosecond=None,
            tz_offset=None)
        ssc = SubSecondComponent(obj)
        actual = ssc._value
        self.assertEquals(expected, actual)
        # Test microsecond
        expected = ss[1]
        obj = TemporencUtils.packb(
            value=None, type=None,
            year=1983, month=1, day=15,
            hour=18, minute=25, second=12,
            millisecond=None, microsecond=expected, nanosecond=None,
            tz_offset=None)
        ssc = SubSecondComponent(obj)
        actual = ssc._value
        self.assertEquals(expected, actual)
        # Test millisecond
        expected = ss[2]
        obj = TemporencUtils.packb(
            value=None, type=None,
            year=1983, month=1, day=15,
            hour=18, minute=25, second=12,
            millisecond=None, microsecond=None, nanosecond=expected,
            tz_offset=None)
        ssc = SubSecondComponent(obj)
        actual = ssc._value
        self.assertEquals(expected, actual)

    def test_precision(self):
        type_s = SubSecondComponent(
            SubSecondComponentTest.COMPONENT_S_OBJS[0]["byte_str"])
        data = (('0000000000', "00"), ('00000000000000000000', "01"),
                ('000000000000000000000000000000', "10"), ('', "11"))
        for pair in data:
            type_s.as_binary = MagicMock(return_value=pair[0])
            self.assertEqual(type_s.precision_tag(), pair[1])

    def test_precision_name(self):
        type_s = SubSecondComponent(
            SubSecondComponentTest.COMPONENT_S_OBJS[0]["byte_str"])
        data = (("0000000000", "millisecond"),
                ("00000000000000000000", "microsecond"),
                ("000000000000000000000000000000", "nanosecond"),
                ("", "none"))
        for pair in data:
            type_s.as_binary = MagicMock(return_value=pair[0])
            self.assertEqual(type_s.precision_name(), pair[1])

    def test_as_json(self):
        data = [
            {"byte_string": TemporencUtils.packb(
                value=None, type=None, year=None, month=None,
                day=None, hour=None, minute=None, second=None,
                millisecond=123, microsecond=None, nanosecond=None,
                tz_offset=None),
                "expected":
                    '{"s": {' +
                    '"binary": {' +
                    '"nanoseconds": "000000000000000000000001111011", ' +
                    '"milliseconds": "0001111011", ' +
                    '"microseconds": "00000000000001111011"}, ' +
                    '"precision name": "millisecond", "value": "123"}}'}]
        for pair in data:
            actual = SubSecondComponent(pair["byte_string"])
            expected = pair["expected"]
            self.assertEqual(actual.as_json(), expected)

    def test_as_binary_case_7_fix(self):
        obj = SubSecondComponent(
            SubSecondComponentTest.COMPONENT_S_OBJS[0]["byte_str"])
        with self.assertRaises(Exception) as context:
            obj.asBinary()
        self.assertTrue(
            "SubSecondComponent instance has no attribute 'asBinary'"
            in context.exception)


if __name__ == '__main__':
    # noinspection PyUnresolvedReferences
    unittest.main()
