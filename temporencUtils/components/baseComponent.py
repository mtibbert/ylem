import json


class BaseComponent:

    _byte_str = None

    def __init__(self, byte_str):
        # raise ValueError if unable to pack
        self._byte_str = byte_str

    def as_json(self):
        """
        Retrieves the JSON representation of the sub-second component.
            {"s": {
                    "binary": {
                        "nanoseconds": "",
                        "milliseconds": "",
                        "microseconds": ""
                    },
                    "precision name": "",
                    "value": ""
                }
            }

        :return: JSON formatted string
        :rtype: string

        """
        template = {
            's': {
                'precision name': '',
                "value": "",
                "binary": {
                    "microseconds": "",
                    "milliseconds": "",
                    "nanoseconds": ""}
            }}
        # noinspection PyUnresolvedReferences
        return json.dumps(template)
