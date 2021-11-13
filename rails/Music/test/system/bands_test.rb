require "application_system_test_case"

class BandsTest < ApplicationSystemTestCase
  setup do
    @band = bands(:one)
  end

  test "visiting the index" do
    visit bands_url
    assert_selector "h1", text: "Bands"
  end

  test "creating a Band" do
    visit bands_url
    click_on "New Band"

    fill_in "Description", with: @band.description
    fill_in "Genre", with: @band.genre
    fill_in "Name", with: @band.name
    fill_in "Year", with: @band.year
    click_on "Create Band"

    assert_text "Band was successfully created"
    click_on "Back"
  end

  test "updating a Band" do
    visit bands_url
    click_on "Edit", match: :first

    fill_in "Description", with: @band.description
    fill_in "Genre", with: @band.genre
    fill_in "Name", with: @band.name
    fill_in "Year", with: @band.year
    click_on "Update Band"

    assert_text "Band was successfully updated"
    click_on "Back"
  end

  test "destroying a Band" do
    visit bands_url
    page.accept_confirm do
      click_on "Destroy", match: :first
    end

    assert_text "Band was successfully destroyed"
  end
end
