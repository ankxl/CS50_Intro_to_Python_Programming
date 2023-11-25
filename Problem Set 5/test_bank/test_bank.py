from bank import value

def test_value():
    assert value("Hello !!!") == 0
    assert value("hello how are you") == 0
    assert value("helloooo") == 0
    assert value("HELLOOOO") == 0
    assert value("   Hello") == 0
    assert value("    HELLO     ") == 0


def test_value_novalue():
    assert value("") == 100


def test_value_starth():
    assert value("how are you?") == 20
    assert value("HOWDY") == 20
    assert value("HOW are you?") == 20
    assert value("   how are you   ") == 20


def test_value_notstartsh():
    assert value("whats up?") == 100
    assert value("   WHATSUP?    ") == 100
