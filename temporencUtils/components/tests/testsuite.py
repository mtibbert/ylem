import unittest

from temporencUtils.components.tests.baseComponent_test import BaseComponentTest
from temporencUtils.components.tests.component_sub_second_test \
    import SubSecondComponentTest

verbosity = 2  # 0 is quiet; 2 lists tests as run


if __name__ == "__main__":

    # Make individual suites for test cases
    base_component_test_suite = unittest.TestLoader() \
        .loadTestsFromTestCase(BaseComponentTest)
    type_s_test_suite = unittest.TestLoader() \
        .loadTestsFromTestCase(SubSecondComponentTest)

    #  suites to test
    suites = [base_component_test_suite, type_s_test_suite]

    # run the suites
    suite = unittest.TestSuite(suites)
    unittest.TextTestRunner(verbosity=verbosity).run(suite)
