
# A class should have one single job

# this is your base class 
class Chromatic:

	whole_step = 2 
	half_step = 1 
	flat_symbol = 'b'
	sharp_symbol = '#'

	default_flat = ['f']
	default_flat_minor = ['c', 'd', 'g']
	
	chromatic = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#',  'g', 'g#', 'a', 'a#', 'b' ]
	chromatic_flats = ['c', 'db', 'd', 'eb', 'e', 'f', 'gb', 'g', 'ab', 'a', 'bb', 'b']
	

	def valid_note(self, note):
		
		note = note.lower()

		if note in self.chromatic or note in self.chromatic_flats:
			return True

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

	MAJOR_FORMULA = {
		'whole_steps' : [0,2,5,7,9], 
		'half_steps' : [4,11]
	}

	MINOR_FORMULA = {
		'whole_steps' : [0,3,5,8,10], 
		'half_steps' : [2,7]
	}

	def __init__(self, tonic='c', major=True, **kwargs):
		super().__init__(**kwargs)
		self.major = major
		tonic = tonic.lower()
		self.scale = self.get_scale(
				tonic, 
				self.scale_formula['whole_steps'], 
				self.scale_formula['half_steps']
			)


	@property
	def major(self):
		return self.__major

	@major.setter
	def major(self, major):
		print('called major setter')
		if isinstance(major, bool):
			self.__major = major
		else:
			raise TypeError('Expected a boolean value')


	@property
	def scale_formula(self):
		if self.__major :
			return self.MAJOR_FORMULA
		else: 
			return self.MINOR_FORMULA

	@property
	def tonic(self):
		return self.scale[Diatonic.TONIC]

	@tonic.setter
	def tonic(self, tonic) :
		if valid_note(tonic.lower()):
			self.__tonic = tonic.lower()
		else: 
			raise Exception('Invalid Note')


	@property
	def supertonic(self):
		return self.scale[Diatonic.SUPERTONIC]

	@property 
	def mediant(self):
		return self.scale[Diatonic.MEDIANT]

	@property
	def subdominant(self):
		return self.scale[Diatonic.SUBDOMINANT]

	@property
	def dominant(self):
		return self.scale[Diatonic.DOMINANT]

	@property
	def submediant(self):
		return self.scale[Diatonic.SUBMEDIANT]

	@property
	def subtonic(self):
		return self.scale[Diatonic.SUBTONIC]


	# @property
	# def scale(self):
	# 	return self.get_scale(self.tonic, self.__scale_formula['whole_steps'], 
	# 		self.__scale_formula['half_steps'])
		

	# @scale.setter
	# def scale(self, test): 
	# 	if self.valid_note(self.tonic):
	# 		return self.get_scale(self.tonic, self.__scale_formula['whole_steps'], 
	# 			self.__scale_formula['half_steps'])

	def __str__(self):
		return ', '.join(self.scale)


# major and minor are now really easy implementations
class Major(Diatonic):

	def __init__(self, tonic='c', **kwargs):
		super().__init__(tonic, **kwargs)


class Minor(Diatonic):

	def __init__(self, tonic='c', **kwargs):
		super().__init__(tonic, major=True, **kwargs)



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

	penta = MinorPentatonic('e')
	print(penta.bluesy)


	
