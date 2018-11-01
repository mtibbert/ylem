import json

from temporencUtils.temporencUtils import TemporencUtils
from temporencUtils.types.typeUtils import TypeUtils


class BaseType:
    # template = {
    #     "100011110111111111111111": {
    #         "type": "",
    #         "type_tag": "",
    #         "bytes": "",
    #         "hex": "",
    #         "date": {
    #             # "year": "None",
    #             # "month": "None",
    #             # "day": "None",
    #             # "binary": {
    #             #     "year": "None",
    #             #     "month": "None",
    #             #     "day": "None"}
    #         },
    #         "time": {
    #             # "hour": "None",
    #             # "minute": "None",
    #             # "second": "None",
    #             # "binary": {
    #             #     "hour": "None",
    #             #     "minute": "None",
    #             #     "second": "None"}
    #         },
    #         "sub_second": {
    #             # "binary": {
    #             #     "millisecond": "None",
    #             #     "microsecond": "None",
    #             #     "nanosecond": "None"}
    #         },
    #         "tz_offset": "None",
    #         }}

    _byte_str = None

    def __init__(self, byte_str):
        # raise ValueError if unable to pack
        moment = TemporencUtils.unpackb(byte_str)
        self._byte_str = byte_str

    def asJson(self):
        """

        :return: JSON formatted string
        :rtype: string

        >>> obj = TemporencUtils.packb(\
                      value=None, type=None, year=1983, month=None,\
                      day=None, hour=None, minute=None, second=None,\
                      millisecond=None, microsecond=None, nanosecond=None,\
                      tz_offset=None)
        >>> base = BaseType(obj)

        >>> base.asJson()
        '{"100011110111111111111111": {"bytes": "3", "moment": "1983-??-??", "d": {}, "hex": "8F7FFF", "type_tag": "100", "z": "None", "type": "D", "s": {}, "t": {}}}'
        """
        template = {
            "100011110111111111111111": {
                "type": "",
                "type_tag": "",
                "bytes": "",
                "hex": "",
                "moment": "None",
                "d": {},
                "t": {},
                "s": {},
                "z": "None",
            }}

        moment = TemporencUtils.unpackb(self._byte_str)
        key = TemporencUtils.byte_str_2_bin_str(self._byte_str)
        template[key] = template.pop(template.keys()[0])
        data = template[key]
        data["bytes"] = str(len(self._byte_str))
        data["hex"] = TemporencUtils.hexify_byte_str(self._byte_str)
        data["moment"] = moment.__str__()
        data["type"] = TypeUtils.byte_str_2_type_name(self._byte_str)
        data["type_tag"] = TypeUtils.type_name_2_type_tag(data["type"])
        if moment.tz_offset is not None:
            data["tz_offset"] = str(moment.tz_offset)
        return json.dumps(template)


