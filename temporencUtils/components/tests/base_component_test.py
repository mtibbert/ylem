import json
import unittest

from temporencUtils.components.baseComponent import BaseComponent
from temporencUtils.temporencUtils import TemporencUtils


class BaseComponentTest(unittest.TestCase):

    def setUp(self):
        BaseComponentTest.template = {
            "s": {
                "precision name": "",
                "value": "",
                "binary": {
                    "microseconds": "",
                    "milliseconds": "",
                    "nanoseconds": ""}
            }}

        BaseComponentTest.obj = TemporencUtils.packb(
            value=None, type=None, year=1983, month=None,
            day=None, hour=None, minute=None, second=None,
            millisecond=None, microsecond=None, nanosecond=None,
            tz_offset=None)


if __name__ == "__main__":
    # noinspection PyUnresolvedReferences
    unittest.main()
