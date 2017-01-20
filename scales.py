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


	def valid_note(self, note):
		note = note.lower()

		if note in self.chromatic or note in self.chromatic_flats:
			return True
		else:
			return False


	def is_flat(self, tonic):

		tonic = tonic.lower()

		if len(tonic) == 1 :
			if tonic in self.default_flat:
				return True #default to sharp
			elif type(self).__name__ == 'Diatonic' :
				if not self.major:
					if tonic in self.default_flat_minor :
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

class Diatonic(Chromatic):
	
	''' Representation of Diatonic major and minor scales. The scale will default to c major '''


	TONIC = 0
	SUPERTONIC = 1
	MEDIANT = 2
	SUBDOMINANT = 3
	DOMINANT = 4
	SUBMEDIANT = 5
	SUBTONIC = 6

	__MAJOR_FORMULA = {
		'whole_steps' : [0,2,5,7,9],
		'half_steps' : [4,11]
	}

	__MINOR_FORMULA = {

		'whole_steps' : [0,3,5,8,10], 
		'half_steps' : [2,7]
	}

	def __init__(self, tonic='c', major=True, **kwargs):
		super().__init__(**kwargs)
		self.tonic = tonic
		self.major = major


	@property
	def major(self):
		return self.__major

	@major.setter
	def major(self, major):
		if isinstance(major, bool):
			self.__major = major
		else:
			raise TypeError('Expected a boolean value')


	@property
	def scale_formula(self):
		if self.__major :
			return self.__MAJOR_FORMULA
		else: 
			return self.__MINOR_FORMULA

	@property
	def scale(self):
		return self.get_scale(self.tonic, self.scale_formula['whole_steps'],
			self.scale_formula['half_steps'])

	@property
	def tonic(self):
		return self.__tonic


	@tonic.setter
	def tonic(self, tonic):
		# if self.valid_note(tonic.lower()):
		# 	self.__tonic_char = tonic.lower()
		# else:
		# 	raise Exception('Invalid note')
		self.__tonic = tonic.lower()

	@property
	def supertonic(self):
		return self.scale[self.SUPERTONIC]


	@property
	def mediant(self):
		return self.scale[self.MEDIANT]

	@property
	def subdominant(self):
		return self.scale[self.SUBDOMINANT]

	@property
	def dominant(self):
		return self.scale[self.DOMINANT]

	@property
	def submediant(self):
		return self.scale[self.SUBMEDIANT]

	@property
	def subtonic(self):
		return self.scale[self.SUBTONIC]


	def __str__(self):
		return ', '.join(self.scale)

class Major(Diatonic):

	'Major exists just to make the API cleaner.You could also just instantiate Diatonic'
	def __init__(self, tonic='c', **kwargs):
		super().__init__(tonic, major=True, **kwargs)



class Minor(Diatonic):

	def __init__(self, tonic='c', **kwargs):
		super().__init__(tonic, major=False, **kwargs)



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

class MajorPentatonic(Diatonic, Pentatonic):
	
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


class MinorPentatonic(Diatonic, Pentatonic):
	
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

	c = Minor(tonic='db')
	# print(c.supertonic)
	c.tonic='a'
	print(c.tonic)
	for i in [c.tonic, c.supertonic, c.mediant, c.submediant, c.dominant, c.subdominant, c.subtonic]:
		print(i)


