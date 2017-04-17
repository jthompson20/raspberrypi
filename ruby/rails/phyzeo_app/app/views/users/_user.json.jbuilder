json.extract! user, :id, :provider, :first, :last, :email, :username, :password, :created_at, :updated_at
json.url user_url(user, format: :json)
