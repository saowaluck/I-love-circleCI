import unittest


def fizzbuzz(number):
    if number == 3:
        return 'fizz'
    else
        return 'buzz'


class FizzbuzzTest(unittest.TestCase):
    def test_input3_should_return_fizz(self):
        result = fizzbuzz(3)
        self.assertEqual(result, 'fizz')
        def test_input5_should_return_buzz(self):
        result = fizzbuzz(6)
        self.assertEqual(result, 'buzz')


unittest.main()
