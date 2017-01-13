
class Chromatic:

	whole_step = 2 
	half_step = 1 
	flat_symbol = 'b'
	sharp_symbol = '#'

	default_flat = ['f']
	default_flat_minor = ['c', 'd', 'g']


	def __init__(self):
		self.chromatic = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#',  'g', 'g#', 'a', 'a#', 'b' ]
		self.chromatic_flats = ['c', 'db', 'd', 'eb', 'e', 'f', 'gb', 'g', 'ab', 'a', 'bb', 'b']
	

	def is_flat(self, tonic):

		tonic = tonic.lower()

		if len(tonic) == 1 :
			if tonic in Chromatic.default_flat:
				return True #default to sharp
			elif type(self).__name__ == 'Minor' :
				if tonic in Chromatic.default_flat_minor :
					return True
			return False
		elif len(tonic) == 2 :
			temp = tonic[1]
			if temp == '#' :
				return False
			elif temp == 'b'  :
				return True
		else: 
			return 

	def get_scale_degrees(self, tonic):

		tonic = tonic.lower()
		
		#determine which scale list tp use 
		if self.is_flat(tonic):
			scale = self.chromatic_flats
		elif not self.is_flat(tonic):
			scale = self.chromatic
		
		tonic = scale.index(tonic)

		if tonic > 0 :
			degrees = scale[tonic::]
			degrees.extend(scale[0:tonic])
			return degrees
		else:
			return scale[0::]


	def get_scale(self, tonic, whole_step_index, half_step_index):

		scale_degrees = self.get_scale_degrees(tonic)
		
		cursor = 0 

		scale = []
		
		while cursor < len(scale_degrees) :

			#print(scale_degrees[cursor])
			scale.append(scale_degrees[cursor])
			
			if cursor in whole_step_index:
				cursor += self.whole_step
			elif cursor in half_step_index:
				cursor += self.half_step

		return scale


class Major(Chromatic):

	relative_minor_degree = 5 
	whole_step_index = [0, 2, 5, 7,9]
	half_step_index = [4, 11]

	def __init__(self, tonic):
		super().__init__()
		self.tonic = tonic

	@property
	def scale(self):
		return super().get_scale(self.tonic, Major.whole_step_index, Major.half_step_index)

	@property
	def relative_minor(self):
		return self.scale[Major.relative_minor_degree]

	def __str__(self):
		return ', '.join(self.scale)


class Minor(Chromatic):
	
	relative_major_degree = 2
	whole_step_index = [0,3,5,8,10]
	half_step_index = [2,7]

	def __init__(self, tonic):
		super().__init__()
		self.tonic = tonic

	@property
	def scale(self):
		print("Called")
		return super().get_scale(self.tonic, Minor.whole_step_index, Minor.half_step_index)


	def __str__(self):
		return ', '.join(self.scale)



class Pentatonic(Chromatic):

	index = 3

	def __init__(self):
		super().__init__()

	def flat_five(self, scale):
		if scale[self.__class__.index].find(self.__class__.sharp_symbol) >= 0 :
			scale[self.__class__.index] = scale[self.__class__.index].replace(self.__class__.sharp_symbol, '')
		else:
			scale[self.__class__.index] = scale[self.__class__.index] + self.__class__.flat_symbol
		return scale

class MajorPentatonic(Major, Pentatonic):
	
	indexes = [0,1,2,4,5]

	def __init__(self, tonic):
		super().__init__(tonic)

	@property
	def scale(self):
		# grab the parent scale
		parent = super().scale
		return [parent[i] for i in self.__class__.indexes]
		
	@property
	def bluesy(self):
		return super().flat_five(self.scale)


class MinorPentatonic(Minor, Pentatonic):
	
	indexes = [0, 2, 3, 4, 6]

	def __init__(self, tonic):
		super().__init__(tonic)


	@property 
	def scale(self):
		parent = super().scale
		return [parent[i] for i in self.__class__.indexes]

	@property
	def bluesy(self):
		return super().flat_five(self.scale)

if __name__ == '__main__' :

	penta = MinorPentatonic('e')
	print(penta.bluesy)


	
