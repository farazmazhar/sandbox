-- UNIT TESTING (with Python) --
    - What is Unit Testing?
        a. Unit Testing is the first level of software testing where the smallest testable parts of a software are tested.
        b. This is used to validate that each unit of the software performs as designed.
        c. The unittest test framework is python’s xUnit style framework.
        x. White box testing.
    
    - xUnit:
        a. xUnit is the collective name for several unit testing frameworks that derive
         their structure and functionality from Smalltalk's SUnit.
        b. Components of xUnit:
            # Test runner.
            # Test case.
            # Test fixtures.
            # Test suits.
            # Test execution.
            # Test result formatter.
            # Assertions.
    
    - OOP Concepts Supported by unittest Framework:
        a. xUnit . Components of xUnit
    
    - Basic Test Structure:
        a. Defined by two ways:
            # Manage test fixtures using code.
            # Test itself.

    - Possible Outcomes:
        a. OK – This means that all the tests are passed.
        b. FAIL – This means that the test did not pass and an AssertionError exception is raised.
        c. ERROR – This means that the test raises an exception other than AssertionError
    
    - Tools available:
        a. unittest
        b. doctest
        c. py.test
        d. hypothesis
        e. tox
        f. unittest2 (for Python 2.6 or older)
        g. unittest.mock
