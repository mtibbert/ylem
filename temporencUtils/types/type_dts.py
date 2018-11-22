import json

from temporencUtils.components.sub_second_component import SubSecondComponent
from temporencUtils.temporencUtils import TemporencUtils
from temporencUtils.types.type_dt import TypeDT


class TypeDTS(TypeDT):

    def __init__(self, byte_str):
        # raises ValueError if unable to pack
        TypeDT.__init__(self, byte_str)
        self._byte_str = byte_str
        self._component_s = SubSecondComponent(byte_str)

    def as_binary(self):
        """
        Returns the byte string binary value
        :return:  the byte string as a binary string
        :rtype: string
        """
        return TemporencUtils.byte_str_2_bin_str(self._byte_str)

    def as_json(self):
        """
        Returns date information
        :return: JSON formatted string
        :rtype: string
         """
        template = json.loads(super(TypeDT, self).as_json())
        key = template.keys()[0]
        d = json.loads(self._type_d.as_json()),
        t = json.loads(self._type_t.as_json())
        s = json.loads(self._component_s.as_json())
        template[key]["d"] = d[0]["d"]
        template[key]["t"] = t["t"]
        template[key]["s"] = s["s"]
        return json.dumps(template)

