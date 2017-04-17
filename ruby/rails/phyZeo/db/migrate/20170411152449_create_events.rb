class CreateEvents < ActiveRecord::Migration[5.0]
  def change
    create_table :events do |t|
      t.integer :patient_id
      t.integer :provider_id
      t.string :name
      t.date :start
      t.date :end
      t.integer :confirmed
      t.text :notes

      t.timestamps
    end
  end
end
