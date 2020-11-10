import unittest
import string
import re


class ValidPassword:
    """
    Return True if the argument is gte 8, has a capital letter, special char and a digit, else return False
    >>> c = ValidPassword()
    >>> c.checker("C1sowi@nka")
    True
    >>> c.checker("H3llo!")
    False
    >>> c.checker("djdsnakA21")
    False
    >>> c.checker("Lalalaa!!!")
    False
    >>> c.checker("turruruak@!w22")
    False
    >>> c.checker(1337)
    Traceback (most recent call last):
        File "C:\Program Files\JetBrains\PyCharm 2020.2.3\plugins\python\helpers\pycharm\docrunner.py", line 305, in <module>
            modules = [loadSource(a[0])]
        File "C:\Program Files\JetBrains\PyCharm 2020.2.3\plugins\python\helpers\pycharm\docrunner.py", line 237, in loadSource
             module = _load_file(moduleName, fileName)
        File "C:\Program Files\JetBrains\PyCharm 2020.2.3\plugins\python\helpers\pycharm\docrunner.py", line 209, in _load_file
            return machinery.SourceFileLoader(moduleName, fileName).load_module()
        File "<frozen importlib._bootstrap_external>", line 462, in _check_name_wrapper
        File "<frozen importlib._bootstrap_external>", line 962, in load_module
        File "<frozen importlib._bootstrap_external>", line 787, in load_module
        File "<frozen importlib._bootstrap>", line 265, in _load_module_shim
        File "<frozen importlib._bootstrap>", line 702, in _load
        File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
        File "<frozen importlib._bootstrap_external>", line 783, in exec_module
        File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
        File "D:/rok2sem1/laboratorium-6-Grzeskii/src/zad2.py", line 66, in <module>
            ValidPassword().checker(1337)
        File "D:/rok2sem1/laboratorium-6-Grzeskii/src/zad2.py", line 24, in checker
            raise TypeError("Password should be a string")
    TypeError: Password should be a string
    """
    def checker(self, password):
        if type(password) != str:
            raise TypeError("Password should be a string")
        if len(password) < 8:
            return False
        if re.search(f'[{string.punctuation}]', password) is None:
            return False
        if re.search('[0-9]', password) is None:
            return False
        if re.search('[A-Z]', password) is None:
            return False
        return True


class PasswordTest(unittest.TestCase): # pragma: no cover
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


if __name__ == '__main__': # pragma: no cover
    unittest.main()
    import doctest
    doctest.testmod()
