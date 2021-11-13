class CreateGames < ActiveRecord::Migration[6.1]
  def change
    create_table :games do |t|
      t.string :name
      t.string :studio
      t.integer :stock
      t.string :platform

      t.timestamps
    end
  end
end
