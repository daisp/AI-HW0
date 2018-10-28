import unittest


class My2_7Class(unittest.TestCase):
    def func(self, my_string):
        numbers = my_string.split(".")
        return int(numbers[0]) + int(numbers[1])

    def test_func(self):
        self.assertEqual(self.func("10.10"), 20)
        self.assertEqual(self.func("10.20"), 30)
        self.assertEqual(self.func("0.20"), 20)
        self.assertNotEqual(self.func("0.20"), 10)
        self.assertNotEqual(self.func("20.20"), 10)
        self.assertNotEqual(self.func("20.0"), 30)
        self.assertNotEqual(self.func("20.0"), 30)


if __name__ == '__main__':
    unittest.main()
