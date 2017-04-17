class CreatePaymentMethods < ActiveRecord::Migration[5.0]
  def change
    create_table :payment_methods do |t|
      t.integer :user_id
      t.string :merchant
      t.string :merchant_id
      t.string :cardtype
      t.string :lastfour
      t.integer :active
      t.integer :default

      t.timestamps
    end
  end
end
