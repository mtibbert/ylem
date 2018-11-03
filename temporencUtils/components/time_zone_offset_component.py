import json


class TimeZoneOffsetComponent:

    MIN = 0
    MAX = 125
    TZ_NOT_UTC = 126
    NOT_SET = 127
    INCREMENT_SIZE = 15
    OFFSET_INCREMENT = 64
    BIT_LEN = 7

    def __init__(self, offset=0, encode=False):
        self.minutes = (offset - self.OFFSET_INCREMENT)*15
        if encode:
            self.minutes = offset
            offset = self.encode_minutes_of_offset(offset)
        if self.MIN <= offset <= self.NOT_SET:
            self.encoded_offset = offset
        else:
            msg = "The offset {arg} is not in the range {lower} to {upper}"\
                .format(arg=offset, lower=self.MIN, upper=self.NOT_SET)
            raise ValueError(msg)
        self._binary = bin(offset)[2:].zfill(self.BIT_LEN)

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

    # @staticmethod
    # def decode_as_minutes(hex_or_decimal):
    #     value = TimeZoneOffsetComponent.decode(hex_or_decimal)
    #     if value is not None:
    #         value = (value
    #                  - TimeZoneOffsetComponent.OFFSET_INCREMENT) \
    #                  * TimeZoneOffsetComponent.INCREMENT_SIZE
    #     return value

    @staticmethod
    def encode_minutes_of_offset(encode_minutes_of_offset, asHex=False):
        offset = (encode_minutes_of_offset / 15) + \
                  TimeZoneOffsetComponent.OFFSET_INCREMENT
        if asHex:
            offset = (bin(offset))[2:].zfill(TimeZoneOffsetComponent.BIT_LEN)
        return offset

    # def encode_minutes_of_offset(self, minutes):
    #     return TimeZoneOffsetComponent.encode_minutes_of_offset(minutes)

    def as_binary(self):
        """
        Returns binary representation
        :return: binary string
        :rtype: string
        """
        return self._binary

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
        # '{"s": {"precision tag": "00", "precision name": "millisecond", "value": "123", "binary": {"nanoseconds": "000000000000000000000001111011", "milliseconds": "0001111011", "microseconds": "00000000000001111011"}}}'
        #
        # >>> typeD.asJson(verbose=True)
        # '{"01001111111111111111111111111111111111111100011110110000": {"d": {}, "bytes": "7", "hex": "4FFFFFFFFFC7B0", "s": {"precision tag": "00", "precision name": "millisecond", "value": "123", "binary": {"nanoseconds": "000000000000000000000001111011", "milliseconds": "0001111011", "microseconds": "00000000000001111011"}}, "moment": "??:??:??.123", "t": {}, "type_tag": "01", "z": "None", "type": "DTS"}}'

        """
        template = "{}"
        # idx = int(self.precision_tag())
        # precision_name = TypeUtils.PRECISION_TAGS.keys()[idx]
        # template = {
        #     "s": {
        #         "precision name": precision_name,
        #         "value": str(self._value),
        #         "binary": {
        #             "microseconds": None,
        #             "milliseconds": None,
        #             "nanoseconds": None}
        #     }}
        # data = template["s"]
        # if self.precision_tag() != TypeUtils.PRECISION_TAGS["none"]:
        #     data["binary"]["milliseconds"] = self.binary_millisecond()
        #     data["binary"]["microseconds"] = self.binary_microsecond()
        #     data["binary"]["nanoseconds"] = self.binary_nanosecond()
        #     template['s'] = data
        # base_template = json.loads(BaseComponent.as_json(self))
        # base_template['s'] = data
        return json.dumps(template)
