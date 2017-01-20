from scales import * 

class Triads(Diatonic):
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs) 

	@Diatonic.tonic.getter
	def tonic(self):
		print('attempted to call')
		return [super().tonic, super().mediant, super().dominant]

	@property 
	def supertonic(self):
		return [super().supertonic, super().subdominant, super().submediant]

	@property
	def mediant(self):
		return [super().mediant, super().dominant, super().leading_tone]


	@property
	def subdominant(self):
		return [super().subdominant, super().submediant, super().tonic]

