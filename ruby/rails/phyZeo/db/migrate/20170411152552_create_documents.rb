class CreateDocuments < ActiveRecord::Migration[5.0]
  def change
    create_table :documents do |t|
      t.integer :user_id
      t.string :slug
      t.integer :completed
      t.text :data

      t.timestamps
    end
  end
end
