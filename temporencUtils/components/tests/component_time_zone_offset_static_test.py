import unittest
# Object under Test
from temporencUtils.components.tests.base_time_zone_offset_component_test import \
    TimeZoneOffsetComponentBaseTest
from temporencUtils.components.time_zone_offset_component import \
    TimeZoneOffsetComponent as Obj4Test


class TimeZoneOffsetComponentStaticTest(TimeZoneOffsetComponentBaseTest):

    # static methods

    def test_encode(self):
        dp = TimeZoneOffsetComponentStaticTest.DATA_PROVIDER
        for item in dp:
            actual = Obj4Test.encode_minutes_of_offset(item[0])
            expected = item[2]
            msg = "{actual} != {expected} for {item}" \
                .format(actual=actual, expected=expected, item=item[2])
            self.assertEquals(actual, expected, msg=msg)

    def test_encode_as_hex_is_true(self):
        dp = TimeZoneOffsetComponentStaticTest.DATA_PROVIDER
        for item in dp:
            actual = Obj4Test.encode_minutes_of_offset(item[0], asHex=True)
            expected = item[3]
            self.assertEquals(actual, expected,
                              msg=(actual + " != " + expected + " " +
                                   "for " + str(item[0])))

    def test_encode_decode(self):
        dp = TimeZoneOffsetComponentStaticTest.DATA_PROVIDER
        for item in dp:
            expected = item[0]
            #  Encode as Hex
            hex = Obj4Test.encode_minutes_of_offset(item[0], asHex=True)
            # Decode minutes
            actual = Obj4Test.decode(hex, to_minutes=True)
            msg = "{actual} != {expected} for {item}" \
                .format(actual=actual, expected=expected, item=item[3])
            self.assertTrue(actual == expected, msg=msg)

    def test_decode_dec_to_increments(self):
        dp = TimeZoneOffsetComponentStaticTest.DATA_PROVIDER
        for item in dp:
            actual = Obj4Test.decode(item[2])
            # Check default (to_minutes=False) matches
            expected = Obj4Test.decode(item[2], to_minutes=False)
            msg = "{actual} != {expected} for {item} when to_minutes=False" \
                .format(actual=actual, expected=expected, item=item[3])
            self.assertEquals(actual, expected, msg=msg)
            # If they are equal, check for correctness
            expected = item[1]
            msg = "{actual} != {expected} for {item}" \
                .format(actual=actual, expected=expected, item=item[3])
            self.assertEquals(actual, expected, msg=msg)

    def test_decode_dec_to_minutes(self):
        dp = TimeZoneOffsetComponentStaticTest.DATA_PROVIDER
        for item in dp:
            actual = Obj4Test.decode(item[2], to_minutes=True)
            expected = item[0]
            msg = "{actual} != {expected} for {item}" \
                .format(actual=actual, expected=expected, item=item[3])
            self.assertEquals(actual, expected, msg=msg)

    def test_decode_hex_to_decimal(self):
        dp = TimeZoneOffsetComponentStaticTest.DATA_PROVIDER
        for item in dp:
            actual = Obj4Test.decode(item[3])
            # Check default (to_minutes=False) matches
            expected = Obj4Test.decode(item[3], to_minutes=False)
            msg = "{actual} != {expected} for {item} when to_minutes=False" \
                .format(actual=actual, expected=expected, item=item[3])
            self.assertEquals(actual, expected, msg=msg)
            # If they are equal, check for correctness
            expected = item[2]
            msg = "{actual} != {expected} for {item}" \
                .format(actual=actual, expected=expected, item=item[3])
            self.assertEquals(actual, expected, msg=msg)

    def test_decode_hex_to_minutes(self):
        dp = TimeZoneOffsetComponentStaticTest.DATA_PROVIDER
        for item in dp:
            actual = Obj4Test.decode(item[3], to_minutes=True)
            expected = item[0]
            msg = "{actual} != {expected} for {item}" \
                .format(actual=actual, expected=expected, item=item[3])
            self.assertEquals(actual, expected, msg=msg)

    def test_decode_to_decimal_hex_leading_zeros(self):
        dp = [['01000000', 64]]
        for item in dp:

            actual = Obj4Test.decode(item[0])
            expected = item[1]
            msg = "{actual} != {expected} for {item}" \
                .format(actual=actual, expected=expected, item=item)
            self.assertEquals(actual, expected, msg=msg)

    def test_decode_to_decimal_invalid_hex(self):
        dp = ['10000000']
        for item in dp:
            actual = Obj4Test.decode(item)
            expected = None
            msg = "{actual} != {expected} for {item}" \
                .format(actual=actual, expected=expected, item=item)
            self.assertEquals(actual, expected, msg=msg)


if __name__ == '__main__':
    # noinspection PyUnresolvedReferences
    unittest.main()
