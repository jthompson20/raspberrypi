json.extract! event, :id, :patient_id, :provider_id, :name, :start, :end, :confirmed, :notes, :created_at, :updated_at
json.url event_url(event, format: :json)
