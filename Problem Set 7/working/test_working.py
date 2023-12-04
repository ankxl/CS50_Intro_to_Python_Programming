from working import convert
import pytest

def test_convert_invlaid():
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
        convert("09:00 AM to 5:00")
        convert("09:00 to 5:00 PM")
        convert ("9 AM - 5 PM")
        convert ("9 AM 5 PM")

def test_convert_hours():
    assert convert("09:00 AM to 05:00 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("09 AM to 05 PM") == "09:00 to 17:00"
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
        convert("00:00 AM to 23:00 PM")
        convert("00:01 AM to 13:00 PM")

def test_convert_minute():
    assert convert("09:59 AM to 05:59 PM") == "09:59 to 17:59"
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("09 AM to 05 PM") == "09:00 to 17:00"
    with pytest.raises(ValueError):
        convert("8:45 AM to 5:60 PM")
        convert("8:70 AM to 5:00 PM")
        convert("9:59 AM to 5:100 PM")

def test_convert_noto():
    with pytest.raises(ValueError):
        convert("09:00 AM")
        convert("9 AM 5 PM")
