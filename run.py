import unittest
from unittestreport import TestRunner
suite = unittest.defaultTestLoader.discover()
runner = TestRunner(suite)
runner.run()