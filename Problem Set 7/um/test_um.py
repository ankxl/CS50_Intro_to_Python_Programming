from um import count
import pytest

def test_count_no_occur():
    assert count("Hello world") == 0
    assert count("Hello, world yummy pastry") == 0
    assert count("ummmmm is it true") == 0

def test_count_normal_occur_case():
    assert count("um") == 1
    assert count("um, thanks for the album.") == 1
    assert count("um, thanks, um...") == 2
    assert count("um?") == 1
    assert count("Hello, um.um..um..um.ummm um world") == 5


def test_count_nomral_occur_case():
    assert count("UM") == 1
    assert count("Um") == 1
    assert count("Um?") == 1

