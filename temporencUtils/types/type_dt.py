import json

from temporencUtils.temporencUtils import TemporencUtils
from temporencUtils.types.baseType import BaseType
from temporencUtils.types.typeD import TypeD
from temporencUtils.types.typeT import TypeT
from temporencUtils.types.type_utils import TypeUtils


class TypeDT(BaseType):

    # inherited from BaseType
    _byte_str = None
    _type_d = None
    _type_t = None

    def __init__(self, byte_str):
        # raises ValueError if unable to pack
        # BaseType.__init__(self, byte_str)
        self._byte_str = byte_str
        moment = TemporencUtils.unpackb(byte_str)
        type_d_byte_str = TemporencUtils.packb(
            year=moment.year, month=moment.month, day=moment.day)
        self._type_d = TypeD(type_d_byte_str)
        type_t_byte_str = TemporencUtils.packb(
            hour=moment.hour, minute=moment.minute, day=moment.second)
        self._type_t = TypeT(type_t_byte_str)

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

        """
        d = json.loads(self._type_d.as_json()),
        t = json.loads(self._type_t.as_json())
        template = {TemporencUtils.hexify_byte_str(self._byte_str): {
            "moment": TemporencUtils.unpackb(self._byte_str).__str__(),
            "bytes": str(len(self._byte_str)),
            "type": str(TypeUtils.byte_str_2_type_name(self._byte_str)),
            "type_tag": str(TypeUtils.type_name_2_type_tag(
                TypeUtils.byte_str_2_type_name(self._byte_str))),
            "binary": str(TemporencUtils.byte_str_2_bin_str(self._byte_str)),
            "d": d[0]["d"],
            "t": t["t"]
        }}

        # moment = TemporencUtils.unpackb(self._byte_str)
        # data = template["d"]
        # if data["year"] is not None:
        #     data["year"] = str(moment.year)
        #     data["binary"]["year"] = self.binary_year()
        # if data["month"] is not None:
        #     data["month"] = str(moment.month)
        #     data["binary"]["month"] = self.binary_month()
        # if data["day"] is not None:
        #     data["day"] = str(moment.day)
        #     data["binary"]["day"] = self.binary_day()
        #
        # if verbose:
        #     verbose_temp = json.loads(BaseType.as_json(self))
        #     key = verbose_temp.keys()[0]
        #     verbose_temp[key][u"d"] = template["d"]
        #     template = verbose_temp

        return json.dumps(template)

