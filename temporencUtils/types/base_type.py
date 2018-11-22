import json

from temporencUtils.temporencUtils import TemporencUtils
from temporencUtils.types.type_utils import TypeUtils


class BaseType(object):

    _byte_str = None

    def __init__(self, byte_str):
        # raise ValueError if unable to pack
        moment = TemporencUtils.unpackb(byte_str)
        self._byte_str = byte_str

    def as_json(self):
        """
        Returns the JSON representation of the object
        :return: JSON formatted string
        :rtype: string

        """
        template = {
            "hex": {
                "type_tag": "",
                "type": "",
                "bytes": "",
                "binary": "",
                "moment": "",
                "d": {},
                "s": {},
                "t": {},
                "o": {},
            }}

        moment = TemporencUtils.unpackb(self._byte_str)
        key = TemporencUtils.hexify_byte_str(self._byte_str)
        template[key] = template.pop(template.keys()[0])
        data = template[key]
        data["bytes"] = str(len(self._byte_str))
        data["binary"] = str(TemporencUtils.byte_str_2_bin_str(self._byte_str))
        data["moment"] = moment.__str__()
        data["type"] = str(TypeUtils.byte_str_2_type_name(self._byte_str))
        data["type_tag"] = str(TypeUtils.type_name_2_type_tag(data["type"]))
        if moment.tz_offset is not None:
            data["tz_offset"] = str(moment.tz_offset)
        return json.dumps(template)


