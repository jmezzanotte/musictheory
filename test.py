import chords
import sys

#small change for git test
#x  = chords.get_scale_degrees('A#')
#print(x)

scales = ['db', 'd', 'a#', 'x']

for i in scales:
	chords.major_scale(i)



# tonic =  int(sys.argv[1])



# if tonic > 0 :

# 	degrees = chords.diatonic[tonic::]
# 	degrees.extend(chords.diatonic[0:tonic  ])
# 	print(degrees)
# 	chords.major_scale(tonic, degrees)
