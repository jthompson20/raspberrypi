require 'test_helper'

class ProviderPatientsControllerTest < ActionDispatch::IntegrationTest
  setup do
    @provider_patient = provider_patients(:one)
  end

  test "should get index" do
    get provider_patients_url
    assert_response :success
  end

  test "should get new" do
    get new_provider_patient_url
    assert_response :success
  end

  test "should create provider_patient" do
    assert_difference('ProviderPatient.count') do
      post provider_patients_url, params: { provider_patient: { active: @provider_patient.active, patient_id: @provider_patient.patient_id, provider_id: @provider_patient.provider_id } }
    end

    assert_redirected_to provider_patient_url(ProviderPatient.last)
  end

  test "should show provider_patient" do
    get provider_patient_url(@provider_patient)
    assert_response :success
  end

  test "should get edit" do
    get edit_provider_patient_url(@provider_patient)
    assert_response :success
  end

  test "should update provider_patient" do
    patch provider_patient_url(@provider_patient), params: { provider_patient: { active: @provider_patient.active, patient_id: @provider_patient.patient_id, provider_id: @provider_patient.provider_id } }
    assert_redirected_to provider_patient_url(@provider_patient)
  end

  test "should destroy provider_patient" do
    assert_difference('ProviderPatient.count', -1) do
      delete provider_patient_url(@provider_patient)
    end

    assert_redirected_to provider_patients_url
  end
end
