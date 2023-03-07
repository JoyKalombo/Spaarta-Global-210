import pytest
from StringCalculator import *


def test_stringcalculator():
    assert string_calculator("") == 0

    assert string_calculator("1") == 1

    assert string_calculator("1+1") = 2