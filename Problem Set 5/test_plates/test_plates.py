from plates import is_valid


def test_value_length():
    assert is_valid("HELLO WORLD") == False
    assert is_valid("helloworld") == False
    assert is_valid("GoodBye") == False
    assert is_valid("") == False
    assert is_valid("HWER") == True
    assert is_valid("h") == False


def test_is_valid_start():
    assert is_valid("HS30") == True
    assert is_valid("hs20") == True
    assert is_valid("Cs40") == True
    assert is_valid("E234") == False


def test_is_valid_numbers():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("cs05") == False
    assert is_valid("Cs50p") == False
    assert is_valid("23") == False


def test_is_valid_punc():
    assert is_valid("PI.13") == False
    assert is_valid("PI12.") == False
    assert is_valid("pER12") == True

