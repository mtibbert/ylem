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

    def test_precision(self):
        typeS = SubSecondComponent(SubSecondComponentTest.COMPONENT_S_OBJS[0]["byte_str"])
        data = (('abcdefghij', "00"), ('abcdefghijabcdefghij', "01"),
                ('abcdefghijabcdefghijabcdefghij', "10"), ('', "11"))
        for pair in data:
            typeS.as_binary = MagicMock(return_value=pair[0])
            self.assertEqual(typeS.precision_tag(), pair[1])

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
