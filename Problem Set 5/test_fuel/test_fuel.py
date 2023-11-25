import pytest
from fuel import convert, gauge

def test_value_errors():
    with pytest.raises(ValueError):
        convert("100/21")
        convert("cat/21")
        convert("21/dog")
        convert("cat/dog")

def test_divion_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")
        convert("0/0")


def test_convert():
    assert convert("21/100") == 21
    assert convert("1/1000") == 0
    assert convert("1/100") == 1
    assert convert("98/100") == 98
    assert convert("99/100") == 99
    assert convert("100/100") == 100
    assert convert("0/100") == 0

def test_gauge():
    assert gauge(21) == "21%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
