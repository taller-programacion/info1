class CreateArtists < ActiveRecord::Migration[6.1]
  def change
    create_table :artists do |t|
      t.string :name
      t.string :lastname
      t.string :artistname
      t.string :nationality

      t.timestamps
    end
  end
end
