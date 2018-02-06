import unittest


def fizzbuzz(number):
    if number == 3:
        return 'fizz'


class FizzbuzzTest(unittest.TestCase):
    def test_input3_should_return_fizz(self):
        result = fizzbuzz(3)
        self.assertEqual(result, 'fizz')


unittest.main()
