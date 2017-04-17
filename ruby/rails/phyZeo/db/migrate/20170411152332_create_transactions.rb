class CreateTransactions < ActiveRecord::Migration[5.0]
  def change
    create_table :transactions do |t|
      t.integer :provider_id
      t.integer :patient_id
      t.string :transaction_id
      t.float :amount
      t.integer :success
      t.text :response

      t.timestamps
    end
  end
end
