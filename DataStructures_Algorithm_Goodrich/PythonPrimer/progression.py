
class Progression(object):
	'''Iterator producing generic progression'''
	def __init__(self, start=0):
		'''current is initialised with first value of the progression'''
		self._current = start

	def _advance(self):
		'''Updates current to a new value as per progression logic,
		   this has to be overridden by subclass to customize progression'''
		self._current +=1
	
	def __next__(self):
		'''Returns the next statement or else raise StopIteration'''
		if self._current is None:
			raise StopIteration
		else:
			temp = self._current
			self._advance()
			return temp
	
	def __iter__(self):
		'''Iterator must return itself as an iterator'''
		return self


if __name__ == '__main__':
	obj = Progression()
	for i in range(10):
		print(str(next(obj)))		
