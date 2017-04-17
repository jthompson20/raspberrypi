module MessagesHelper
	def patients
		# TODO: update this to pull a provider's patients
		@patients ||= User.where(admin:0)
	end
	def provider
		# TODO: update this to pull a patient's provider
		@provider ||= User.find_by(id: 6)
	end
end
