import json
import random
import unittest

from temporencUtils.components.tests.base_time_zone_offset_component_test\
    import TimeZoneOffsetComponentBaseTest
from temporencUtils.components.time_zone_offset_component\
    import TimeZoneOffsetComponent as Obj4Test


class TimeZoneOffsetComponentTest(TimeZoneOffsetComponentBaseTest):

    # constructor

    def test_ctor_default(self):
        item = [0, 0, 64, "1000000"]
        # Default is 0 increments
        obj = Obj4Test()
        # Check _binary
        actual = obj.as_binary()
        expected = item[3]
        msg = "{actual} != {expected} for {item}" \
            .format(actual=actual, expected=expected,
                    item="default ctor - encoded _binary")
        self.assertEquals(actual, expected, msg=msg)
        # Convert back minutes
        actual = obj.__class__.decode(obj.as_binary(), as_minutes=True)
        expected = item[0]
        msg = "{actual} != {expected} for {item}" \
            .format(actual=actual, expected=expected,
                    item="default ctor - minutes")
        self.assertEquals(actual, expected, msg=msg)

    def test_ctor_encode_true(self):
        dp = self.__class__.DATA_PROVIDER
        for item in dp:
            start_mins = item[0]
            obj = Obj4Test(start_mins, encode=True)
            actual = obj.__class__.decode(obj.as_binary(), as_minutes=True)
            expected = start_mins
            msg = "{actual} != {expected} for {item}" \
                .format(actual=actual, expected=expected, item=item[3])
            self.assertEquals(actual, expected, msg=msg)

    def test_ctor_arg_valid(self):
        expected = Obj4Test.INCREMENT_SIZE * \
                   (random.randint(self.MIN, self.MAX) -
                    Obj4Test.OFFSET_INCREMENT)
        obj = Obj4Test(expected, encode=True)
        actual = obj.__class__.decode(obj.as_binary(), as_minutes=True)
        self.assertEquals(actual, expected)

    def test_ctor_out_of_range(self):
        offsets = [self.MIN-1, self.NOT_SET+1]
        for offset in offsets:
            with self.assertRaises(ValueError) as ve:
                Obj4Test(offset - Obj4Test.OFFSET_INCREMENT)
                the_exception = ve.exception
                expected = "The offset {arg} is not " + \
                           "in the range {lower} to {upper}".format(
                               arg=offset, lower=self.MIN, upper=self.NOT_SET)
                self.assertEqual(the_exception.message, expected)

    def test_ctor_special_not_utc(self):
        expected = str(int(bin(Obj4Test.TZ_NOT_UTC)[2:]))
        for offset in range(930, 945):
            obj = Obj4Test(offset, encode=True)
            actual = obj.as_binary()
            msg = "The offset {offset} is not " + \
                  "in the range {lower} to {upper}".format(
                      arg=offset, lower=self.MIN, upper=self.NOT_SET)
            self.assertEqual(actual, expected, msg=msg)

    def test_ctor_special_not_set(self):
        expected = str(int(bin(Obj4Test.NOT_SET)[2:]))
        for offset in range(945, 960):
            obj = Obj4Test(offset, encode=True)
            actual = obj.as_binary()
            msg = "The offset {offset} is not " + \
                  "in the range {lower} to {upper}".format(
                      arg=offset, lower=self.MIN, upper=self.NOT_SET)
            self.assertEqual(actual, expected, msg=msg)

    # instance methods

    def test_as_binary(self):
        dp = self.__class__.DATA_PROVIDER
        for item in dp:
            obj = Obj4Test(item[1])
            actual = obj.as_binary()
            expected = item[3]
            msg = "{actual} != {expected} for {item}" \
                .format(actual=actual, expected=expected, item=item[3])
            self.assertEquals(actual, expected, msg=msg)

    def test_as_binary_len(self):
        expected = Obj4Test.BIT_LEN
        for offset in range(Obj4Test.MIN, (Obj4Test.NOT_SET + 1)):
            obj = Obj4Test(offset - Obj4Test.OFFSET_INCREMENT, True)
            actual = len(obj.as_binary())
            msg = "The binary length ({len}) of offset {offset} is not {bits} "\
                .format(offset=offset, len=actual, bits=expected)
            self.assertTrue(actual == expected, msg=msg)

    def test_as_json(self):
        dp = self.__class__.DATA_PROVIDER
        for item in dp:
            data = {
                "increments": "0",
                "expected": {
                    "z": {
                        "binary": str(item[3]),
                        "decimal": str(item[2]),
                        "increments": str(item[1]),
                        "minutes": str(item[0])}}}
            actual = Obj4Test(item[0], True)
            expected = json.dumps(data["expected"])
            self.assertEqual(expected, actual.as_json())

    def test_as_minutes(self):
        dp = self.__class__.DATA_PROVIDER
        for item in dp:
            obj = Obj4Test(item[1])
            actual = obj.as_minutes()
            expected = item[0]
            msg = "{actual} != {expected} for {item}" \
                .format(actual=actual, expected=expected, item=item[3])
            self.assertEquals(actual, expected, msg=msg)

    def test_is_utc(self):
        # Valid offsets return True
        for offset in range(Obj4Test.MIN, Obj4Test.MAX + 1):
            increments = offset - Obj4Test.OFFSET_INCREMENT
            obj = Obj4Test(increments)
            actual = obj.is_utc()
            msg = "The offset {offset} is in the range {lower} to {upper}." \
                .format(offset=offset, lower=Obj4Test.MIN, upper=Obj4Test.MAX)
            self.assertTrue(actual, msg=msg)
        # TZ_NOT_UTC & NOT_SET return False
        for offset in range(Obj4Test.TZ_NOT_UTC, Obj4Test.NOT_SET + 1):
            increments = offset - Obj4Test.OFFSET_INCREMENT
            obj = Obj4Test(increments)
            actual = obj.is_utc()
            msg = "The offset {offset} is in the range {lower} to {upper}." \
                .format(offset=offset, lower=Obj4Test.MIN, upper=Obj4Test.MAX)
            self.assertFalse(actual, msg=msg)

    def test_is_not_set(self):
        offset = Obj4Test.NOT_SET
        increments = offset - Obj4Test.OFFSET_INCREMENT
        obj = Obj4Test(increments)
        actual = obj.is_not_set()
        self.assertTrue(actual)
        # Valid offsets return False
        for offset in range(Obj4Test.MIN, Obj4Test.TZ_NOT_UTC + 1):
            increments = offset - Obj4Test.OFFSET_INCREMENT
            obj = Obj4Test(increments)
            actual = obj.is_not_set()
            msg = "The offset {offset} is in the range {lower} to {upper}; " + \
                  "it should be {notset}".format(
                      offset=offset, lower=Obj4Test.MIN,
                      upper=Obj4Test.TZ_NOT_UTC, notset=Obj4Test.NOT_SET)
            self.assertFalse(actual, msg=msg)

    def test_is_tzinfo_not_utc(self):
        offset = Obj4Test.TZ_NOT_UTC
        increments = offset - Obj4Test.OFFSET_INCREMENT
        obj = Obj4Test(increments)
        actual = obj.is_tzinfo_not_utc_info()
        msg = "The offset {offset} (or {increments} increments) was " +\
              "reserved for non-UTC time zone information."
        msg = msg.format(offset=offset, increments=increments)
        self.assertTrue(actual, msg=msg)
        # Valid offsets return False
        for offset in range(Obj4Test.MIN, Obj4Test.MAX + 1):
            increments = offset - Obj4Test.OFFSET_INCREMENT
            obj = Obj4Test(increments)
            actual = obj.is_tzinfo_not_utc_info()
            msg = "The offset {offset} represents UTC info; should be {notutc}"\
                .format(offset=offset, notutc=Obj4Test.TZ_NOT_UTC)
            self.assertFalse(actual, msg=msg)

    def test_is_valid(self):
        valid_range = range(Obj4Test.MIN, Obj4Test.NOT_SET + 1)
        for offset in valid_range:
            obj = Obj4Test(offset - Obj4Test.OFFSET_INCREMENT)
            msg = "The offset {offset} not found in the " + \
                  "range {lower} to {upper}."
            msg = msg.format(offset=offset,
                             lower=Obj4Test.MIN, upper=Obj4Test.MAX)
            self.assertTrue(obj.is_valid(), msg=msg)


if __name__ == '__main__':
    # noinspection PyUnresolvedReferences
    unittest.main()
