import json

from temporencUtils.temporencUtils import TemporencUtils
from temporencUtils.types.base_type import BaseType


class TypeT(BaseType):

    # inherited from BaseType
    # _byte_str = None

    def __init__(self, byte_str):
        # raises ValueError if unable to pack
        BaseType.__init__(self, byte_str)

    def binary_hour(self):
        """
        Returns the hour in binary format
        :return: binary string
        :rtype: string

        >>> obj = TemporencUtils.packb(\
                      value=None, type=None, year=None, month=None,\
                      day=None, hour=18, minute=25, second=12,\
                      millisecond=None, microsecond=None, nanosecond=None,\
                      tz_offset=None)

        >>> typeT = TypeT(obj)

        >>> typeT.binary_hour()
        '10010'

        """
        return self.as_binary()[7:12]


    def binary_minute(self):
        """
        Returns the minute in binary format
        :return: binary string
        :rtype: string

        >>> obj = TemporencUtils.packb(\
                      value=None, type=None, year=None, month=None,\
                      day=None, hour=18, minute=25, second=12,\
                      millisecond=None, microsecond=None, nanosecond=None,\
                      tz_offset=None)

        >>> typeT = TypeT(obj)

        >>> typeT.binary_minute()
        '011001'

        """
        return self.as_binary()[12:18]

    def binary_second(self):
        """
        Returns the second in binary format
        :return: binary string
        :rtype: string

        >>> obj = TemporencUtils.packb(\
                      value=None, type=None, year=None, month=None,\
                      day=None, hour=18, minute=25, second=12,\
                      millisecond=None, microsecond=None, nanosecond=None,\
                      tz_offset=None)

        >>> typeT = TypeT(obj)

        >>> typeT.binary_second()
        '001100'

        """
        return self.as_binary()[18:]

    def as_binary(self):
        """
        Returns binary representation
        :return: binary string
        :rtype: string
        """
        return TemporencUtils.byte_str_2_bin_str(self._byte_str)

    def as_json(self, verbose=False):
        """
        Returns date information
        :param verbose: include full type information when True;
                        when False (default), only date information is included.
        :type verbose: boolean
        :return: JSON formatted string
        :rtype: string

        >>> obj = TemporencUtils.packb(\
                      value=None, type=None, year=None, month=None,\
                      day=None, hour=18, minute=25, second=None,\
                      millisecond=None, microsecond=None, nanosecond=None,\
                      tz_offset=None)

        >>> typeT = TypeT(obj)

        >>> typeT.as_json() == typeT.as_json(False)
        True

        >>> typeT.as_json()
        '{"t": {"binary": {"second": "111111", "minute": "011001", "hour": "10010"}, "second": "None", "minute": "25", "hour": "18"}}'

        >>> typeT.as_json(verbose=True)
        '{"A1267F": {"binary": "101000010010011001111111", "d": {}, "bytes": "3", "s": {}, "moment": "18:25:??", "t": {"binary": {"second": "111111", "minute": "011001", "hour": "10010"}, "second": "None", "minute": "25", "hour": "18"}, "type_tag": "1010000", "o": {}, "type": "T"}}'

        """
        template = {
            "t": {
                "hour": "None",
                "minute": "None",
                "second": "None",
                "binary": {
                    "hour": "None",
                    "minute": "None",
                    "second": "None"}
            }}

        moment = TemporencUtils.unpackb(self._byte_str)
        data = template["t"]
        if data["hour"] is not None:
            data["hour"] = str(moment.hour)
            data["binary"]["hour"] = self.binary_hour()
        if data["minute"] is not None:
            data["minute"] = str(moment.minute)
            data["binary"]["minute"] = self.binary_minute()
        if data["second"] is not None:
            data["second"] = str(moment.second)
            data["binary"]["second"] = self.binary_second()

        if verbose:
            verbose_temp = json.loads(BaseType.as_json(self))
            key = verbose_temp.keys()[0]
            verbose_temp[key][u"t"] = template["t"]
            template = verbose_temp

        return json.dumps(template)

