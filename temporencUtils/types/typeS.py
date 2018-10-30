import binascii
import json

from temporencUtils.temporencUtils import TemporencUtils
from temporencUtils.types.baseType import BaseType
from temporencUtils.types.typeUtils import TypeUtils


class TypeS(BaseType):

    # inherited from BaseType
    # _byte_str = None

    def __init__(self, byte_str):
        # raises ValueError if unable to pack
        BaseType.__init__(self, byte_str)

        # TODO: Refactor When Issue #5 is fixed
        len_byte_str = len(byte_str)
        padded_bin_str = ('{:0>' + (str(len(byte_str) * 8)) + 'b}') \
            .format(int(binascii.hexlify(self._byte_str), 16))
        assert(len(padded_bin_str) % 1) != 1

        if (len_byte_str == TypeUtils.TYPE_DTS_NONE["size"])\
                and (padded_bin_str[0] == "0"):
            self._type_name = TypeUtils.TYPE_DTS_NONE["_type_name"]
        elif (len_byte_str == TypeUtils.TYPE_DTS_NONE["size"])\
                and (padded_bin_str[0] == "1"):
            self._type_name = TypeUtils.TYPE_DTZ["_type_name"]
        else:
            self._type_name = TypeUtils.byte_str_2_type_name(byte_str)

        self.moment = TemporencUtils.unpackb(byte_str)
        # end Refactor When Issue #5 is fixed


    def binary_millisecond(self):
        """
        Returns the millisecond in binary format
        :return: binary string
        :rtype: string

        # >>> obj = TemporencUtils.packb(\
        #               value=None, type=None, year=None, month=None,\
        #               day=None, hour=None, minute=None, second=None,\
        #               millisecond=None, microsecond=None, nanosecond=None,\
        #               tz_offset=None)
        #
        # >>> typeD = TypeS(obj)
        #
        # >>> typeD.binary_millisecond()
        # '0001111011' #

        """
        return self.asBinary()[2:]

    def binary_microsecond(self):
        """
        Returns the second in binary format
        :return: binary string
        :rtype: string

        # >>> obj = TemporencUtils.packb(\
        #               value=None, type=None, year=None, month=None,\
        #               day=None, hour=None, minute=None, second=None,\
        #               millisecond=None, microsecond=123456, nanosecond=None,\
        #               tz_offset=None)
        #
        # >>> typeD = TypeS(obj)
        #
        # >>> typeD.binary_microsecond()
        # '00011110001001000000' #
        """
        return self.asBinary()[2:]

    def binary_nanosecond(self):
        """
        Returns the nanosecond in binary format
        :return: binary string
        :rtype: string

        # >>> obj = TemporencUtils.packb(\
        #               value=None, type=None, year=None, month=None,\
        #               day=None, hour=None, minute=None, second=None,\
        #               millisecond=None, microsecond=None, nanosecond=123456789,\
        #               tz_offset=None)
        #
        # >>> typeD = TypeS(obj)
        #
        # >>> typeD.binary_nanosecond()
        # '000111010110111100110100010101' #

        """
        return self.asBinary()[2:]

    def asBinary(self):
        """
        Returns binary representation
        :return: binary string
        :rtype: string
        """
        return TemporencUtils.byte_str_2_bin_str(self._byte_str)

    def binStrPrecision(self):
        """
        Returns binary representation of the precision substrubg
        :return: binary string
        :rtype: string

        # Check when not DTS/DTSZ object
        >>> obj = TemporencUtils.packb(\
                      value=None, type=None, year=123, month=None,\
                      day=None, hour=None, minute=None, second=None,\
                      millisecond=None, microsecond=None, nanosecond=None,\
                      tz_offset=None)

        >>> typeS = TypeS(obj)

        # should raise Type Error
        >>> typeS.binStrPrecision()
        Traceback (most recent call last):
        ...
        TypeError: Binary string does not unpack into a Type DTS or DTSZ object.

        >>> obj = TemporencUtils.packb(\
                      value=None, type=None, year=123, month=None,\
                      day=None, hour=None, minute=None, second=None,\
                      millisecond=None, microsecond=None, nanosecond=None,\
                      tz_offset=60)

        >>> typeS = TypeS(obj)

        # should raise Type Error
        >>> typeS.binStrPrecision()
        Traceback (most recent call last):
        ...
        TypeError: Binary string does not unpack into a Type DTS or DTSZ object.

        # Check DTS / DTSZ - millisecond
        >>> obj = TemporencUtils.packb(\
                      value=None, type=None, year=1983, month=01,\
                      day=15, hour=18, minute=25, second=12,\
                      millisecond=123, microsecond=None, nanosecond=None,\
                      tz_offset=None)

        >>> typeS = TypeS(obj)

        >>> typeS.binStrPrecision()
        '0001111011'

        >>> obj = TemporencUtils.packb(\
                      value=None, type=None, year=1983, month=01,\
                      day=15, hour=18, minute=25, second=12,\
                      millisecond=123, microsecond=None, nanosecond=None,\
                      tz_offset=60)

        >>> typeS = TypeS(obj)

        >>> typeS.binStrPrecision()
        '0001111011'

        # Check DTS / DTSZ - microsecond
        >>> obj = TemporencUtils.packb(\
                      value=None, type=None, year=1983, month=01,\
                      day=15, hour=18, minute=25, second=12,\
                      millisecond=None, microsecond=123456, nanosecond=None,\
                      tz_offset=None)

        >>> typeS = TypeS(obj)

        >>> typeS.binStrPrecision()
        '00011110001001000000'

        >>> obj = TemporencUtils.packb(\
                      value=None, type=None, year=1983, month=01,\
                      day=15, hour=18, minute=25, second=12,\
                      millisecond=None, microsecond=123456, nanosecond=None,\
                      tz_offset=60)

        >>> typeS = TypeS(obj)

        >>> typeS.binStrPrecision()
        '00011110001001000000'

        # # # Check DTS - nanosecond
        >>> obj = TemporencUtils.packb(\
                      value=None, type=None, year=1983, month=01,\
                      day=15, hour=18, minute=25, second=12,\
                      millisecond=None, microsecond=None, nanosecond=123456789,\
                      tz_offset=None)

        >>> typeS = TypeS(obj)

        >>> typeS.binStrPrecision()
        '000111010110111100110100010101'

        # Check DTS - none
        >>> obj = TemporencUtils.packb(\
                      value=None, type='DTS', year=1983, month=01,\
                      day=15, hour=18, minute=25, second=12,\
                      millisecond=None, microsecond=None, nanosecond=None,\
                      tz_offset=None)

        >>> typeS = TypeS(obj)

        >>> typeS.binStrPrecision()
        '0000'

        """
        bin_str = None
        dts_offset = 42
        dtsz_offset = dts_offset + 1
        milli_len = 10
        micro_len = 20
        nano_len = 30
        none_len = 4

        bin_str_len = len(self._byte_str)

        # TODO: When Issue #5 is fixed:
        #         Remove next line
        #         Uncomment following line
        temporenc_type = self._type_name
        #
        # TODO: Resume here after Issue #6
        #
        # temporenc_type = TypeUtils.byte_str_2_type_name(self._byte_str)

        if temporenc_type == "DTS":
            if bin_str_len == TypeUtils.TYPE_DTS_MILLI["size"]:
                bin_str = self.extract_dts_bin_str(
                    TypeUtils.TYPE_DTS_MILLI["size"], (dts_offset, milli_len))
            if bin_str_len == TypeUtils.TYPE_DTS_MICRO["size"]:
                bin_str = self.extract_dts_bin_str(
                    TypeUtils.TYPE_DTS_MICRO["size"], (dts_offset, micro_len))
            if bin_str_len == TypeUtils.TYPE_DTS_NANO["size"]:
                bin_str = self.extract_dts_bin_str(
                    TypeUtils.TYPE_DTS_NANO["size"], (dts_offset, nano_len))
            if bin_str_len == TypeUtils.TYPE_DTS_NONE["size"]:
                bin_str = self.extract_dts_bin_str(
                    TypeUtils.TYPE_DTS_NONE["size"], (dts_offset, none_len))
        elif temporenc_type[:4] == "DTSZ":
            if bin_str_len == TypeUtils.TYPE_DTSZ_MILLI["size"]:
                bin_str = self.extract_dts_bin_str(
                    TypeUtils.TYPE_DTSZ_MILLI["size"], (dtsz_offset, milli_len))
            if bin_str_len == TypeUtils.TYPE_DTSZ_MICRO["size"]:
                bin_str = self.extract_dts_bin_str(
                    TypeUtils.TYPE_DTSZ_MICRO["size"], (dtsz_offset, micro_len))
            if bin_str_len == TypeUtils.TYPE_DTSZ_NANO["size"]:
                bin_str = self.extract_dts_bin_str(
                    TypeUtils.TYPE_DTSZ_NANO["size"], (dtsz_offset, nano_len))
            if bin_str_len == TypeUtils.TYPE_DTSZ_NONE["size"]:
                bin_str = self.extract_dts_bin_str(
                    TypeUtils.TYPE_DTSZ_NONE["size"], (dtsz_offset, none_len))
        else:
            raise TypeError(
                'Binary string does not unpack into a Type DTS or DTSZ object.')
        return bin_str

    def extract_dts_bin_str(self, size, trim):
        bit_len = (8 * int(size))
        end = trim[0] + trim[1]
        start = trim[0]
        width = str(trim[1])
        bin_str = ('{:0>' + width + '}').format(
            TemporencUtils.byte_str_2_bin_str(
                self._byte_str, bit_len))[start:end]
        return bin_str

    def asJson(self, verbose=False):
        """
        Returns date information
        :param verbose: include full type information when True;
                        when False (default), only date information is included.
        :type verbose: boolean
        :return: JSON formatted string
        :rtype: string

        # Millesecond
        # >>> obj = TemporencUtils.packb(\
        #               value=None, type=None, year=None, month=None,\
        #               day=None, hour=None, minute=None, second=None,\
        #               millisecond=123, microsecond=None, nanosecond=None,\
        #               tz_offset=None)
        # >>> typeD = TypeS(obj)
        #
        # >>> typeD.asJson() == typeD.asJson(False)
        # True
        # >>> typeD.asJson()
        # '"s": {
        #             # "binary": {
        #             #     "millisecond": "None",
        #             #     "microsecond": "None",
        #             #     "nanosecond": "None"}
        #         }'
        #
        # >>> typeD.asJson(verbose=True)
        ''
        """
        template = {
            "d": {
                "year": "None",
                "month": "None",
                "day": "None",
                "binary": {
                    "year": "None",
                    "month": "None",
                    "day": "None"}
            }}

        moment = TemporencUtils.unpackb(self._byte_str)
        data = template["d"]
        if data["year"] is not None:
            data["year"] = str(moment.year)
            data["binary"]["year"] = self.binary_year()
        if data["month"] is not None:
            data["month"] = str(moment.month)
            data["binary"]["month"] = self.binary_month()
        if data["day"] is not None:
            data["day"] = str(moment.day)
            data["binary"]["day"] = self.binary_day()

        if verbose:
            verbose_temp = json.loads(BaseType.asJson(self))
            key = verbose_temp.keys()[0]
            verbose_temp[key][u"d"] = template["d"]
            template = verbose_temp

        return json.dumps(template)

    # Demonstrate bug associated with Issue #5
    @staticmethod
    def is_issue_active__check_byte_str_2_type_name():
        """
        Demonstrates a bug where a properly formatted Type DTS Component is
        identified as a DTZ Component.
        :return: boolean True if the bug exists, otherwise false
        :rtype: boolean

        >>> TypeS.is_issue_active__check_byte_str_2_type_name()
        Meta
          Moment: 1983-01-15 18:25:12
          Hex:    77bf07499300
          Binary: 011101111011111100000111010010011001001100000000
          byte_str_2_type_name() returns correct value: False
          Work-around returns correct value: True


        """
        obj = TemporencUtils.packb(
            value=None, type="DTS",
            year=1983, month=01, day=15,
            hour=18, minute=25, second=12,
            millisecond=None, microsecond=None, nanosecond=None,
            tz_offset=None)
        moment = TemporencUtils.unpackb(obj)
        hex_str = binascii.hexlify(obj)
        expected_bin_str = ('{:0>' + (str(len(obj) * 8)) + 'b}') \
            .format(int(binascii.hexlify(obj), 16))
        expected = "DTS"
        actual = TypeUtils.byte_str_2_type_name(obj)
        actual_eq_expected = (actual == expected)
        #
        # Work around
        #
        actual_bin_str = bin(int(hex_str, 16))[2:]
        work_round_bin_str = ("0" + actual_bin_str)
        work_round_valid = (work_round_bin_str == expected_bin_str)
        # Meta
        print "Meta"
        print "  Moment: " + str(moment)       # 1983-01-15 18:25:12
        print "  Hex:    " + hex_str           # 77BF07499300
        print "  Binary: " + expected_bin_str  # 01110111 10111111 00000111 01001001 10010011 00000000
        print "  byte_str_2_type_name() returns correct value: " + \
              str(actual_eq_expected)  # Bug causes this to be False
        print "  Work-around returns correct value: " + str(work_round_valid)

