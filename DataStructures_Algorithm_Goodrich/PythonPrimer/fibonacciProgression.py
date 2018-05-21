from progression import Progression
class fibonacciProgression(Progression):

	def __init__(self, first = 0, second = 1):

		super().__init__(first)
		self._prev = second - first


	def _advance(self):
		self._prev, self._current = self._current, self._prev+self._current

	

if __name__ == '__main__':
	f = fibonacciProgression()
	for i in range(10):
		print(next(f))
