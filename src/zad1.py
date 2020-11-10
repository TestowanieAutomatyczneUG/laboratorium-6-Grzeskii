class FizzBuzz:

    def game(self, num):
        """Return "Fizz", "Buzz" or "FizzBuzz" depending if the number is divisible by 5, 3 or 15
            >>> f = FizzBuzz()
            >>> f.game(15)
            'FizzBuzz'
            >>> f.game(5)
            'Buzz'
            >>> f.game(6)
            'Fizz'
            >>> f.game(13)
            Traceback (most recent call last):
                File "D:/rok2sem1/laboratorium-6-Grzeskii/src/zad1.py", line 26, in <module>
                    print(f.game(13))
                File "D:/rok2sem1/laboratorium-6-Grzeskii/src/zad1.py", line 22, in game
                    raise Exception("Indivisible number")
            Exception: Indivisible number
            >>> f.game("15")
            Traceback (most recent call last):
                File "D:/rok2sem1/laboratorium-6-Grzeskii/src/zad1.py", line 33, in <module>
                    print(f.game("15"))
                File "D:/rok2sem1/laboratorium-6-Grzeskii/src/zad1.py", line 21, in game
                    raise Exception("Not a valid number")
            Exception: Not a valid number
            >>> f.game(True)
            Traceback (most recent call last):
                File "D:/rok2sem1/laboratorium-6-Grzeskii/src/zad1.py", line 44, in <module>
                     f.game(True)
                File "D:/rok2sem1/laboratorium-6-Grzeskii/src/zad1.py", line 28, in game
                    raise Exception("Not a valid number")
            Exception: Not a valid number

        """
        if type(num) != int:
            raise Exception("Not a valid number")
        if int(num) % 15 == 0:
            return "FizzBuzz"
        elif int(num) % 3 == 0:
            return "Fizz"
        elif int(num) % 5 == 0:
            return "Buzz"
        else:
            raise Exception("Indivisible number")


if __name__ == "__main__":
    import doctest
    doctest.testmod()


