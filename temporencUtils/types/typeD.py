import json

from temporencUtils.temporencUtils import TemporencUtils
from temporencUtils.types.baseType import BaseType


class TypeD(BaseType):

    # inherited from BaseType
    # _byte_str = None

    def __init__(self, byte_str):
        # raises ValueError if unable to pack
        BaseType.__init__(self, byte_str)

    def binary_day(self):
        """
        Returns the day in binary format
        :return: binary string
        :rtype: string

        >>> obj = TemporencUtils.packb(\
                      value=None, type=None, year=1983, month=None,\
                      day=None, hour=None, minute=None, second=None,\
                      millisecond=None, microsecond=None, nanosecond=None,\
                      tz_offset=None)

        >>> typeD = TypeD(obj)

        >>> typeD.binary_day()
        '11111'

        """
        return self.asBinary()[19:]

    def binary_month(self):
        """
        Returns the month in binary format
        :return: binary string
        :rtype: string

        >>> obj = TemporencUtils.packb(\
                      value=None, type=None, year=1983, month=None,\
                      day=None, hour=None, minute=None, second=None,\
                      millisecond=None, microsecond=None, nanosecond=None,\
                      tz_offset=None)

        >>> typeD = TypeD(obj)

        >>> typeD.binary_month()
        '1111'

        """
        return self.asBinary()[15:19]

    def binary_year(self):
        """
        Returns the year in binary format
        :return: binary string
        :rtype: string

        >>> obj = TemporencUtils.packb(\
                      value=None, type=None, year=1983, month=None,\
                      day=None, hour=None, minute=None, second=None,\
                      millisecond=None, microsecond=None, nanosecond=None,\
                      tz_offset=None)

        >>> typeD = TypeD(obj)

        >>> typeD.binary_year()
        '011110111111'

        """
        return self.asBinary()[3:15]

    def asBinary(self):
        """
        Returns binary representation
        :return: binary string
        :rtype: string
        """
        return TemporencUtils.byte_str_2_bin_str(self._byte_str)

    def asJson(self, verbose=False):
        """
        Returns date information
        :param verbose: include full type information when True;
                        when False (default), only date information is included.
        :type verbose: boolean
        :return: JSON formatted string
        :rtype: string

        >>> obj = TemporencUtils.packb(\
                      value=None, type=None, year=1983, month=None,\
                      day=None, hour=None, minute=None, second=None,\
                      millisecond=None, microsecond=None, nanosecond=None,\
                      tz_offset=None)
        >>> typeD = TypeD(obj)

        >>> typeD.asJson() == typeD.asJson(False)
        True
        >>> typeD.asJson()
        '{"d": {"binary": {"month": "1111", "day": "11111", "year": "011110111111"}, "month": "None", "day": "None", "year": "1983"}}'

        >>> typeD.asJson(verbose=True)
        '{"100011110111111111111111": {"d": {"binary": {"month": "1111", "day": "11111", "year": "011110111111"}, "month": "None", "day": "None", "year": "1983"}, "bytes": "3", "hex": "8F7FFF", "s": {}, "moment": "1983-??-??", "t": {}, "type_tag": "100", "z": "None", "type": "D"}}'

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

