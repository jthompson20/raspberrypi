json.array!(@provider_patients) do |provider_patient|
  json.extract! provider_patient, :id, :provider_id, :patient_id, :active
  json.url provider_patient_url(provider_patient, format: :json)
end
