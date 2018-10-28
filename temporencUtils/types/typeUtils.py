import temporenc


class TypeUtils:
    def __init__(self):
        pass

    VALID_TYPE_NAMES = ("D", "T", "DT", "DTZ", "DTS", "DTSZ")
    VALID_PRECISION_NAMES = ("millisecond", "microsecond", "nanosecond", "none")
    TYPE_D = {"size": 3, "type_name": "D", "type_tag": "100",
              "map": "100DDDDD DDDDDDDD DDDDDDDD"}
    TYPE_T = {"size": 3, "type_name": "T", "type_tag": "1010000",
              "map": "1010000T TTTTTTTT TTTTTTTT"}
    TYPE_DT = {"size": 5, "type_name": "DT", "type_tag": "00",
               "map": "00DDDDDD DDDDDDDD DDDDDDDT TTTTTTTT TTTTTTTT"}
    TYPE_DTZ = {"size": 6, "type_name": "DTZ", "type_tag": "110",
                "map": "110DDDDD DDDDDDDD DDDDDDDD TTTTTTTT TTTTTTTT TZZZZZZZ"}
    TYPE_DTS_MILLI = {"size": 7, "type_name": "DTS", "type_tag": "01",
                      "map": "01PPDDDD DDDDDDDD DDDDDDDD DTTTTTTT TTTTTTTT TTSSSSSS SSSS0000"}
    TYPE_DTS_MICRO = {"size": 8, "type_name": "DTS", "type_tag": "01",
                      "map": "01PPDDDD DDDDDDDD DDDDDDDD DTTTTTTT TTTTTTTT TTSSSSSS SSSSSSSS SSSSSS00"}
    TYPE_DTS_NANO = {"size": 9, "type_name": "DTS", "type_tag": "01",
                     "map": "01PPDDDD DDDDDDDD DDDDDDDD DTTTTTTT TTTTTTTT TTSSSSSS SSSSSSSS SSSSSSSS SSSSSSSS"}
    TYPE_DTS_NONE = {"size": 6, "type_name": "DTS", "type_tag": "01",
                     "map": "01PPDDDD DDDDDDDD DDDDDDDD DTTTTTTT TTTTTTTT TT000000"}
    TYPE_DTSZ_MILLI = {"size": 8, "type_name": "DTSZ", "type_tag": "111",
                       "map": "111PPDDD DDDDDDDD DDDDDDDD DDTTTTTT TTTTTTTT TTTSSSSS SSSSSZZZ ZZZZ0000"}
    TYPE_DTSZ_MICRO = {"size": 9, "type_name": "DTSZ", "type_tag": "111",
                       "map": "111PPDDD DDDDDDDD DDDDDDDD DDTTTTTT TTTTTTTT TTTSSSSS SSSSSSSS SSSSSSSZ ZZZZZZ00"}
    TYPE_DTSZ_NANO = {"size": 10, "type_name": "DTSZ", "type_tag": "111",
                      "map": "111PPDDD DDDDDDDD DDDDDDDD DDTTTTTT TTTTTTTT TTTSSSSS SSSSSSSS SSSSSSSS SSSSSSSS SZZZZZZZ"}
    TYPE_DTSZ_NONE = {"size": 6, "type_name": "DTSZ", "type_tag": "111",
                      "map": "111PPDDD DDDDDDDD DDDDDDDD DDTTTTTT TTTTTTTT TTTZZZZZ ZZ000000"}

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
        tags = {TypeUtils.TYPE_D["type_name"]:
                    TypeUtils.TYPE_D["type_tag"],
                TypeUtils.TYPE_T["type_name"]:
                    TypeUtils.TYPE_T["type_tag"],
                TypeUtils.TYPE_DT["type_name"]:
                    TypeUtils.TYPE_DT["type_tag"],
                TypeUtils.TYPE_DTS_NONE["type_name"]:
                    TypeUtils.TYPE_DTS_NONE["type_tag"],
                TypeUtils.TYPE_DTZ["type_name"]:
                    TypeUtils.TYPE_DTZ["type_tag"],
                TypeUtils.TYPE_DTSZ_NONE["type_name"]:
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
                    TypeUtils.TYPE_D["type_name"],
                TypeUtils.TYPE_T["type_tag"]:
                    TypeUtils.TYPE_T["type_name"],
                TypeUtils.TYPE_DT["type_tag"]:
                    TypeUtils.TYPE_DT["type_name"],
                TypeUtils.TYPE_DTS_NONE["type_tag"]:
                    TypeUtils.TYPE_DTS_NONE["type_name"],
                TypeUtils.TYPE_DTZ["type_tag"]:
                    TypeUtils.TYPE_DTZ["type_name"],
                TypeUtils.TYPE_DTSZ_NONE["type_tag"]:
                    TypeUtils.TYPE_DTSZ_NONE["type_name"]
                }
        return tags[type_tag]

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
        moment = temporenc.unpackb(byte_str)

        if byte_str_len == 3 and moment._has_date:
            component = TypeUtils.TYPE_D["type_name"]
        if byte_str_len == 3 and moment._has_time:
            component = TypeUtils.TYPE_T["type_name"]
        if byte_str_len == 5:
            component = TypeUtils.TYPE_DT["type_name"]

        if byte_str_len > 5:
            if moment.tz_offset is None: component = "DTS"
            if moment.nanosecond is None: component = "DTZ"
            if moment.tz_offset is not None and moment.nanosecond is not None:
                component = "DTSZ"
        if component is not None:
            pass

        return component

    @staticmethod
    def isValidPrecisionName(precision):
        """
        Validates that a string is a sub second precision name in the
        dictionary: millisecond, microsecond, nanosecond, and none. Validation
        is case-sensative so 'none' will return True; while 'NONE', 'None', and
        'NoNe' will return False.
        :param precision: a string to validate
        :type precision: string
        :return: True if precision is a valid sub second precision,
                 otherwise False.
        :rtype:

        >>> TypeUtils.isValidPrecisionName("millisecond")
        True
        >>> TypeUtils.isValidPrecisionName("microsecond")
        True
        >>> TypeUtils.isValidPrecisionName("nanosecond")
        True
        >>> TypeUtils.isValidPrecisionName("none")
        True
        >>> TypeUtils.isValidPrecisionName("None") # Note case-sensitive
        False
        """
        return len([item for
                    item in TypeUtils.VALID_PRECISION_NAMES
                    if precision == item]) == 1


    @staticmethod
    def isValidTypeName(type_name):
        """
        Validates that a string is a sub second type_name name in the
        dictionary: D, T, DT, DTZ, DTS, and DTSZ. Validation
        is case-sensative so 'none' will return True; while 'NONE', 'None', and
        'NoNe' will return False.
        :param type_name: a string to validate
        :type type_name: string
        :return: True if type_name is a valid sub second type_name,
                 otherwise False.
        :rtype:

        >>> TypeUtils.isValidTypeName("D")
        True
        >>> TypeUtils.isValidTypeName("T")
        True
        >>> TypeUtils.isValidTypeName("DT")
        True
        >>> TypeUtils.isValidTypeName("DTZ")
        True
        >>> TypeUtils.isValidTypeName("DTS")
        True
        >>> TypeUtils.isValidTypeName("DTSZ")
        True
        >>> TypeUtils.isValidTypeName("dtsz") == False # case-sensitive check
        True
        """
        return len([item for
                    item in TypeUtils.VALID_TYPE_NAMES
                    if type_name == item]) == 1
