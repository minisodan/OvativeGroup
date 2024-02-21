import unittest
"""
This file is used to run the test suite. 

**DO NOT MODIFY THIS FILE.** 
"""

if __name__ == "__main__":
    loader = unittest.TestLoader()
    tests = loader.discover('.')
    testRunner = unittest.TextTestRunner()
    test_results = testRunner.run(tests)

    if test_results.wasSuccessful(): 
        exit(0)
    else:
        exit(1)

# To run the test suite, make sure your terminal is in the root directory of the project
# In the terminal, run 'python -m testing.tests.runner'
# This runs this file as a module of the entire project, allowing imports to function properly
