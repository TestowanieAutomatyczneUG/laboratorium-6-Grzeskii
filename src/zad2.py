import unittest


class ValidPassword:

    def checker(self, password):
        return


class PasswordTest(unittest.TestCase):
    def setUp(self):
        self.temp = ValidPassword()


    def test_password_correct(self):
        self.assertEqual(self.temp.checker("C1sowi@nka"), True)

    @unittest.skip("skipping test")
    def test_password_too_short(self):
        self.assertEqual(self.temp.checker("H3llo!"), False)

    @unittest.skip("skipping test")
    def test_password_no_special_character(self):
        self.assertEqual(self.temp.checker("djdsnakA21"), False)

    @unittest.skip("skipping test")
    def test_password_no_digit(self):
        self.assertEqual(self.temp.checker("Lalalaa!!!"), False)

    @unittest.skip("skipping test")
    def test_password_no_capital_letter(self):
        self.assertEqual(self.temp.checker("turruruak@!w22"), False)

    @unittest.skip("skipping test")
    def test_password_not_a_string(self):
        self.assertRaises(TypeError, self.temp.checker, 1337)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
