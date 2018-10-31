import unittest

from temporencUtils.temporencUtils import TemporencUtils
from temporencUtils.types.typeUtils import TypeUtils


class TypeUtilsTest(unittest.TestCase):
    TYPE_D_OBJ = {
        "type": TypeUtils.TYPE_D["_type_name"],
        "byte_str": TemporencUtils.packb(
            value=None, type=None,
            year=1983, month=1, day=15,
            hour=None, minute=None, second=None,
            millisecond=None, microsecond=None, nanosecond=None,
            tz_offset=None),
        "binary": "100011110111111000001110",
        "hex": "8f7e0e"}
    TYPE_T_OBJ = {
        "type": TypeUtils.TYPE_T["_type_name"],
        "byte_str": TemporencUtils.packb(
            value=None, type=None,
            year=None, month=None, day=None,
            hour=18, minute=25, second=12,
            millisecond=None, microsecond=None, nanosecond=None,
            tz_offset=None),
        "binary": "101000010010011001001100",
        "hex": "a1264c"}
    TYPE_DT_OBJ = {
        "type": TypeUtils.TYPE_DT["_type_name"],
        "byte_str": TemporencUtils.packb(
            value=None, type=None,
            year=1983, month=1, day=15,
            hour=18, minute=25, second=12,
            millisecond=None, microsecond=None, nanosecond=None,
            tz_offset=None),
        "binary": "0001111011111100000111010010011001001100",
        "hex": "1efc1d264c"}
    TYPE_DTZ_OBJ = {
        "type": TypeUtils.TYPE_DTZ["_type_name"],
        "byte_str": TemporencUtils.packb(
            value=None, type=None,
            year=1983, month=1, day=15,
            hour=18, minute=25, second=12,
            millisecond=None, microsecond=None, nanosecond=None,
            tz_offset=60),
        "binary": "110011110111111000001110100010110010011001000100",
        "hex": "cf7e0e8b2644"}
    TYPE_DTS_MILLI_OBJ = {
        "type": TypeUtils.TYPE_DTS_MILLI["_type_name"][:3],
        "byte_str": TemporencUtils.packb(
            value=None, type=None,
            year=1983, month=1, day=15,
            hour=18, minute=25, second=12,
            millisecond=123, microsecond=None, nanosecond=None,
            tz_offset=None),
        "binary": "01000111101111110000011101001001100100110000011110110000",
        "hex": "47bf07499307b0",
        "expected": {
             "value": "123",
             "value_binary": "0001111011",
             "precision_tag": TypeUtils.PRECISION_TAGS["millisecond"]}
    }
    TYPE_DTS_MICRO_OBJ = {
        "type": TypeUtils.TYPE_DTS_MILLI["_type_name"][:3],
        "byte_str": TemporencUtils.packb(
            value=None, type=None,
            year=1983, month=1, day=15,
            hour=18, minute=25, second=12,
            millisecond=None, microsecond=123456, nanosecond=None,
            tz_offset=None),
        "binary": "010101111011111100000111" +
                  "010010011001001100000111" +
                  "1000100100000000",
        "hex": "57bf074993078900",
        "expected": {
            "value": "123456",
            "value_binary": "00011110001001000000",
            "precision_tag": TypeUtils.PRECISION_TAGS["microsecond"]}
    }
    TYPE_DTS_NANO_OBJ = {
        "type": TypeUtils.TYPE_DTS_MILLI["_type_name"][:3],
        "byte_str": TemporencUtils.packb(
            value=None, type=None,
            year=1983, month=1, day=15,
            hour=18, minute=25, second=12,
            millisecond=None, microsecond=None, nanosecond=123456789,
            tz_offset=None),
        "binary": "011001111011111100000111" +
                  "010010011001001100000111" +
                  "010110111100110100010101",
        "hex": "67bf074993075bcd15",
        "expected": {
            "value": "123456789",
            "value_binary": "000111010110111100110100010101",
            "precision_tag": TypeUtils.PRECISION_TAGS["nanosecond"]}
    }
    TYPE_DTS_NONE_OBJ = {
        "type": TypeUtils.TYPE_DTS_MILLI["_type_name"][:3],
        "byte_str": TemporencUtils.packb(
            value=None, type="DTS",
            year=1983, month=1, day=15,
            hour=18, minute=25, second=12,
            millisecond=None, microsecond=None, nanosecond=None,
            tz_offset=None),
        "binary": "011101111011111100000111010010011001001100000000",
        "hex": "77bf07499300",
        "expected": {
            "value": "",
            "value_binary": "",
            "precision_tag": TypeUtils.PRECISION_TAGS["none"]}
    }
    TYPE_DTSZ_MILLI_OBJ = {
        "type": TypeUtils.TYPE_DTSZ_MILLI["_type_name"][:4],
        "byte_str": TemporencUtils.packb(
            value=None, type=None,
            year=1983, month=1, day=15,
            hour=18, minute=25, second=12,
            millisecond=123, microsecond=None, nanosecond=None,
            tz_offset=60),
        "binary": "111000111101111110000011" +
                  "101000101100100110000011" +
                  "1101110001000000",
        "hex": "e3df83a2c983dc40",
        "expected": {
            "value": "123",
            "value_binary": "0001111011",
            "precision_tag": TypeUtils.PRECISION_TAGS["millisecond"]}
    }
    TYPE_DTSZ_MICRO_OBJ = {
        "type": TypeUtils.TYPE_DTSZ_MILLI["_type_name"][:4],
        "byte_str": TemporencUtils.packb(
            value=None, type=None,
            year=1983, month=1, day=15,
            hour=18, minute=25, second=12,
            millisecond=None, microsecond=123456, nanosecond=None,
            tz_offset=60),
        "binary": "111010111101111110000011" +
                  "101000101100100110000011" +
                  "110001001000000100010000",
        "hex": "ebdf83a2c983c48110",
        "expected": {
            "value": "123456",
            "value_binary": "00011110001001000000",
            "precision_tag": TypeUtils.PRECISION_TAGS["microsecond"]}
    }
    TYPE_DTSZ_NANO_OBJ = {
        "type": TypeUtils.TYPE_DTSZ_MILLI["_type_name"][:4],
        "byte_str": TemporencUtils.packb(
            value=None, type=None,
            year=1983, month=1, day=15,
            hour=18, minute=25, second=12,
            millisecond=None, microsecond=None, nanosecond=123456789,
            tz_offset=60),
        "binary": "111100111101111110000011" +
                  "101000101100100110000011" +
                  "101011011110011010001010" +
                  "11000100",
        "hex": "f3df83a2c983ad e68ac4",
        "expected": {
            "value": "123456789",
            "value_binary": "000111010110111100110100010101",
            "precision_tag": TypeUtils.PRECISION_TAGS["nanosecond"]}
    }
    TYPE_DTSZ_NONE = {
        "type": TypeUtils.TYPE_DTSZ_MILLI["_type_name"][:4],
        "byte_str": TemporencUtils.packb(
            value=None, type="DTSZ",
            year=1983, month=1, day=15,
            hour=18, minute=25, second=12,
            millisecond=None, microsecond=None, nanosecond=None,
            tz_offset=60),
        "binary": "111110111101111110000011" +
                  "101001001100100110010001" +
                  "00000000",
        "hex": "fbdf83a2c99100",
        "expected": {
            "value": "",
            "value_binary": "",
            "precision_tag": TypeUtils.PRECISION_TAGS["none"]}
    }
    TYPE_OBJS = [TYPE_D_OBJ, TYPE_T_OBJ, TYPE_DT_OBJ, TYPE_DTZ_OBJ,
                 TYPE_DTS_MILLI_OBJ, TYPE_DTS_MICRO_OBJ,
                 TYPE_DTS_NANO_OBJ, TYPE_DTS_NONE_OBJ,
                 TYPE_DTSZ_MILLI_OBJ, TYPE_DTSZ_MICRO_OBJ,
                 TYPE_DTSZ_NANO_OBJ, TYPE_DTSZ_NONE]
    COMPONENT_S_NAMES = [
        TYPE_DTS_MILLI_OBJ["type"], TYPE_DTS_MICRO_OBJ["type"],
        TYPE_DTS_NANO_OBJ["type"], TYPE_DTS_NONE_OBJ["type"],
        TYPE_DTSZ_MILLI_OBJ["type"], TYPE_DTSZ_MICRO_OBJ["type"],
        TYPE_DTSZ_NANO_OBJ["type"], TYPE_DTSZ_NONE["type"]]

    def test_byte_str_2_type_name(self):
        for temporenc_type in TypeUtilsTest.TYPE_OBJS:
            byte_str = temporenc_type["byte_str"]
            expected = temporenc_type["type"]
            self.assertEquals(
                TypeUtils.byte_str_2_type_name(byte_str), expected)

    def test_parse_component_s(self):
        for temporenc_type in TypeUtilsTest.TYPE_OBJS:
            if temporenc_type["type"] in TypeUtilsTest.COMPONENT_S_NAMES:
                expected = temporenc_type["expected"]["value_binary"]
                actual = TypeUtils.parse_component_s(
                    temporenc_type["byte_str"])
                self.assertEquals(actual, expected)
        print "test_parse_component_s() Completed"

    def test_type_name_2_type_tag(self):
        for temporenc_type in TypeUtils.TYPES:
            self.assertEqual(
                TypeUtils.type_name_2_type_tag(temporenc_type["_type_name"]),
                temporenc_type["type_tag"])

    def test_type_tag_to_type_name(self):
        for temporenc_type in TypeUtils.TYPES:
            self.assertEqual(
                TypeUtils.type_tag_to_type_name(temporenc_type["type_tag"]),
                temporenc_type["_type_name"])

    def test_isValidPrecisionName(self):
        for ss in ("millisecond", "microsecond", "nanosecond", "none"):
            self.assertTrue(TypeUtils.isValidPrecisionName(ss))

    def test_isValidTypeName(self):
        for temporenc_type in ("D", "T", "DT", "DTZ", "DTS", "DTSZ"):
            self.assertTrue(TypeUtils.isValidTypeName(temporenc_type))


if __name__ == '__main__':
    # noinspection PyUnresolvedReferences
    unittest.main()
