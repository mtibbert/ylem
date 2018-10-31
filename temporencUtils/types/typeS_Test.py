import unittest

# from temporencUtils.temporencUtils import TemporencUtils
# from temporencUtils.types.typeUtils import TypeUtils
import mock as mock
from mock import MagicMock

from temporencUtils.temporencUtils import TemporencUtils
from temporencUtils.types.typeS import TypeUtils, TypeS


class TypeSTest(unittest.TestCase):
    COMPONENT_S_OBJS = [
        {"type": TypeUtils.TYPE_DTS_MILLI["_type_name"][:3],
         "byte_str": TemporencUtils.packb(
            value=None, type=None,
            year=1983, month=1, day=15,
            hour=18, minute=25, second=12,
            millisecond=123, microsecond=None, nanosecond=None,
            tz_offset=None)}]
    # TYPE_DTS_MICRO_OBJ = {
    #     "type": TypeUtils.TYPE_DTS_MILLI["_type_name"][:3],
    #     "byte_str": TemporencUtils.packb(
    #         value=None, type=None,
    #         year=1983, month=1, day=15,
    #         hour=18, minute=25, second=12,
    #         millisecond=None, microsecond=123456, nanosecond=None,
    #         tz_offset=None),
    #     "binary": "010101111011111100000111" +
    #               "010010011001001100000111" +
    #               "1000100100000000",
    #     "hex": "57bf074993078900"}
    # TYPE_DTS_NANO_OBJ = {
    #     "type": TypeUtils.TYPE_DTS_MILLI["_type_name"][:3],
    #     "byte_str": TemporencUtils.packb(
    #         value=None, type=None,
    #         year=1983, month=1, day=15,
    #         hour=18, minute=25, second=12,
    #         millisecond=None, microsecond=None, nanosecond=123456789,
    #         tz_offset=None),
    #     "binary": "011001111011111100000111" +
    #               "010010011001001100000111" +
    #               "010110111100110100010101",
    #     "hex": "67bf074993075bcd15"}
    # TYPE_DTS_NONE_OBJ = {
    #     "type": TypeUtils.TYPE_DTS_MILLI["_type_name"][:3],
    #     "byte_str": TemporencUtils.packb(
    #         value=None, type="DTS",
    #         year=1983, month=1, day=15,
    #         hour=18, minute=25, second=12,
    #         millisecond=None, microsecond=None, nanosecond=None,
    #         tz_offset=None),
    #     "binary": "011101111011111100000111010010011001001100000000",
    #     "hex": "77bf07499300"}
    # TYPE_DTSZ_MILLI_OBJ = {
    #     "type": TypeUtils.TYPE_DTSZ_MILLI["_type_name"][:4],
    #     "byte_str": TemporencUtils.packb(
    #         value=None, type=None,
    #         year=1983, month=1, day=15,
    #         hour=18, minute=25, second=12,
    #         millisecond=123, microsecond=None, nanosecond=None,
    #         tz_offset=60),
    #     "binary": "111000111101111110000011" +
    #               "101000101100100110000011" +
    #               "1101110001000000",
    #     "hex": "e3df83a2c983dc40"}
    # TYPE_DTSZ_MICRO_OBJ = {
    #     "type": TypeUtils.TYPE_DTSZ_MILLI["_type_name"][:4],
    #     "byte_str": TemporencUtils.packb(
    #         value=None, type=None,
    #         year=1983, month=1, day=15,
    #         hour=18, minute=25, second=12,
    #         millisecond=None, microsecond=123456, nanosecond=None,
    #         tz_offset=60),
    #     "binary": "111010111101111110000011" +
    #               "101000101100100110000011" +
    #               "110001001000000100010000",
    #     "hex": "ebdf83a2c983c48110"}
    # TYPE_DTSZ_NANO_OBJ = {
    #     "type": TypeUtils.TYPE_DTSZ_MILLI["_type_name"][:4],
    #     "byte_str": TemporencUtils.packb(
    #         value=None, type=None,
    #         year=1983, month=1, day=15,
    #         hour=18, minute=25, second=12,
    #         millisecond=None, microsecond=None, nanosecond=123456789,
    #         tz_offset=60),
    #     "binary": "111100111101111110000011" +
    #               "101000101100100110000011" +
    #               "101011011110011010001010" +
    #               "11000100",
    #     "hex": "f3df83a2c983ad e68ac4"}
    # TYPE_DTSZ_NONE = {
    #     "type": TypeUtils.TYPE_DTSZ_MILLI["_type_name"][:4],
    #     "byte_str": TemporencUtils.packb(
    #         value=None, type="DTSZ",
    #         year=1983, month=1, day=15,
    #         hour=18, minute=25, second=12,
    #         millisecond=None, microsecond=None, nanosecond=None,
    #         tz_offset=60),
    #     "binary": "111110111101111110000011" +
    #               "101001001100100110010001" +
    #               "00000000",
    #     "hex": "fbdf83a2c99100"}
    #
    # TYPE_OBJS = [TYPE_D_OBJ, TYPE_T_OBJ, TYPE_DT_OBJ, TYPE_DTZ_OBJ,
    #              TYPE_DTS_MILLI_OBJ, TYPE_DTS_MICRO_OBJ,
    #              TYPE_DTS_NANO_OBJ, TYPE_DTS_NONE_OBJ,
    #              TYPE_DTSZ_MILLI_OBJ, TYPE_DTSZ_MICRO_OBJ,
    #              TYPE_DTSZ_NANO_OBJ, TYPE_DTSZ_NONE]

    # def test_byte_str_2_type_name(self):
    #     for component in TypeSTest.COMPONENT_S_OBJS:
    #         expected_value = component["expected"]["value"]
    #         expected_value_binary = component["expected"]["value_binary"]
    #         expected_precision_tag = component["expected"]["precision_tag"]
    #         self.assertEquals(
    #             "", expected_value)

    def test_precision(self):
        typeS = TypeS(TypeSTest.COMPONENT_S_OBJS[0]["byte_str"])
        data = (('abcdefghij', "00"), ('abcdefghijabcdefghij', "01"),
                ('abcdefghijabcdefghijabcdefghij', "10"), ('', "11"))
        for pair in data:
            typeS.asBinary = MagicMock(return_value=pair[0])
            self.assertEqual(typeS.precision_tag(), pair[1])

if __name__ == '__main__':
    # noinspection PyUnresolvedReferences
    unittest.main()
