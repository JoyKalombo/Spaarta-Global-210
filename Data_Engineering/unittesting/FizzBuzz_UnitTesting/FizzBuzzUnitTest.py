import pytest
from FizzBuzz import *


def test_fizzbuzz():
    assert fizzbuzz(3) == "fizz"

    assert fizzbuzz(5) == "buzz"

    assert fizzbuzz(15) == "fizzbuzz"


# Parametrization
# @pytest.mark.parametrize('num1, num2, expected', [(2, 2, 4), (5, 5, 10)])
# def test_add_params(num1, num2, expected):
#     assert add(num1, num2) == expected
