
class Chromatic:

	whole_step = 2 
	half_step = 1 

	def __init__(self):
		self.chromatic = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#',  'g', 'g#', 'a', 'a#', 'b' ]
		self.chromatic_flats = ['c', 'db', 'd', 'eb', 'e', 'f', 'gb', 'g', 'ab', 'a', 'bb', 'b']
	
	def is_flat(self, tonic):

		tonic = tonic.lower()

		if len(tonic) == 1 :
			#default to sharp
			return False
		elif len(tonic) == 2:
			temp = tonic[1]
			if temp == '#' :
				return False
			elif temp == 'b' :
				return True
		else: 
			return 

	def get_scale_degrees(self, tonic):

		tonic = tonic.lower()
		
		#determine which scale list tp use 
		if is_flat(tonic):
			scale = self.chormatic_flats
		elif not _is_flat(tonic):
			scale = self.chromatic
		
		tonic = scale.index(tonic)

		if tonic > 0 :
			degrees = scale[tonic::]
			degrees.extend(scale[0:tonic])
			return degrees
		else:
			return scale[0::]


	def get_scale(self, tonic, whole_step_index, half_step_index):

		scale_degrees = get_scale_degrees(tonic)
		
		cursor = 0 

		scale = []
		
		while cursor < len(scale_degrees) :

			#print(scale_degrees[cursor])
			scale.append(scale_degrees[cursor])
			
			if cursor in whole_step_index:
				cursor += whole_step
			elif cursor in half_step_index 
				cursor += half_step

		return scale


class Major(Chromatic):


	# Your design has made the implementation of major and minor easy
	relative_minor_degree = 9 
	whole_step_index = [0, 2, 5, 7,9]
	half_step_index = [4, 11]

	def __init__(self, tonic):
		# calling the parent constructor -- set up your part of the class
		super().__init__()
		self.tonic = tonic
	
	@propery
	def scale(self):
		return get_scale(self.tonic, whole_step_index, half_step_index)


	def relative_minor(self):
		return self.scale[relative_minor_degree]

	def __str__(self):
		return ', '.join(self.scale)


class Minor(Chromatic):


	


diatonic = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#',  'g', 'g#', 'a', 'a#', 'b' ]
diatonic_flats = ['c', 'db', 'd', 'eb', 'e', 'f', 'gb', 'g', 'ab', 'a', 'bb', 'b']

whole_step = 2
half_step = 1
# 9 will alway land on the tonic of the relative minor
relative_minor = 9 


def _is_flat(tonic):

	tonic = tonic.lower()

	if len(tonic) == 1 :
		#default to sharp
		return False
	elif len(tonic) == 2:
		temp = tonic[1]
		if temp == '#' :
			return False
		elif temp == 'b' :
			return True
	else: 
		return 



def _get_scale_degrees(tonic):

	tonic = tonic.lower()
	

	#determine which scale list tp use 
	if _is_flat(tonic):
		scale = diatonic_flats
	elif not _is_flat(tonic):
		scale = diatonic
	
	tonic = scale.index(tonic)

	if tonic > 0 :
		degrees = scale[tonic::]
		degrees.extend(scale[0:tonic])
		return degrees
	else:
		return scale[0::]


def major_scale(tonic):

	scale_degrees = _get_scale_degrees(tonic)
	
	cursor = 0 
	
	while cursor < len(scale_degrees) :

		print(scale_degrees[cursor])
		
		if cursor == 0 or cursor == 2  or cursor == 5 or cursor == 7 or cursor == 9 : 
			cursor += whole_step
		elif cursor == 4 or cursor == 11: 
			cursor += half_step



if __name__ == '__main__' :


	cursor = 0 
	print(len(diatonic))
	while cursor < len(diatonic) :

		print(diatonic[cursor])
		
		# if cursor in whole_step_inded -- this is what you will modify the method to be
		if cursor == 0 or cursor == 2  or cursor == 5 or cursor == 7 or cursor == 9 : 
			cursor += whole_step
		elif cursor == 4 or cursor == 11: 
			cursor += half_step
	
	
