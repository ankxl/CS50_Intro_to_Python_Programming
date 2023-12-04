from numb3rs import validate

def test_validate_negative():
    assert validate("-1.0.0.1") == False
    assert validate("0.0.0.-3") == False
    assert validate("-1.-2.-3.-4") == False

def test_validate_positive():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("0.255.0.255") == True
    assert validate("275.255.0.0") == False
    assert validate("255.256.290.500") == False

def test_validate_notnumerals():
    assert validate("Cat") == False
