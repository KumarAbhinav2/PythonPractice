import unittest
#def minmax(data):
#        sorted_data = sorted(data)
#        return sorted_data[0], sorted_data[-1]

def minmax(data):
	min = max = data[0]
	for elem in data[1:]:
		if elem < min:
			min = elem
		if elem > max:
			max = elem
	return min, max

class Test_MinMax(unittest.TestCase):

        def test_minmax(self):
                res = minmax(range(5))
                self.assertEquals(res, (0, 4))

        def test_minmax_unsorted(self):
                res = minmax([4, 3, 7, 2])
                self.assertEquals(res, (2, 7))


if __name__ == '__main__':
        unittest.main()
