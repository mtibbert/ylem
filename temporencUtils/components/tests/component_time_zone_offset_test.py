import random
import unittest

from temporencUtils.components.tests.base_time_zone_offset_component_test import \
    TimeZoneOffsetComponentBaseTest
from temporencUtils.components.time_zone_offset_component import \
    TimeZoneOffsetComponent as Obj4Test


class TimeZoneOffsetComponentTest(TimeZoneOffsetComponentBaseTest):

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
        actual = obj.__class__.decode(obj.as_binary(), to_minutes=True)
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
            actual = obj.__class__.decode(obj.as_binary(), to_minutes=True)
            expected = start_mins
            msg = "{actual} != {expected} for {item}" \
                .format(actual=actual, expected=expected, item=item[3])
            self.assertEquals(actual, expected, msg=msg)

    def test_ctor_arg_valid(self):
        expected = Obj4Test.INCREMENT_SIZE * \
                   (random.randint(self.MIN, self.MAX) -
                    Obj4Test.OFFSET_INCREMENT)
        obj = Obj4Test(expected, encode=True)
        actual = obj.__class__.decode(obj.as_binary(), to_minutes=True)
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

    # # dp format [0 = minutes, 1 = increments, 2 = decimal, 3 = hex]
    #
    # def test_as_binary(self):
    #     dp = self.__class__.DATA_PROVIDER
    #     for item in dp:
    #         obj = TimeZoneOffsetComponent(item[0])
    #         actual = obj.as_binary()
    #         expected = item[3]
    #         msg = "{actual} != {expected} for {item}" \
    #             .format(actual=actual, expected=expected, item=item[3])
    #         self.assertEquals(actual, expected, msg=msg)

    #     # offset = random.randint(self.MIN, self.MAX)
    #     offsets = [{"minutes": 0, "_binary": "1000000"},
    #                {"minutes": 60, "_binary": "1000100"},
    #                {"minutes": -360, "_binary": "0101000"}]
    #     for offset in offsets:
    #         expected = offset["_binary"]
    #         obj = TimeZoneOffsetComponent(offset["minutes"], True)
    #         actual = obj.as_binary()
    #         msg = "{actual} != {expected} for {offset}" \
    #             .format(actual=actual, expected=expected, offset=offset)
    #         self.assertEquals(actual, expected, msg=msg)
    #
    # def test_as_binary_len(self):
    #     # offset = random.randint(self.MIN, self.MAX)
    #     offset = 94  # 94 fails
    #     obj = TimeZoneOffsetComponent(offset, True)
    #     self.assertEquals(len(obj.as_binary()), self.BIT_LEN, "Where offset = " + str(offset))

    # def test_as_json(self):
    #     data = [
    #         {"increments": "0",
    #          "expected": {
    #              "offset": "+00:00",
    #              '"z"': {
    #                  "increments": "0",
    #                  "decimal": "64",
    #                  "_binary": "1000000"}}},
    #         {"increments": "4",
    #          "expected": {
    #              "offset": "+01:00",
    #              '"z"': {
    #                  "increments": "0",
    #                  "decimal": "68",
    #                  "_binary": "1000100"}}},
    #         {"increments": "-24",
    #          "expected": {
    #              "offset": "-06:00",
    #              '"z"': {
    #                  "increments": "-24",
    #                  "decimal": "40",
    #                  "_binary": "0101000"}}}]
    #     for pair in data:
    #         actual = SubSecondComponent(pair["byte_string"])
    #         expected = pair["expected"]
    #         self.assertEqual(actual.as_json(), expected)


if __name__ == '__main__':
    # noinspection PyUnresolvedReferences
    unittest.main()
