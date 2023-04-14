class CreateRundates < ActiveRecord::Migration[7.0]
  def change
    create_table :rundates do |t|
      t.integer :word_id
      t.datetime :date
      t.integer :last_month

      t.timestamps
    end
  end
end
