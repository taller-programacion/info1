json.extract! artist, :id, :name, :lastname, :artistname, :nationality, :created_at, :updated_at
json.url artist_url(artist, format: :json)
