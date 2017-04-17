json.extract! payment_method, :id, :user_id, :merchant, :merchant_id, :cardtype, :lastfour, :active, :default, :created_at, :updated_at
json.url payment_method_url(payment_method, format: :json)
