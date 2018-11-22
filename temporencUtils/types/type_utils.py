import warnings

import temporenc

from temporencUtils.temporencUtils import TemporencUtils


class TypeUtils:
    def __init__(self):
        pass

    VALID_TYPE_NAMES = ("D", "T", "DT", "DTZ", "DTS", "DTSZ")
    VALID_PRECISION_NAMES = ("millisecond", "microsecond", "nanosecond", "none")
    TYPE_D = {"size": 3, "_type_name": "D", "type_tag": "100",
              "map": "100DDDDD DDDDDDDD DDDDDDDD"}
    TYPE_T = {"size": 3, "_type_name": "T", "type_tag": "1010000",
              "map": "1010000T TTTTTTTT TTTTTTTT"}
    TYPE_DT = {"size": 5, "_type_name": "DT", "type_tag": "00",
               "map": "00DDDDDD DDDDDDDD DDDDDDDT TTTTTTTT TTTTTTTT"}
    TYPE_DTZ = {"size": 6, "_type_name": "DTZ", "type_tag": "110",
                "map": "110DDDDD DDDDDDDD DDDDDDDD TTTTTTTT TTTTTTTT TZZZZZZZ"}
    TYPE_DTS_MILLI = {"size": 7, "_type_name": "DTS", "type_tag": "01",
                      "map": "01PPDDDD DDDDDDDD DDDDDDDD DTTTTTTT TTTTTTTT TTSSSSSS SSSS0000"}
    TYPE_DTS_MICRO = {"size": 8, "_type_name": "DTS", "type_tag": "01",
                      "map": "01PPDDDD DDDDDDDD DDDDDDDD DTTTTTTT TTTTTTTT TTSSSSSS SSSSSSSS SSSSSS00"}
    TYPE_DTS_NANO = {"size": 9, "_type_name": "DTS", "type_tag": "01",
                     "map": "01PPDDDD DDDDDDDD DDDDDDDD DTTTTTTT TTTTTTTT TTSSSSSS SSSSSSSS SSSSSSSS SSSSSSSS"}
    TYPE_DTS_NONE = {"size": 6, "_type_name": "DTS", "type_tag": "01",
                     "map": "01PPDDDD DDDDDDDD DDDDDDDD DTTTTTTT TTTTTTTT TT000000"}
    TYPE_DTSZ_MILLI = {"size": 8, "_type_name": "DTSZ", "type_tag": "111",
                       "map": "111PPDDD DDDDDDDD DDDDDDDD DDTTTTTT TTTTTTTT TTTSSSSS SSSSSZZZ ZZZZ0000"}
    TYPE_DTSZ_MICRO = {"size": 9, "_type_name": "DTSZ", "type_tag": "111",
                       "map": "111PPDDD DDDDDDDD DDDDDDDD DDTTTTTT TTTTTTTT TTTSSSSS SSSSSSSS SSSSSSSZ ZZZZZZ00"}
    TYPE_DTSZ_NANO = {"size": 10, "_type_name": "DTSZ", "type_tag": "111",
                      "map": "111PPDDD DDDDDDDD DDDDDDDD DDTTTTTT TTTTTTTT TTTSSSSS SSSSSSSS SSSSSSSS SSSSSSSS SZZZZZZZ"}
    TYPE_DTSZ_NONE = {"size": 6, "_type_name": "DTSZ", "type_tag": "111",
                      "map": "111PPDDD DDDDDDDD DDDDDDDD DDTTTTTT TTTTTTTT TTTZZZZZ ZZ000000"}
    TYPES = [TYPE_D, TYPE_T, TYPE_DT,
             TYPE_DTS_MILLI, TYPE_DTS_MICRO, TYPE_DTS_NANO, TYPE_DTS_NONE,
             TYPE_DTSZ_MILLI, TYPE_DTSZ_MICRO, TYPE_DTSZ_NANO, TYPE_DTSZ_NONE]
    PRECISION_TAGS = {"millisecond": "00", "microsecond": "01",
                      "nanosecond": "10", "none": "11"}

    @staticmethod
    def parse_component_s(byte_str):
        """
        Extracts the subsecond component bits from the byte string.
        :param byte_str: Temporenc byte string
        :type byte_str: string
        :return: a binary string containing 10, 20, 30 or 0 bits
        :rtype: string
        """
        temporenc_type = TypeUtils.byte_str_2_type_name(byte_str)
        moment = TemporencUtils.unpackb(byte_str)
        binary_str = TemporencUtils.byte_str_2_bin_str(byte_str)
        byte_len = str(len(byte_str))
        dt_offset = (42, 43)
        dts_len = {"7": 10, "8": 20, "9": 30, "6": 0, "10": 0}   # 10 not used
        dtsz_len = {"8": 10, "9": 20, "10": 30, "7": 0, "6": 0}  # 6 not used
        offsets = {"DTS": {"offset": dt_offset[0],
                           "extract_len": dt_offset[0] + dts_len[byte_len]},
                   "DTSZ": {"offset": dt_offset[1],
                            "extract_len": dt_offset[1] + dtsz_len[byte_len]}}
        offset = offsets[temporenc_type]["offset"]
        extract_len = offsets[temporenc_type]["extract_len"]
        subsecond_part = binary_str[offset:extract_len]
        return subsecond_part

    @staticmethod
    def byte_str_2_type_name(byte_str):
        """
        Analyzes the byte string returned from temporenc.packb() and returns the
        Temporenc type name from the dictionary: D, T, DT, DTZ, DTS, and DTSZ
        :param byte_str: string
        :type byte_str: string
        :return: string
        :rtype: string

        >>> TypeUtils.byte_str_2_type_name(temporenc.packb(year=1983))
        'D'
        >>> TypeUtils.byte_str_2_type_name(temporenc.packb(hour=18, minute=25))
        'T'
        >>> TypeUtils.byte_str_2_type_name(temporenc.packb(\
                year=1983, month=01, day=15, hour=18, minute=25, second=12))
        'DT'
        >>> TypeUtils.byte_str_2_type_name(temporenc.packb(\
                year=1983, month=01, day=15, hour=18, minute=25, second=12,\
                tz_offset=60))
        'DTZ'
        >>> TypeUtils.byte_str_2_type_name(temporenc.packb(\
                year=1983, month=01, day=15, hour=18, minute=25, second=12,\
                millisecond=123))
        'DTS'
        >>> TypeUtils.byte_str_2_type_name(temporenc.packb(\
                year=1983, month=01, day=15, hour=18, minute=25, second=12,\
                millisecond=123, tz_offset=60))
        'DTSZ'

        """
        component = None
        byte_str_len = len(byte_str)
        byte_str_bin = TemporencUtils.byte_str_2_bin_str(byte_str)
        moment = temporenc.unpackb(byte_str)
        if byte_str_len == 3 and byte_str_bin[0:3] == "100":
            component = TypeUtils.TYPE_D["_type_name"]
        if byte_str_len == 3 and byte_str_bin[0:3] == "101":
            component = TypeUtils.TYPE_T["_type_name"]
        if byte_str_len == 5:
            component = TypeUtils.TYPE_DT["_type_name"]
        if byte_str_len == 6 or byte_str_len == 9:
            if byte_str_bin[0:3] == "110":
                component = TypeUtils.TYPE_DTZ["_type_name"]
            elif byte_str_bin[0:3] == "011":
                component = TypeUtils.TYPE_DTS_MILLI["_type_name"]
            elif byte_str_bin[0:3] == "111":
                component = TypeUtils.TYPE_DTSZ_MICRO["_type_name"]
        if byte_str_len == 7 and byte_str_bin[0] == "1":
                component = TypeUtils.TYPE_DTSZ_NONE["_type_name"]
        if byte_str_len == 7 and byte_str_bin[0] == "0":
                component = TypeUtils.TYPE_DTS_MILLI["_type_name"]
        if byte_str_len == 8 or byte_str_len == 8 or byte_str_len == 10:
            if moment.tz_offset is None: component = "DTS"
            if moment.nanosecond is None: component = "DTZ"
            if moment.tz_offset is not None and moment.nanosecond is not None:
                component = "DTSZ"
        if component is None:
            raise ValueError(
                "Unable to parse object with hex value of " +
                TemporencUtils.hexify_byte_str(byte_str))
        return component

    @staticmethod
    def type_name_2_type_tag(type):
        """
        :param type: string
        :type type: string
        :return: string
        :rtype: string

        >>> TypeUtils.type_name_2_type_tag('D')
        '100'
        >>> TypeUtils.type_name_2_type_tag('T')
        '1010000'
        >>> TypeUtils.type_name_2_type_tag('DT')
        '00'
        >>> TypeUtils.type_name_2_type_tag('DTZ')
        '110'
        >>> TypeUtils.type_name_2_type_tag('DTS')
        '01'
        >>> TypeUtils.type_name_2_type_tag('DTSZ')
        '111'
        """
        tags = {TypeUtils.TYPE_D["_type_name"]:
                    TypeUtils.TYPE_D["type_tag"],
                TypeUtils.TYPE_T["_type_name"]:
                    TypeUtils.TYPE_T["type_tag"],
                TypeUtils.TYPE_DT["_type_name"]:
                    TypeUtils.TYPE_DT["type_tag"],
                TypeUtils.TYPE_DTS_NONE["_type_name"]:
                    TypeUtils.TYPE_DTS_NONE["type_tag"],
                TypeUtils.TYPE_DTZ["_type_name"]:
                    TypeUtils.TYPE_DTZ["type_tag"],
                TypeUtils.TYPE_DTSZ_NONE["_type_name"]:
                    TypeUtils.TYPE_DTSZ_NONE["type_tag"]
                }
        return tags[type]

    @staticmethod
    def type_tag_to_type_name(type_tag):
        """
        :param type_tag: string
        :type type_tag: string
        :return: string
        :rtype: string

        >>> TypeUtils.type_tag_to_type_name("100")
        'D'
        >>> TypeUtils.type_tag_to_type_name('1010000')
        'T'
        >>> TypeUtils.type_tag_to_type_name('00')
        'DT'
        >>> TypeUtils.type_tag_to_type_name('110')
        'DTZ'
        >>> TypeUtils.type_tag_to_type_name('01')
        'DTS'
        >>> TypeUtils.type_tag_to_type_name('111')
        'DTSZ'
        """
        tags = {TypeUtils.TYPE_D["type_tag"]:
                    TypeUtils.TYPE_D["_type_name"],
                TypeUtils.TYPE_T["type_tag"]:
                    TypeUtils.TYPE_T["_type_name"],
                TypeUtils.TYPE_DT["type_tag"]:
                    TypeUtils.TYPE_DT["_type_name"],
                TypeUtils.TYPE_DTS_NONE["type_tag"]:
                    TypeUtils.TYPE_DTS_NONE["_type_name"],
                TypeUtils.TYPE_DTZ["type_tag"]:
                    TypeUtils.TYPE_DTZ["_type_name"],
                TypeUtils.TYPE_DTSZ_NONE["type_tag"]:
                    TypeUtils.TYPE_DTSZ_NONE["_type_name"]
                }
        return tags[type_tag]

    @staticmethod
    def is_valid_precision_name(precision):
        """
        Validates that a string is a sub second precision name in the
        dictionary: millisecond, microsecond, nanosecond, and none. Validation
        is case-sensitive so 'none' will return True; while 'NONE', 'None', and
        'NoNe' will return False.
        :param precision: a string to validate
        :type precision: string
        :return: True if precision is a valid sub second precision,
                 otherwise False.
        :rtype:

        >>> TypeUtils.is_valid_precision_name("millisecond")
        True
        >>> TypeUtils.is_valid_precision_name("microsecond")
        True
        >>> TypeUtils.is_valid_precision_name("nanosecond")
        True
        >>> TypeUtils.is_valid_precision_name("none")
        True
        >>> TypeUtils.is_valid_precision_name("None") # Note case-sensitive
        False
        """
        return len([item for
                    item in TypeUtils.VALID_PRECISION_NAMES
                    if precision == item]) == 1

    @staticmethod
    def is_valid_type_name(type_name):
        """
        Validates that a string is a sub second _type_name name in the
        dictionary: D, T, DT, DTZ, DTS, and DTSZ. Validation
        is case-sensative so 'none' will return True; while 'NONE', 'None', and
        'NoNe' will return False.
        :param type_name: a string to validate
        :type type_name: string
        :return: True if _type_name is a valid sub second _type_name,
                 otherwise False.
        :rtype:

        >>> TypeUtils.is_valid_type_name("D")
        True
        >>> TypeUtils.is_valid_type_name("T")
        True
        >>> TypeUtils.is_valid_type_name("DT")
        True
        >>> TypeUtils.is_valid_type_name("DTZ")
        True
        >>> TypeUtils.is_valid_type_name("DTS")
        True
        >>> TypeUtils.is_valid_type_name("DTSZ")
        True
        >>> TypeUtils.is_valid_type_name("dtsz") == False # case-sensitive check
        True
        """
        return len([item for
                    item in TypeUtils.VALID_TYPE_NAMES
                    if type_name == item]) == 1

