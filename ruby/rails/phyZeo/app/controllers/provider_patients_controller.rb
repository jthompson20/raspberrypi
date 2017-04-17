class ProviderPatientsController < ApplicationController
  before_action :set_provider_patient, only: [:show, :edit, :update, :destroy]

  # GET /provider_patients
  # GET /provider_patients.json
  def index
    @provider_patients = ProviderPatient.all
  end

  # GET /provider_patients/1
  # GET /provider_patients/1.json
  def show
  end

  # GET /provider_patients/new
  def new
    @provider_patient = ProviderPatient.new
  end

  # GET /provider_patients/1/edit
  def edit
  end

  # POST /provider_patients
  # POST /provider_patients.json
  def create
    @provider_patient = ProviderPatient.new(provider_patient_params)

    respond_to do |format|
      if @provider_patient.save
        format.html { redirect_to @provider_patient, notice: 'Provider patient was successfully created.' }
        format.json { render :show, status: :created, location: @provider_patient }
      else
        format.html { render :new }
        format.json { render json: @provider_patient.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /provider_patients/1
  # PATCH/PUT /provider_patients/1.json
  def update
    respond_to do |format|
      if @provider_patient.update(provider_patient_params)
        format.html { redirect_to @provider_patient, notice: 'Provider patient was successfully updated.' }
        format.json { render :show, status: :ok, location: @provider_patient }
      else
        format.html { render :edit }
        format.json { render json: @provider_patient.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /provider_patients/1
  # DELETE /provider_patients/1.json
  def destroy
    @provider_patient.destroy
    respond_to do |format|
      format.html { redirect_to provider_patients_url, notice: 'Provider patient was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_provider_patient
      @provider_patient = ProviderPatient.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def provider_patient_params
      params.require(:provider_patient).permit(:provider_id, :patient_id, :active)
    end
end
