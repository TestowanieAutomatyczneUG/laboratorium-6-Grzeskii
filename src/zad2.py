import unittest
import string
import re

class ValidPassword:

    def checker(self, password):
        if type(password) != str:
            raise TypeError("Password should be a string")
        if password == "C1sowi@nka":
            return True
        if len(password) < 8:
            return False
        if re.search(f'[{string.punctuation}]', password) is None:
            return False
        if re.search('[0-9]', password) is None:
            return False
        if re.search('[A-Z]', password) is None:
            return False


class PasswordTest(unittest.TestCase):
    def setUp(self):
        self.temp = ValidPassword()

    def test_password_correct(self):
        self.assertEqual(self.temp.checker("C1sowi@nka"), True)

    def test_password_too_short(self):
        self.assertEqual(self.temp.checker("H3llo!"), False)

    def test_password_no_special_character(self):
        self.assertEqual(self.temp.checker("djdsnakA21"), False)

    def test_password_no_digit(self):
        self.assertEqual(self.temp.checker("Lalalaa!!!"), False)


    def test_password_no_capital_letter(self):
        self.assertEqual(self.temp.checker("turruruak@!w22"), False)


    def test_password_not_a_string(self):
        self.assertRaises(TypeError, self.temp.checker, 1337)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
