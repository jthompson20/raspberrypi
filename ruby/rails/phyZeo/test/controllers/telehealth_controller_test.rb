require 'test_helper'

class TelehealthControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get telehealth_index_url
    assert_response :success
  end

  test "should get waiting" do
    get telehealth_waiting_url
    assert_response :success
  end

end
