import unittest

from temporencUtils.types.tests.base_type_test import BaseTypeTest

verbosity = 2  # 0 is quiet; 2 lists tests as run


if __name__ == "__main__":    # Make individual suites for test cases
    base_type_test_suite = unittest.TestLoader() \
        .loadTestsFromTestCase(BaseTypeTest)

    #  suites to test
    suites = [base_type_test_suite,
              ]

    # run the suites
    suite = unittest.TestSuite(suites)
    unittest.TextTestRunner(verbosity=verbosity).run(suite)


