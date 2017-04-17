json.extract! document, :id, :user_id, :slug, :completed, :data, :created_at, :updated_at
json.url document_url(document, format: :json)
