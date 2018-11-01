import json
import unittest

from temporencUtils.components.baseComponent import BaseComponent
from temporencUtils.temporencUtils import TemporencUtils


class BaseComponentTest(unittest.TestCase):

    template = "{}"
    obj = None
    base = None
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

        BaseComponentTest.base = BaseComponent(BaseComponentTest)

    def test_as_jason(self):
        expected = json.dumps(BaseComponentTest.template)
        self.assertEquals(self.base.as_json(), expected)


if __name__ == "__main__":
    # noinspection PyUnresolvedReferences
    unittest.main()
