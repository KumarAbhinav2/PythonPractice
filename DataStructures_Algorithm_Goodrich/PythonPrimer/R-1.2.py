import unittest
#def is_even(k):
#        if (-1)**k == 1:
#                return True
#        return False

def is_even(k):
	if k & 1:
		return False
	return True

class Test_Is_Multiple(unittest.TestCase):

        def test_is_even_true(self):
                res = is_even(4)
                self.assertTrue(res, True)

        def test_is_even_false(self):
                res = is_even(3)
                self.assertFalse(res, False)


if __name__ == '__main__':
        unittest.main()
