class Triad:
	
	def __init__(self, scale, **kwargs):
		super().__init__(**kwargs)
		self.scale = scale

	@property
	def tonic(self):
		return [self.scale.tonic, self.scale.mediant, self.scale.dominant]

	@property
	def supertonic(self):
		return [self.scale.supertonic, self.scale.subdominant, self.scale.submediant]

	@property
	def mediant(self):
		return [self.scale.mediant, self.scale.dominant, self.scale.subtonic]

	@property
	def subdominant(self):
		return [self.scale.subdominant, self.scale.submediant, self.scale.tonic]

	@property
	def dominant(self):
		return [self.scale.dominant, self.scale.subtonic, self.scale.supertonic]

	@property
	def submediant(self):
		return [self.scale.submediant, self.scale.tonic, self.scale.mediant]

	@property
	def subtonic(self):
		return [self.scale.subtonic, self.scale.supertonic, self.scale.subdominant]


	def __str__(self):
		return 'Triads of the {tonic} {scale_type} scale ({scale})'.format(
			tonic=self.scale.tonic.upper(),
			scale_type=self.scale.__class__.__name__,
			scale=str(self.scale))


class Sevenths:

	pass


