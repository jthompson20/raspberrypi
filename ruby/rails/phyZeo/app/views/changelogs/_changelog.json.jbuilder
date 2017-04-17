json.extract! changelog, :id, :user_id, :action, :success, :notes, :created_at, :updated_at
json.url changelog_url(changelog, format: :json)
