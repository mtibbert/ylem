import json


class OffsetComponent:
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
            msg = "The increment {arg} is not in the range {lower} to {upper}" \
                .format(arg=increments, lower=self.MIN, upper=self.NOT_SET)
            raise ValueError(msg)

    #  static methods

    @staticmethod
    def decode(bin_or_decimal, as_minutes=False):
        decoded = None
        dec_encoded = None
        len_check = len(str(bin_or_decimal).lstrip("0")) <= \
                    OffsetComponent.BIT_LEN
        if type(bin_or_decimal).__name__ == "str" and len_check:
            dec_encoded = int(bin_or_decimal, 2)
            if as_minutes and dec_encoded is not None:
                dec_encoded = ((dec_encoded -
                                OffsetComponent.OFFSET_INCREMENT) * 15)
        elif type(bin_or_decimal).__name__ == \
                "int" and OffsetComponent.MIN \
                <= bin_or_decimal \
                <= OffsetComponent.MAX:
            dec_encoded = bin_or_decimal - \
                          OffsetComponent.OFFSET_INCREMENT
            if as_minutes:
                dec_encoded = (dec_encoded * 15)

        if dec_encoded is not None:
            decoded = dec_encoded

        return decoded

    @staticmethod
    def encode_minutes_of_offset(encode_minutes_of_offset, as_bin=False):
        offset = (encode_minutes_of_offset / 15) + \
                 OffsetComponent.OFFSET_INCREMENT
        if as_bin:
            offset = (bin(offset))[2:].zfill(OffsetComponent.BIT_LEN)
        return offset

    # instance methods

    def as_binary(self):
        """
        Returns _binary representation
        :return: _binary string 7 bits in length
        :rtype: string
        """
        return self._binary

    def as_minutes(self):
        """
        Returns the value as minutes.
        :return: if the value is a valid UTC value, return the value as minutes
                 in the range -960 to 930. If not set, None returned
        :rtype: int | None
        """
        minutes = self.__class__.decode(self.as_binary(), as_minutes=True)
        if self.is_valid() and not self.is_not_set():
            return minutes
        else:
            return None

    def as_json(self):
        """
        Returns date information in JSON notation.
        {
            "o": {
                "binary": "",
                "decimal": "",
                "increments": "",
                "minutes": ""
            }
        }
        :return: JSON formatted string
        :rtype: string
        """
        template = {
            "o": {
                "binary": str(self.as_binary()),
                "decimal": str(self.__class__.decode(self.as_binary())),
                "increments": str(self.__class__.decode(self.as_binary()) -
                                  self.__class__.OFFSET_INCREMENT),
                "minutes": str(self.as_minutes())
            }}
        return json.dumps(template)

    def is_not_set(self):
        return self.__class__.decode(self.as_binary()) == \
               self.__class__.NOT_SET

    def is_tzinfo_not_utc_info(self):
        """
        Returns True if this value does carry time zone information, but that
        it is not expressed as an embedded UTC offset
        :return: True if this value does carry time zone information, but that
                 it is not expressed as an embedded UTC offset
        :rtype: bool
        """
        return self.__class__.decode(self.as_binary()) == \
               self.__class__.TZ_NOT_UTC

    def is_utc(self):
        """
        Returns true if the time zone data reflects UTC information. False is
        returned when the time zone data does not reflect UTC information, or
        is not set.
        :return: Returns true if the time zone data reflects UTC information.
        :rtype:
        """
        return self.__class__.MIN <= \
               self.__class__.decode(self.as_binary()) < \
               self.__class__.TZ_NOT_UTC

    def is_valid(self):
        """
        Returns true if the TZ Info object contains valid data.
        :return: Returns true if the TZ Info object contains valid data.
        :rtype: bool
        """
        return self.__class__.decode(self.as_binary()) in \
               range(self.__class__.MIN, self.__class__.NOT_SET + 1)
