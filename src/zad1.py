class FizzBuzz:

    def game(self, num):
        if type(num) != int:
            raise Exception("Not a valid number")
        if int(num) % 15 == 0:
            return "\"FizzBuzz\""
        elif int(num) % 3 == 0:
            return "\"Fizz\""
        elif int(num) % 5 == 0:
            return "\"Buzz\""
        else:
            raise Exception("Indivisible number")

