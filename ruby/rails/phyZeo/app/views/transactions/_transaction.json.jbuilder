json.extract! transaction, :id, :provider_id, :patient_id, :transaction_id, :amount, :success, :response, :created_at, :updated_at
json.url transaction_url(transaction, format: :json)
