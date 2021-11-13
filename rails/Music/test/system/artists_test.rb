require "application_system_test_case"

class ArtistsTest < ApplicationSystemTestCase
  setup do
    @artist = artists(:one)
  end

  test "visiting the index" do
    visit artists_url
    assert_selector "h1", text: "Artists"
  end

  test "creating a Artist" do
    visit artists_url
    click_on "New Artist"

    fill_in "Artistname", with: @artist.artistname
    fill_in "Lastname", with: @artist.lastname
    fill_in "Name", with: @artist.name
    fill_in "Nationality", with: @artist.nationality
    click_on "Create Artist"

    assert_text "Artist was successfully created"
    click_on "Back"
  end

  test "updating a Artist" do
    visit artists_url
    click_on "Edit", match: :first

    fill_in "Artistname", with: @artist.artistname
    fill_in "Lastname", with: @artist.lastname
    fill_in "Name", with: @artist.name
    fill_in "Nationality", with: @artist.nationality
    click_on "Update Artist"

    assert_text "Artist was successfully updated"
    click_on "Back"
  end

  test "destroying a Artist" do
    visit artists_url
    page.accept_confirm do
      click_on "Destroy", match: :first
    end

    assert_text "Artist was successfully destroyed"
  end
end
