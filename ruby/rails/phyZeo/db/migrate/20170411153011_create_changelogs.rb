class CreateChangelogs < ActiveRecord::Migration[5.0]
  def change
    create_table :changelogs do |t|
      t.integer :user_id
      t.string :action
      t.integer :success
      t.text :notes

      t.timestamps
    end
  end
end
