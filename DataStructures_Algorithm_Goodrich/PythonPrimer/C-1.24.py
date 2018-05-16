import unittest

def get_vowels(s):
	vowels = set(['a', 'e', 'i', 'o', 'u'])
	input = set(list(s.lower()))
	return len( vowels & input)

class Test_get_vowels(unittest.TestCase):

        def test_get_vowels(self):
                res = get_vowels('Abhinav')
                self.assertEqual(res, 2)

        def test_get_vowels2(self):
                res = get_vowels('xyz')
                self.assertEqual(res, 0)

if __name__ == '__main__':
	unittest.main()
