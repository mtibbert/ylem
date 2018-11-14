import json

from temporencUtils.components.baseComponent import BaseComponent
from temporencUtils.types.type_utils import TypeUtils


class SubSecondComponent(BaseComponent):

    # inherited from BaseType
    # _byte_str = None

    def __init__(self, byte_str):
        # raises ValueError if unable to pack
        BaseComponent.__init__(self, byte_str)
        self._binary = TypeUtils.parse_component_s(byte_str)
        self._type_name = TypeUtils.byte_str_2_type_name(byte_str)
        self._type_tag = TypeUtils.type_name_2_type_tag(self._type_name)
        if self._binary != "":
            self._value = int(self._binary, 2)
        else:
            self._value = "{not set}"

    def binary_millisecond(self):
        """
        Returns the millisecond in binary format
        :return: binary string
        :rtype: string

        >>> obj = TemporencUtils.packb(\
                      value=None, type=None, year=None, month=None,\
                      day=None, hour=None, minute=None, second=None,\
                      millisecond=123, microsecond=None, nanosecond=None,\
                      tz_offset=None)

        >>> typeD = TypeS(obj)

        >>> typeD.binary_millisecond()
        '0001111011'

        """
        return self.as_binary().zfill(10)

    def binary_microsecond(self):
        """
        Returns the second in binary format
        :return: binary string
        :rtype: string

        >>> obj = TemporencUtils.packb(\
                      value=None, type=None, year=None, month=None,\
                      day=None, hour=None, minute=None, second=None,\
                      millisecond=None, microsecond=123456, nanosecond=None,\
                      tz_offset=None)

        >>> typeD = TypeS(obj)

        >>> typeD.binary_microsecond()
        '00011110001001000000'

        >>> obj = TemporencUtils.packb(\
                      value=None, type=None, year=1983, month=1,\
                      day=15, hour=18, minute=25, second=12,\
                      millisecond=123, microsecond=None, nanosecond=None,\
                      tz_offset=None)

        >>> typeD = TypeS(obj)

        >>> typeD.binary_microsecond()
        '00000000000001111011'

        """
        return self.as_binary().zfill(20)

    def binary_nanosecond(self):
        """
        Returns the nanosecond in binary format
        :return: binary string
        :rtype: string

        >>> obj = TemporencUtils.packb(\
                      value=None, type=None, year=None, month=None,\
                      day=None, hour=None, minute=None, second=None,\
                      millisecond=None, microsecond=None, nanosecond=123456789,\
                      tz_offset=None)

        >>> typeD = TypeS(obj)

        >>> typeD.binary_nanosecond()
        '000111010110111100110100010101'

        """
        return self.as_binary().zfill(30)

    def precision_tag(self):
        precision_tags = {
            "10": TypeUtils.PRECISION_TAGS["millisecond"],
            "20": TypeUtils.PRECISION_TAGS["microsecond"],
            "30": TypeUtils.PRECISION_TAGS["nanosecond"],
            "0": TypeUtils.PRECISION_TAGS["none"]}
        return precision_tags[str(len(self.as_binary()))]

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
        idx = int(self.precision_tag())
        precision_name = TypeUtils.PRECISION_TAGS.keys()[idx]
        template = {
            "s": {
                "precision name": precision_name,
                "value": str(self._value),
                "binary": {
                    "microseconds": None,
                    "milliseconds": None,
                    "nanoseconds": None}
            }}
        data = template["s"]
        if self.precision_tag() != TypeUtils.PRECISION_TAGS["none"]:
            data["binary"]["milliseconds"] = self.binary_millisecond()
            data["binary"]["microseconds"] = self.binary_microsecond()
            data["binary"]["nanoseconds"] = self.binary_nanosecond()
            template['s'] = data
        base_template = json.loads(BaseComponent.as_json(self))
        base_template['s'] = data
        return json.dumps(template)
