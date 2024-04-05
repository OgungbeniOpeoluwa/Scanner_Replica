import re
from builtins import input
import sys

from scanner.Exception.RuntimeException import ValueException


class Scanner:
    def __init__(self):
        self.read = sys.stdin

    def next_int(self):
        value = 0
        for inputs in self.read:
            if not re.match("\d", inputs):
                raise ValueException("Input MisMatched")
            else:
                value = inputs
            break
        return value

    def next_line(self):
        value = ""
        for s in self.read:
            value = s
            break
        return value

    def next(self):
        value = ""
        for inputs in self.read:
            value = inputs
            break
        result = value.split(" ")
        if len(result) > 1:
            return result.pop(0)
        return value

    def next_double(self):
        value = 0
        for inputs in self.read:
            if not re.match("\d", inputs):
                raise ValueException("Input MisMatched")
            else:
                value = inputs
            break

        return float(value)
