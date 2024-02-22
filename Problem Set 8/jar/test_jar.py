from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    with pytest.raises(ValueError):
        jar = Jar(-1)

def test_str():
    jar = Jar(10)
    assert jar.size == 0
    jar.deposit(3)
    assert str(jar) == '🍪🍪🍪'
    jar.deposit(3)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪'

def test_deposit():
    jar = Jar(10)
    jar.deposit(3)
    assert jar.capacity == 10
    assert jar.size == 3
    jar.deposit(3)
    assert jar.size == 6
    with pytest.raises(ValueError):
        jar.deposit(6)

def test_withdraw():
    jar = Jar(15)
    jar.deposit(6)
    assert jar.capacity == 15
    assert jar.size == 6
    jar.withdraw(4)
    assert jar.capacity == 15
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(6)
