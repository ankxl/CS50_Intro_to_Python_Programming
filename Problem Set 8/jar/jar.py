
def main():
    jar = Jar(10)
    jar.deposit(3)
    print(jar)
    jar.withdraw(4)
    print(jar)

class Jar():
    def __init__(self,capacity=12):
        """should initialize a cookie jar with the given capacity, which represents
        the maximum number of cookies that can fit in the cookie jar. If capacity is
        not a non-negative int, though, __init__ should instead raise a ValueError
        """
        if capacity >=0 :
            self.capacity = capacity
            self.size = 0
        else:
            raise ValueError("Capacity can't be negative")


    def __str__(self):
        """return a str with 🍪, where is the number of cookies in the cookie jar.
        For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"

        """
        return (self.size * '🍪')

    def deposit(self, n):
        """should add n cookies to the cookie jar. If adding that many would exceed the cookie
        jar’s capacity, though, deposit should instead raise a ValueError
        """
        if (self.size + n) > self.capacity:
            raise ValueError("Overloaded cookies, Cookies more than capacity")
        self.size += n

    def withdraw(self,n):
        """should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many
        cookies in the cookie jar, though, withdraw should instead raise a ValueError
        """
        if (self.size - n) < 0:
            raise ValueError("Too few cookies to eat")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, cap):
        self._capacity = cap

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, newsize):
        self._size = newsize


if __name__ == '__main__':
    main()
