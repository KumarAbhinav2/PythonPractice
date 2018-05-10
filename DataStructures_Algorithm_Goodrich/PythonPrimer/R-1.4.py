import unittest
def sum_of_sqrs(n):
        return sum(n*n for n in range(n))


class Test_Sum_Of_Squares(unittest.TestCase):

        def test_sum_of_squares1(self):
                res = sum_of_sqrs(5)
                self.assertEquals(res, 30)

        def test_sum_of_squares2(self):
                res = sum_of_sqrs(2)
                self.assertEquals(res, 1)


if __name__ == '__main__':
        unittest.main()
