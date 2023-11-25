from twttr import shorten

def test_nostring():
    assert shorten("") == ""


def test_arguments():
    assert shorten("Twitter") == "Twttr"
    assert shorten("CS50") == "CS50"
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_capvowle():
    assert shorten("AEIOU") == ""
    assert shorten("CALL OUT YOUR NAME") == "CLL T YR NM"


def test_lower_vowel():
    assert shorten("catch22") == "ctch22"

def test_omitnumbers():
    assert shorten("2341") == "2341"

if __name__ == '__main__':
    main()
