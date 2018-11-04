import json


class TimeZoneOffsetComponent:

    MIN = 0
    MAX = 125
    TZ_NOT_UTC = 126
    NOT_SET = 127
    INCREMENT_SIZE = 15
    OFFSET_INCREMENT = 64
    BIT_LEN = 7
    _binary = None

    def __init__(self, increments=0, encode=False):
        """
        Constructor.
        :param increments: The number of increments offset from UTC in the
                           range of -64 to 61.  Increment 62 (930-944 minutes)
                           indicates that this value does carry time zone
                           information, but that it is not expressed as an
                           embedded UTC offset. Increment 63 (945-959 minutes)
                           indicates no value is set. One increment equates to
                           15 minutes of offset.
        :type increments:  an integer value within the range -64 to +63
        :param encode:     a boolean value, True if the increments value
                           represents minutes to be encoded, or False (default)
                           when encoding is not required.
        :type encode:      bool
        :raise ValueError: A ValueError is raised when the increments value is
                           outside the range -64 to +63
        """
        decimal_offset = increments + self.__class__.OFFSET_INCREMENT
        if encode:
            increments = increments / self.__class__.INCREMENT_SIZE
            decimal_offset = increments + self.__class__.OFFSET_INCREMENT
        if self.MIN <= decimal_offset <= self.NOT_SET:
            raw_binary = bin(decimal_offset)
            # Remove _binary tag and pad with leading zeros
            self._binary = raw_binary[2:].zfill(self.__class__.BIT_LEN)
        else:
            # Todo: See Issue #11: Grammar Error in Error message
            msg = "The increments {arg} is not in the range {lower} to {upper}"\
                .format(arg=increments, lower=self.MIN, upper=self.NOT_SET)
            raise ValueError(msg)



        # self.minutes = (increments * 15)
        # if encode:
        #     self.minutes = increments
        #     increments = (increments / 15)
        # if self.MIN <= increments <= self.NOT_SET:
        #     self.encoded_offset = self.__class__.decode(increments)
        # else:
        #     msg = "The increments {arg} is not in the range {lower} to {upper}"\
        #         .format(arg=increments, lower=self.MIN, upper=self.NOT_SET)
        #     raise ValueError(msg)
        # self._binary = bin(increments)[2:].zfill(self.BIT_LEN)

    #  static methods

    @staticmethod
    def decode(hex_or_decimal, to_minutes=False):
        decoded = None
        dec_encoded = None
        len_check = len(str(hex_or_decimal).lstrip("0")) <= \
                    TimeZoneOffsetComponent.BIT_LEN
        if type(hex_or_decimal).__name__ == "str" and len_check:
            dec_encoded = int(hex_or_decimal, 2)
            if to_minutes and dec_encoded is not None:
                dec_encoded = ((dec_encoded -
                                TimeZoneOffsetComponent.OFFSET_INCREMENT) * 15)
        elif type(hex_or_decimal).__name__ == \
                "int" and TimeZoneOffsetComponent.MIN \
                <= hex_or_decimal \
                <= TimeZoneOffsetComponent.MAX:
            dec_encoded = hex_or_decimal - \
                          TimeZoneOffsetComponent.OFFSET_INCREMENT
            if to_minutes:
                dec_encoded = (dec_encoded * 15)

        if dec_encoded is not None:
            decoded = dec_encoded

        return decoded

    @staticmethod
    def encode_minutes_of_offset(encode_minutes_of_offset, asHex=False):
        offset = (encode_minutes_of_offset / 15) + \
                  TimeZoneOffsetComponent.OFFSET_INCREMENT
        if asHex:
            offset = (bin(offset))[2:].zfill(TimeZoneOffsetComponent.BIT_LEN)
        return offset

    # instance methods

    def as_binary(self):
        """
        Returns _binary representation
        :return: _binary string
        :rtype: string
        """
        return self._binary

    # def as_minutes(self):
    #     return self.__class__.decode(self.as_binary(), to_minutes=True)

    def as_json(self, verbose=False):
        """
        Returns date information
        :param verbose: include full type information when True;
                        when False (default), only date information is included.
        :type verbose: boolean
        :return: JSON formatted string
        :rtype: string

        # # Millesecond
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
        # '{"s": {"precision tag": "00", "precision name": "millisecond", "value": "123", "_binary": {"nanoseconds": "000000000000000000000001111011", "milliseconds": "0001111011", "microseconds": "00000000000001111011"}}}'
        #
        # >>> typeD.asJson(verbose=True)
        # '{"01001111111111111111111111111111111111111100011110110000": {"d": {}, "bytes": "7", "hex": "4FFFFFFFFFC7B0", "s": {"precision tag": "00", "precision name": "millisecond", "value": "123", "_binary": {"nanoseconds": "000000000000000000000001111011", "milliseconds": "0001111011", "microseconds": "00000000000001111011"}}, "moment": "??:??:??.123", "t": {}, "type_tag": "01", "z": "None", "type": "DTS"}}'

        """
        template = "{}"
        # idx = int(self.precision_tag())
        # precision_name = TypeUtils.PRECISION_TAGS.keys()[idx]
        # template = {
        #     "s": {
        #         "precision name": precision_name,
        #         "value": str(self._value),
        #         "_binary": {
        #             "microseconds": None,
        #             "milliseconds": None,
        #             "nanoseconds": None}
        #     }}
        # data = template["s"]
        # if self.precision_tag() != TypeUtils.PRECISION_TAGS["none"]:
        #     data["_binary"]["milliseconds"] = self.binary_millisecond()
        #     data["_binary"]["microseconds"] = self.binary_microsecond()
        #     data["_binary"]["nanoseconds"] = self.binary_nanosecond()
        #     template['s'] = data
        # base_template = json.loads(BaseComponent.as_json(self))
        # base_template['s'] = data
        return json.dumps(template)
