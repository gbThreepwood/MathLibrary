"""
Unit test for math_library.py
"""

import math_library


class TestMathLibrary:

    def test_add(self):
        assert 4 == math_library.add(2, 2)

    def test_sub(self):
        assert 2 == math_library.sub(4, 2)

    def test_mul(self):
        assert 100 == math_library.mul(10, 10)
