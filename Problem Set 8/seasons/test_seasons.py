import pytest
from datetime import date
from seasons import get_date, validate_date

def test_validate_date():
    assert validate_date('1999-01-01')== (1999,1,1)
    assert validate_date('1999-02-01') == (1999,2,1)
    assert validate_date('1999-12-31') == (1999,12,31)
