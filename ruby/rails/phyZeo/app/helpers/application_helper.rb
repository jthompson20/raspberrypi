module ApplicationHelper	
	# helper to set default page title
	def page_title(title='')
		base_title 	= 'phyZeo'
		if title.empty?
			base_title
		else
			title + " | " + base_title
		end
	end
	def current_user
		@current_user ||= User.find_by(id: session[:user_id])
	end
end
