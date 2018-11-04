import unittest
# Object under Test
from temporencUtils.components.tests.base_time_zone_offset_component_test import \
    TimeZoneOffsetComponentBaseTest
from temporencUtils.components.time_zone_offset_component import \
    TimeZoneOffsetComponent as Obj4Test


class TimeZoneOffsetComponentStaticTest(TimeZoneOffsetComponentBaseTest):

    # static constants

    def test_min(self):
        self.assertEquals(Obj4Test.MIN,
                          TimeZoneOffsetComponentStaticTest.MIN)
    def test_max(self):
        self.assertEquals(Obj4Test.MAX,
                          TimeZoneOffsetComponentStaticTest.MAX)

    def test_tz_not_utc(self):
        self.assertEquals(Obj4Test.TZ_NOT_UTC,
                          TimeZoneOffsetComponentStaticTest.TZ_NOT_UTC)

    def test_not_set(self):
        self.assertEquals(Obj4Test.NOT_SET,
                          TimeZoneOffsetComponentStaticTest.NOT_SET)

    def test_increment_size(self):
        self.assertEquals(Obj4Test.INCREMENT_SIZE,
                          TimeZoneOffsetComponentStaticTest.INCREMENT_SIZE)

    def test_bit_len(self):
        self.assertEquals(Obj4Test.BIT_LEN,
                          TimeZoneOffsetComponentStaticTest.BIT_LEN)

    def test_offset(self):
        self.assertEquals(Obj4Test.OFFSET_INCREMENT,
                          TimeZoneOffsetComponentStaticTest.OFFSET_INCREMENT)


    # static methods

    def test_encode(self):
        dp = TimeZoneOffsetComponentStaticTest.DATA_PROVIDER
        for item in dp:
            actual = Obj4Test.encode_minutes_of_offset(item[0])
            expected = item[2]
            msg = "{actual} != {expected} for {item}" \
                .format(actual=actual, expected=expected, item=item[2])
            self.assertEquals(actual, expected, msg=msg)

    def test_encode_as_bin_is_true(self):
        dp = TimeZoneOffsetComponentStaticTest.DATA_PROVIDER
        for item in dp:
            actual = Obj4Test.encode_minutes_of_offset(item[0], as_bin=True)
            expected = item[3]
            self.assertEquals(actual, expected,
                              msg=(actual + " != " + expected + " " +
                                   "for " + str(item[0])))

    def test_encode_decode(self):
        dp = TimeZoneOffsetComponentStaticTest.DATA_PROVIDER
        for item in dp:
            expected = item[0]
            #  Encode as Binary
            bin = Obj4Test.encode_minutes_of_offset(item[0], as_bin=True)
            # Decode minutes
            actual = Obj4Test.decode(bin, as_minutes=True)
            msg = "{actual} != {expected} for {item}" \
                .format(actual=actual, expected=expected, item=item[3])
            self.assertTrue(actual == expected, msg=msg)

    def test_decode_dec_to_increments(self):
        dp = TimeZoneOffsetComponentStaticTest.DATA_PROVIDER
        for item in dp:
            actual = Obj4Test.decode(item[2])
            # Check default (to_minutes=False) matches
            expected = Obj4Test.decode(item[2], as_minutes=False)
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
            actual = Obj4Test.decode(item[2], as_minutes=True)
            expected = item[0]
            msg = "{actual} != {expected} for {item}" \
                .format(actual=actual, expected=expected, item=item[3])
            self.assertEquals(actual, expected, msg=msg)

    def test_decode_bin_to_decimal(self):
        dp = TimeZoneOffsetComponentStaticTest.DATA_PROVIDER
        for item in dp:
            actual = Obj4Test.decode(item[3])
            # Check default (to_minutes=False) matches
            expected = Obj4Test.decode(item[3], as_minutes=False)
            msg = "{actual} != {expected} for {item} when to_minutes=False" \
                .format(actual=actual, expected=expected, item=item[3])
            self.assertEquals(actual, expected, msg=msg)
            # If they are equal, check for correctness
            expected = item[2]
            msg = "{actual} != {expected} for {item}" \
                .format(actual=actual, expected=expected, item=item[3])
            self.assertEquals(actual, expected, msg=msg)

    def test_decode_bin_to_minutes(self):
        dp = TimeZoneOffsetComponentStaticTest.DATA_PROVIDER
        for item in dp:
            actual = Obj4Test.decode(item[3], as_minutes=True)
            expected = item[0]
            msg = "{actual} != {expected} for {item}" \
                .format(actual=actual, expected=expected, item=item[3])
            self.assertEquals(actual, expected, msg=msg)

    def test_decode_to_decimal_bin_leading_zeros(self):
        dp = [['01000000', 64]]
        for item in dp:

            actual = Obj4Test.decode(item[0])
            expected = item[1]
            msg = "{actual} != {expected} for {item}" \
                .format(actual=actual, expected=expected, item=item)
            self.assertEquals(actual, expected, msg=msg)

    def test_decode_to_decimal_invalid_bin(self):
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
