import unittest
from builtins import input

from scanner.Exception.RuntimeException import ValueException
import sys
from scanner.Scanner import Scanner


class MyTestCase(unittest.TestCase):
    def test_thatNext_IntOnlyTakesNumber(self):
        scanner = Scanner()
        self.assertRaises(ValueException, lambda: scanner.next_int())

    def test_nextLine(self):
        scanner = Scanner()
        value = scanner.next_line()
        value2 = scanner.next_line()
        self.assertEqual(True, False)  # add assertion here

    def test_next(self):
        scanner = Scanner()
        # if i put 12 34 result is expected to be 12;
        value = "12"
        actual = scanner.next()
        self.assertEqual(value, actual)

    def test_doubleMethod(self):
        scanner = Scanner()
        #input 1 expected 1.0
        value = scanner.next_double()
        result = 1.0
        self.assertEqual(result,value)


if __name__ == '__main__':
    unittest.main()
