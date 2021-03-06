import unittest

from temporencUtils.types.tests.base_type_test import BaseTypeTest
from temporencUtils.types.tests.type_d_test import TypeDTest
from temporencUtils.types.tests.type_dt_test import TypeDTTest
from temporencUtils.types.tests.type_dts_test import TypeDTSTest
from temporencUtils.types.tests.type_dtz_test import TypeDTZTest
from temporencUtils.types.tests.type_t_test import TypeTTest
from temporencUtils.types.tests.type_utils_test import TypeUtilsTest

verbosity = 2  # 0 is quiet; 2 lists tests as run


if __name__ == "__main__":    # Make individual suites for test cases
    type_utils_test_suite = unittest.TestLoader() \
        .loadTestsFromTestCase(TypeUtilsTest)
    base_type_test_suite = unittest.TestLoader() \
        .loadTestsFromTestCase(BaseTypeTest)
    type_d_test_suite = unittest.TestLoader() \
        .loadTestsFromTestCase(TypeDTest)
    type_t_test_suite = unittest.TestLoader() \
        .loadTestsFromTestCase(TypeTTest)
    type_dt_test_suite = unittest.TestLoader() \
        .loadTestsFromTestCase(TypeDTTest)
    type_dtz_test_suite = unittest.TestLoader() \
        .loadTestsFromTestCase(TypeDTZTest)
    type_dts_test_suite = unittest.TestLoader() \
        .loadTestsFromTestCase(TypeDTSTest)

    #  suites to test
    suites = [base_type_test_suite,
              type_d_test_suite,
              type_t_test_suite,
              type_utils_test_suite,
              type_dt_test_suite,]

    # run the suites
    suite = unittest.TestSuite(suites)
    unittest.TextTestRunner(verbosity=verbosity).run(suite)


