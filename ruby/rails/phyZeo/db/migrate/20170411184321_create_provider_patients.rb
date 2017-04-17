class CreateProviderPatients < ActiveRecord::Migration[5.0]
  def change
    create_table :provider_patients do |t|
      t.integer :provider_id
      t.integer :patient_id
      t.integer :active

      t.timestamps
    end
  end
end
