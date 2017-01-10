
diatonic = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#',  'g', 'g#', 'a', 'a#', 'b' ]
diatonic_flats = ['c', 'db', 'd', 'eb', 'e', 'f', 'gb', 'g', 'ab', 'a', 'bb', 'b']

whole_step = 2
half_step = 1

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
		
		if cursor == 0 or cursor == 2  or cursor == 5 or cursor == 7 or cursor == 9 : 
			cursor += whole_step
		elif cursor == 4 or cursor == 11: 
			cursor += half_step
	
	
