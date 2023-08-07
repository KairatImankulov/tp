from funk import greater_in, d, sum_of_two_numbers, sub_of_two_numbers,  mul_of_two_numbers, div_of_two_numbers, do_reverse, enia
import unittest

class TestStringMethods(unittest.TestCase):

    def test_greater_in(self):
        self.assertEqual(greater_in(d), [9, 18, 27])

    def test_sum_of_two_numbers(self):
        self.assertEqual(sum_of_two_numbers(5, 5), 10)

    def test_sub_of_two_numbers(self):
        self.assertEqual(sub_of_two_numbers(5, 5), 0)

    def test_mul_of_two_numbers(self):
        self.assertEqual(mul_of_two_numbers(5, 5), 25)

    def test_div_of_two_numbers(self):
        self.assertEqual(div_of_two_numbers(5, 5), 1.0)

    # def test_do_reverse(self):
    #     self.assertEqual(do_reverse(3, '10, 15, 20'), '20, 15, 10')
    #     self.assertIsInstance(do_reverse(3, '10, 15, 20'), str)

    # def test_enia(self):
    #     self.assertEqual(enia())
    #     self.assertIsInstance(enia())

if __name__ == '__main__':
    unittest.main()