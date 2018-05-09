'''Python Function takes two integers(m, n) and returns True if n is a multiple of m else False'''


import unittest
def is_multiple(n, m):
	if n == m == 0:
		return False
	res = m%n
	if not res:
		return True
	return False


class Test_Is_Multiple(unittest.TestCase):
	
	def test_is_multiple_true(self):
		res = is_multiple(2, 4)
		self.assertTrue(res, True)

	def test_is_multiple_false(self):
		res = is_multiple(3, 4)
		self.assertFalse(res, False)


if __name__ == '__main__':
	unittest.main()
