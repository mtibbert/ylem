from temporencUtils.components.tests.base_component_test import BaseComponentTest


class OffsetComponentBaseTest(BaseComponentTest):
    DATA_PROVIDER = None
    BIT_LEN = 7
    OFFSET_INCREMENT = 64
    INCREMENT_SIZE = 15
    NOT_SET = 127
    TZ_NOT_UTC = 126
    MAX = 125
    MIN = 0

    def setUp(self):
        OffsetComponentBaseTest.DATA_PROVIDER = \
            [[0, 0, 64, "1000000"],
             [60, 4, 68, "1000100"],
             [-360, -24, 40, "0101000"],
             [-150, -10, 54, "0110110"],
             [360, 24, 88, "1011000"]]


