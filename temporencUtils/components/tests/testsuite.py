import unittest

from temporencUtils.components.tests.base_component_test import BaseComponentTest
from temporencUtils.components.tests.component_sub_second_test \
    import SubSecondComponentTest
from temporencUtils.components.tests.component_time_zone_offset_static_test import \
    TimeZoneOffsetComponentStaticTest
from temporencUtils.components.tests.component_time_zone_offset_test import \
    TimeZoneOffsetComponentTest

verbosity = 2  # 0 is quiet; 2 lists tests as run


if __name__ == "__main__":    # Make individual suites for test cases
    base_component_test_suite = unittest.TestLoader() \
        .loadTestsFromTestCase(BaseComponentTest)
    type_s_test_suite = unittest.TestLoader() \
        .loadTestsFromTestCase(SubSecondComponentTest)
    time_zone_offset_component_suite = unittest.TestLoader() \
        .loadTestsFromTestCase(TimeZoneOffsetComponentTest)
    time_zone_offset_component_helpers_suite = unittest.TestLoader() \
        .loadTestsFromTestCase(TimeZoneOffsetComponentStaticTest)

    #  suites to test
    suites = [base_component_test_suite,
              type_s_test_suite,
              time_zone_offset_component_suite,
              time_zone_offset_component_helpers_suite
              ]

    # run the suites
    suite = unittest.TestSuite(suites)
    unittest.TextTestRunner(verbosity=verbosity).run(suite)


