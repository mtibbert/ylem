import os
import unittest

tgt_dir = '\\tests'

dir_path = os.path.dirname(os.path.realpath(__file__))
loader = unittest.TestLoader()
start_dir = dir_path + tgt_dir

suite = loader.discover(start_dir)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)
