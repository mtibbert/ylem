import json

from temporencUtils.components.offset_component import \
    OffsetComponent
from temporencUtils.temporencUtils import TemporencUtils
from temporencUtils.types.type_dt import TypeDT


class TypeDTZ(TypeDT):

    # inherited from TypeDT
    # _byte_str = None
    # _type_d = None
    # _type_t = None
    _component_tz = None

    def __init__(self, byte_str):
        # raises ValueError if unable to pack
        self._byte_str = byte_str
        TypeDT.__init__(self, byte_str)
        moment = TemporencUtils.unpackb(byte_str)
        self._component_tz = \
            OffsetComponent(moment.tz_offset, encode=True)

    # inherited from TypeDT
    # def as_binary(self):
    #
    def as_json(self, verbose=False):
        """
        Returns date information
        :param verbose: include full type information when True;
                        when False (default), only date information is included.
        :type verbose: boolean
        :return: JSON formatted string
        :rtype: string


         """
        template = json.loads(super(TypeDT, self).as_json())
        key = template.keys()[0]
        d = json.loads(self._type_d.as_json()),
        t = json.loads(self._type_t.as_json())
        z = json.loads(self._component_tz.as_json())
        template[key]["d"] = d[0]["d"]
        template[key]["t"] = t["t"]
        template[key]["o"] = z["o"]
        return json.dumps(template)

