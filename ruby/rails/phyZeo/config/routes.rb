Rails.application.routes.draw do
  	
	get    	'/login',   to: 'sessions#new'
	post   	'/login',   to: 'sessions#create'
	delete 	'/logout',  to: 'sessions#destroy'
	get 	'/logout',  to: 'sessions#destroy'

	root 'users#index'
	resources :provider_patients
	resources :payment_methods
	resources :changelogs
	resources :documents
	resources :events
	resources :transactions
	resources :users
	get '/messages', 		to: 'messages#index'
	get '/telehealth', 		to: 'telehealth#index'
	get '/connecting', 		to: 'telehealth#waiting'
	# For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
