from django.db import models


class Archivo(models.Model):
    archivo = models.FileField(upload_to='archivos_excel/')

class MediaDissemination2020(models.Model):
    promotor_name = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    assistant_name = models.CharField(max_length=100)
    municipality_residence = models.CharField(max_length=100)
    rol_territory = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.promotor_name

    class Meta:
        db_table = 'media_dissemination_2020'

class DialogueTables2020(models.Model):
    cultural_dialogue_number = models.CharField(max_length=100)
    promoter_name = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.promoter_name

    class Meta:
        db_table = 'dialogue_tables_2020'

class Beneficiaries2020(models.Model):
    cultural_monitor = models.CharField(max_length=100)
    nac_beneficiary = models.CharField(max_length=100)
    beneficiary_name = models.CharField(max_length=100)
    document_type = models.CharField(max_length=100)
    document_number = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    stratum = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    study = models.CharField(max_length=100)
    level_study = models.CharField(max_length=100)
    dissability = models.CharField(max_length=100)
    dissability_type = models.CharField(max_length=100)
    victim = models.CharField(max_length=100)
    victim_type = models.CharField(max_length=100)
    ethnicity = models.CharField(max_length=100)
    medical_service = models.CharField(max_length=100)
    eps_name = models.CharField(max_length=100)
    health_status = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=100)

    def __str__(self):
        return self.cultural_monitor

    class Meta:
        db_table = 'beneficiaries_2020'

class Attendants2020(models.Model):
    cultural_monitor = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    beneficiary_name = models.CharField(max_length=100)
    document_type = models.CharField(max_length=100)
    document_number = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    stratum = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    study = models.CharField(max_length=100)
    disability = models.CharField(max_length=100)
    disability_type = models.CharField(max_length=100)
    victim = models.CharField(max_length=100)
    victim_type = models.CharField(max_length=100)
    type_ethnicity = models.CharField(max_length=100)
    medical_service = models.CharField(max_length=100)
    eps_name = models.CharField(max_length=100)
    health_status = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=100)

    def __str__(self):
        return self.cultural_monitor

    class Meta:
        db_table = 'attendants_2020'


class Contracts2020(models.Model):
    number_contract = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    assignment_salary = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    month_contract = models.CharField(max_length=100)
    dues = models.CharField(max_length=100)
    specific_rol = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    tribe = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    date_contract = models.CharField(max_length=100)
    date_end = models.CharField(max_length=100)
    contract_value = models.CharField(max_length=100)
    supervisor = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    sign_contract = models.CharField(max_length=100)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'contracts_2020'

class Transfer2020(models.Model):
    transfer_number= models.CharField(max_length=100)
    transfer_type = models.CharField(max_length=100)
    facilitator_name = models.CharField(max_length=100)
    month = models.CharField(max_length=100)

    def __str__(self):
        return self.facilitator_name

    class Meta:
        db_table = 'transfer_2020'

class PsychosocialCareAppointments2020(models.Model):
    number_cite = models.CharField(max_length=100)
    facilitator_name = models.CharField(max_length=100)
    month = models.CharField(max_length=100)

    def __str__(self):
        return self.facilitator_name

    class Meta:
        db_table = 'psychosocial_care_appointments_2020a'

class SynchronousMeetings2020(models.Model):
    activation_number = models.CharField(max_length=100)
    tribe = models.CharField(max_length=100)
    methodologist_name = models.CharField(max_length=100)
    monitor_name = models.CharField(max_length=100)
    art = models.CharField(max_length=100)
    pedagogical_tool = models.CharField(max_length=100)
    number_participants = models.CharField(max_length=100)
    month = models.CharField(max_length=100)

    def __str__(self):
        return self.methodologist_name

    class Meta:
        db_table = 'synchronous_meetings_2020'

class Beneficiaries2021a(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    participant_type = models.CharField(max_length=100)
    vinculation = models.CharField(max_length=100)
    written_link = models.CharField(max_length=100)
    nac_tab = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)
    monitor_name = models.CharField(max_length=100)
    name_parents = models.CharField(max_length=100)
    nac_beneficiary = models.CharField(max_length=100)
    name_beneficiary = models.CharField(max_length=100)
    document_type = models.CharField(max_length=100)
    document_number = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    stratum = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    study = models.CharField(max_length=100)
    level_study = models.CharField(max_length=100)
    dissability = models.CharField(max_length=100)
    dissability_type = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    ethnicity = models.CharField(max_length=100)
    medical_service = models.CharField(max_length=100)
    entity_name = models.CharField(max_length=100)
    health_status = models.CharField(max_length=100)
    upload_data = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'beneficiaries_2021a'
        
class Binnacles2021a(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    monitor_name = models.CharField(max_length=100)
    modality = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    number_attendees = models.CharField(max_length=100)
    upload_date = models.CharField(max_length=100)

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'binnacles_2021a'

class DialogueTables2021a(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    objective = models.CharField(max_length=100)
    diary = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    achievements_difficulties = models.CharField(max_length=100)
    alerts = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'dialogue_tables_2021a'

class Instruments2021a(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    name_reporting_supervision_support = models.CharField(max_length=100)
    facilitator = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    form= models.CharField(max_length=100)
    benefited_person = models.CharField(max_length=100)
    means_verification = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name_reporting_superivison_support

    class Meta:
        db_table = 'instruments_loaded_on_platform_2021a'

class MethodologicalTransfers2021a(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    number_attendees = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    explanation = models.CharField(max_length=100)
    pedagogical = models.CharField(max_length=100)
    practical_technician = models.CharField(max_length=100)
    methodological = models.CharField(max_length=100)
    other_observations = models.CharField(max_length=100)
    upload_date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'methodological_transfers_2021a'
        
class MonitoringParticipants2021a(models.Model):
    id = models.AutoField(primary_key=True)
    monitor_name = models.CharField(max_length=100)
    document_number_monitor = models.CharField(max_length=100)
    beneficiary_name = models.CharField(max_length=100)
    number_document_beneficiary = models.CharField(max_length=100)
    binnacles = models.CharField(max_length=100)
    attendance_count = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)


    def __str__(self):
        return self.monitor_name

    class Meta:
        db_table = 'monitoring_participants_impact_2021a'

class PedagogicalSheets2021a(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    monitor_name = models.CharField(max_length=100)
    cultural_right = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    experiential_objective = models.CharField(max_length=100)
    lineament = models.CharField(max_length=100)
    orientation = models.CharField(max_length=100)
    manifestation = models.CharField(max_length=100)
    process = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    resource = models.CharField(max_length=100)
    upload_date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    

    def __str__(self):
        return self.monitor_name

    class Meta:
        db_table = 'pedagogicals_sheets_2021a'

class PlataformTraining2021a(models.Model):
    id = models.AutoField(primary_key=True)
    training_number = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    collaborator = models.CharField(max_length=100)

    def __str__(self):
        return self.collaborator

    class Meta:
        db_table = 'platform_management_training_2021a'

class PsychosocialCare2021a(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    psychosocial_name = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    person_served = models.CharField(max_length=100)
    name_monitor = models.CharField(max_length=100)
    objective = models.CharField(max_length=100)
    development= models.CharField(max_length=100)
    referrals = models.CharField(max_length=100)
    conclutions= models.CharField(max_length=100)
    report = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.psychosocial_name

    class Meta:
        db_table = 'psychosocial_care_appointments_2021a'

class PsychosocialTransfers2021a(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    number_attendees = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    objective = models.CharField(max_length=100)
    topics = models.CharField(max_length=100)
    development = models.CharField(max_length=100)
    conclutions= models.CharField(max_length=100)
    reports = models.CharField(max_length=100)
    upload_date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'psychosocial_transfers_2021a'

class MonitoringParticipants2021b(models.Model):
    id = models.AutoField(primary_key=True)
    monitor_name = models.CharField(max_length=100)
    document_number_monitor = models.CharField(max_length=100)
    beneficiary_name = models.CharField(max_length=100)
    document_number_beneficiary	 = models.CharField(max_length=100)
    binnacles = models.CharField(max_length=100)
    attendace_count = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)


    def __str__(self):
        return self.monitor_name

    class Meta:
        db_table = 'participants_follow_2021b_2022a'

class CulturalActivation2021b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    monitor_name = models.CharField(max_length=100)
    type_binnacle = models.CharField(max_length=100)
    modality = models.CharField(max_length=100)
    cultural_right = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    name_activity = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    experiential_objective = models.CharField(max_length=100)
    lineament = models.CharField(max_length=100)
    orientation = models.CharField(max_length=100)
    goal_achieved = models.CharField(max_length=100)
    explanation = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    development = models.CharField(max_length=100)
    final = models.CharField(max_length=100)
    observations = models.CharField(max_length=100)
    assistants_number = models.CharField(max_length=100)
    capacity_number = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.monitor_name

    class Meta:
        db_table = 'cultural_activation_2021b_2022a'

class FeedbackCulturalActivation2021b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    name_manager = models.CharField(max_length=100)
    assistants_number = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    objective = models.CharField(max_length=100)
    diary = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    achievements_difficulties = models.CharField(max_length=100)
    alerts = models.CharField(max_length=100)
    status= models.CharField(max_length=100)

    def __str__(self):
        return self.name_manager

    class Meta:
        db_table = 'feedback_cultural_activations_2021b_2022a'

class MethodologicalInstructions2021b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    name_manager = models.CharField(max_length=100)
    assistants_number = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    goal_achieved = models.CharField(max_length=100)
    explication = models.CharField(max_length=100)
    pedagogicals = models.CharField(max_length=100)
    technical_practice = models.CharField(max_length=100)
    metodologycal = models.CharField(max_length=100)
    others_observations = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name_manager

    class Meta:
        db_table = 'methodological_instructions_2021b_2022a'

class PsychosocialInstructions2021b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    name_psychosocial = models.CharField(max_length=100)
    assistants_number = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    objective = models.CharField(max_length=100)
    themes= models.CharField(max_length=100)
    development = models.CharField(max_length=100)
    conclutions = models.CharField(max_length=100)
    report = models.CharField(max_length=100)
    status= models.CharField(max_length=100)

    def __str__(self):
        return self.name_psychosocial

    class Meta:
        db_table = 'psychosocial_instructions_2021b_2022a'

class TerritorialTables2021b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    name_manager = models.CharField(max_length=100)
    number_assistants = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    objective = models.CharField(max_length=100)
    diary = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    achievements_and_difficulties = models.CharField(max_length=100)
    alerts = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name_manager

    class Meta:
        db_table = 'territorial_tables_2021b_2022a'

class BeneficiariesCapacity2021b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    monitor_name = models.CharField(max_length=100)
    type_binnacle = models.CharField(max_length=100)
    modality = models.CharField(max_length=100)
    cultural_right = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    activity_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    experiential_objective = models.CharField(max_length=100)
    lineament = models.CharField(max_length=100)
    orientation = models.CharField(max_length=100)
    goal_achieved = models.CharField(max_length=100)
    explication = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    development = models.CharField(max_length=100)
    final = models.CharField(max_length=100)
    observations = models.CharField(max_length=100)
    capacity_number = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.monitor_name
    class Meta:
        db_table = 'beneficiaries_capacity_2021b_2022a'

class Beneficiaries2021b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    participant_type = models.CharField(max_length=100)
    vinculation = models.CharField(max_length=100)
    vinculation_written = models.CharField(max_length=100)
    nac_file = models.CharField(max_length=100)
    monitor_name = models.CharField(max_length=100)
    parents_name = models.CharField(max_length=100)
    nac_beneficiary = models.CharField(max_length=100)
    beneficiary_name = models.CharField(max_length=100)
    document_type = models.CharField(max_length=100)
    document_number = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    stratum = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    study = models.CharField(max_length=100)
    level_study = models.CharField(max_length=100)
    dissability = models.CharField(max_length=100)
    dissability_tipe = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    ethnicity = models.CharField(max_length=100)
    medical_service = models.CharField(max_length=100)
    entity_name = models.CharField(max_length=100)
    health_status = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.monitor_name

    class Meta:
        db_table = 'beneficiaries_2021b_2022a'

class PedagogicalSheets2021b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    monitor_name = models.CharField(max_length=100)
    cultural_right = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    experiental_objective = models.CharField(max_length=100)
    lineament = models.CharField(max_length=100)
    orientation = models.CharField(max_length=100)
    manifestation = models.CharField(max_length=100)
    process = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    resource = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    

    def __str__(self):
        return self.monitor_name

    class Meta:
        db_table = 'pedagogical_sheet_2021b_2022a'

        
class DevCulturalActivation2021b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    monitor_name = models.CharField(max_length=100)
    type_binnacle = models.CharField(max_length=100)
    modality = models.CharField(max_length=100)
    cultural_right = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    activity_name = models.CharField(max_length=100)
    placer = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    experiential_objective = models.CharField(max_length=100)
    lineament = models.CharField(max_length=100)
    orientation = models.CharField(max_length=100)
    goal_achieved = models.CharField(max_length=100)
    explication = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    development = models.CharField(max_length=100)
    final = models.CharField(max_length=100)
    observations = models.CharField(max_length=100)
    assistans_number = models.CharField(max_length=100)
    capacity_number = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.monitor_name

    class Meta:
        db_table = 'binnacles_2021b_2022a'

class PsychosocialCare2021b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    psychosocial_name = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    name_person_served = models.CharField(max_length=100)
    monitor_name = models.CharField(max_length=100)
    objective = models.CharField(max_length=100)
    development= models.CharField(max_length=100)
    referrals = models.CharField(max_length=100)
    conclutions= models.CharField(max_length=100)
    report = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.psychosocial_name

    class Meta:
        db_table = 'psychosocial_care_appointments_2021b_2022a'

class CirculationCultural2021b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    monitor_name = models.CharField(max_length=100)
    type_binnacle = models.CharField(max_length=100)
    modality = models.CharField(max_length=100)
    cultural_right = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    activity_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    experiential_objective = models.CharField(max_length=100)
    lineament = models.CharField(max_length=100)
    orientation = models.CharField(max_length=100)
    goal_achieved = models.CharField(max_length=100)
    explication = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    development = models.CharField(max_length=100)
    final = models.CharField(max_length=100)
    observations = models.CharField(max_length=100)
    number_capacity = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.monitor_name

    class Meta:
        db_table = 'circulation_cultural_activations_2021b_2022a'

class ShowArtistic2021b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    monitor_name = models.CharField(max_length=100)
    type_binnacle = models.CharField(max_length=100)
    modality = models.CharField(max_length=100)
    cultural_right = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    activity_name = models.CharField(max_length=100)
    placer = models.CharField(max_length=100)  # Corregido de "placer" a "place"
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)  # Corregido de "expertiose" a "expertise"
    experiential_objective = models.CharField(max_length=100)
    lineament = models.CharField(max_length=100)
    orientation = models.CharField(max_length=100)
    goal_achieved = models.CharField(max_length=100)
    explication = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    development = models.CharField(max_length=100)
    final = models.CharField(max_length=100)
    observations = models.CharField(max_length=100)
    number_assistant = models.CharField(max_length=100)
    number_capacity = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.monitor_name

    class Meta:
        db_table = 'artistic_sample_2021b_2022a'

class ValidationUsers2022b(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    document = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    type_user = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'monitoring_validation_users_2022b'

class DialogueTables2022b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    name_manager = models.CharField(max_length=100)
    number_assistants = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    objective = models.CharField(max_length=100)
    diary = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    goals_difficulties = models.CharField(max_length=100)
    alerts = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name_manager

    class Meta:
        db_table = 'dialogue_tables_2022b'

class CulturalActivation2022b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    name_monitor = models.CharField(max_length=100)
    type_binnacle = models.CharField(max_length=100)
    modality = models.CharField(max_length=100)
    cultural_right = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    activity_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    experiential_objective = models.CharField(max_length=100)
    lineament = models.CharField(max_length=100)
    orientation = models.CharField(max_length=100)
    goal_achieved = models.CharField(max_length=100)
    explication = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    development = models.CharField(max_length=100)
    final = models.CharField(max_length=100)
    observations = models.CharField(max_length=100)
    number_assistants = models.CharField(max_length=100)
    number_capacity = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name_monitor

    class Meta:
        db_table = 'cultural_activation_2022b'

class MethodologicalInstructions2022b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    name_manager = models.CharField(max_length=100)
    number_assistant = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    goal_achieved = models.CharField(max_length=100)
    explication = models.CharField(max_length=100)
    pedagogical = models.CharField(max_length=100)
    technical_practice = models.CharField(max_length=100)
    metodologycal = models.CharField(max_length=100)
    others_observations = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name_manager

    class Meta:
        db_table = 'methodological_instructions_2022b'

class PsychosocialInstructions2022b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    assistant_number = models.CharField(max_length=100)  
    nac = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    objective = models.CharField(max_length=100)
    themes = models.CharField(max_length=100)
    development = models.CharField(max_length=100)
    conclutions = models.CharField(max_length=100)  
    report = models.CharField(max_length=100)  
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'psychosocial_instructions_2022b'

class PedagogicalSheets2022b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    cultural_right = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    experiential_objective = models.CharField(max_length=100)
    lineament = models.CharField(max_length=100)
    orientation = models.CharField(max_length=100)
    manifestation = models.CharField(max_length=100)
    process = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    resource = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pedagogical_sheets_2022b'

class Binnacles2022b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    monitor_name = models.CharField(max_length=100)
    type_binnacle = models.CharField(max_length=100)
    modality = models.CharField(max_length=100)
    cultural_right = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    activity_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    experiential_objective = models.CharField(max_length=100)
    lineament = models.CharField(max_length=100)
    orientation = models.CharField(max_length=100)
    goal_achieved = models.CharField(max_length=100)
    explication = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    development = models.CharField(max_length=100)
    final = models.CharField(max_length=100)
    observations = models.CharField(max_length=100)
    number_attendees = models.CharField(max_length=100)
    number_capacity = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.monitor_name

    class Meta:
        db_table = 'binnacles_2022b'

class PsychosocialCareAppointments2022b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    psychosocial_name = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    name_person_served = models.CharField(max_length=100)
    monitor_name = models.CharField(max_length=100)
    objective = models.CharField(max_length=100)
    development = models.CharField(max_length=100)
    referrals = models.CharField(max_length=100)
    conclutions = models.CharField(max_length=100)
    report = models.CharField(max_length=100)
    state = models.CharField(max_length=100)


    def __str__(self):
        return self.psychosocial_name

    class Meta:
        db_table = 'psychosocial_care_appointments_2022b'

class MethodologicalCarpet2022b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=100)
    type_binnacle = models.CharField(max_length=100)
    modality = models.CharField(max_length=100)
    cultural_right = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    activity_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    expertice = models.CharField(max_length=100)  # Corregido de "expertice" a "expertise"
    experiential_objective = models.CharField(max_length=100)
    lineament = models.CharField(max_length=100)
    orientation = models.CharField(max_length=100)
    goal_achieved = models.CharField(max_length=100)
    explication = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    development = models.CharField(max_length=100)
    final = models.CharField(max_length=100)
    observations = models.CharField(max_length=100)
    assistant_number = models.CharField(max_length=100)  # Corregido de "assistant_number" a "assistants_number"
    capacity_number = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


    def __str__(self):
        return self.manager_name

    class Meta:
        db_table = 'methodological_carpet_2022b'

class CulturalEnsemble2022b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    instructor_name = models.CharField(max_length=100)
    type_binnacle = models.CharField(max_length=100)
    modality = models.CharField(max_length=100)
    cultural_right = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    activity_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)  # Corregido de "expertice" a "expertise"
    experiential_objective = models.CharField(max_length=100)
    lineament = models.CharField(max_length=100)
    orientation = models.CharField(max_length=100)
    goal_achieved = models.CharField(max_length=100)
    explication = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    development = models.CharField(max_length=100)
    final = models.CharField(max_length=100)
    observations = models.CharField(max_length=100)
    assistant_number = models.CharField(max_length=100)  # Corregido de "assistant_number" a "assistants_number"
    capacity_number = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


    def __str__(self):
        return self.manager_name

    class Meta:
        db_table = 'cultural_ensemble_2022b'

class CulturalSeedbed2022b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    instructor_name = models.CharField(max_length=100)
    type_binnacle = models.CharField(max_length=100)
    modality = models.CharField(max_length=100)
    cultural_right = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    activity_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)  # Corregido de "expertice" a "expertise"
    experiential_objective = models.CharField(max_length=100)
    lineament = models.CharField(max_length=100)
    orientation = models.CharField(max_length=100)
    goal_achieved = models.CharField(max_length=100)
    explication = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    development = models.CharField(max_length=100)
    final = models.CharField(max_length=100)
    observations = models.CharField(max_length=100)
    assistant_number = models.CharField(max_length=100)  # Corregido de "assistant_number" a "assistants_number"
    capacity_number = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


    def __str__(self):
        return self.instructor_name
    
    class Meta:
        db_table = 'cultural_seedbed_2022b'

class ParentsSchool2022b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    psychosocial_name = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    monitor_name = models.CharField(max_length=100)
    place_attention = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    objective = models.CharField(max_length=100)
    development = models.CharField(max_length=100)
    conclutions = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.psychosocial_name
    
    class Meta:
        db_table = 'parents_school_2022b'

class StrategysCirculation2022b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    monitor_name = models.CharField(max_length=100)
    type_binnacle = models.CharField(max_length=100)
    modality = models.CharField(max_length=100)
    cultural_right = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    activity_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    experiential_objective = models.CharField(max_length=100)
    lineament = models.CharField(max_length=100)
    orientation = models.CharField(max_length=100)
    goal_achieved = models.CharField(max_length=100)
    explication = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    development = models.CharField(max_length=100)
    final = models.CharField(max_length=100)
    observations = models.CharField(max_length=100)
    assistant_number = models.CharField(max_length=100)
    capacity_number = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.monitor_name
    
    class Meta:
        db_table = 'strategys_circulation_2022b'

class Beneficiaries2022b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    participant_type = models.CharField(max_length=100)
    vinculation = models.CharField(max_length=100)
    vinculation_written = models.CharField(max_length=100)
    nac_tab = models.CharField(max_length=100)
    monitor_name = models.CharField(max_length=100)
    parents_name = models.CharField(max_length=100)
    nac_beneficiary = models.CharField(max_length=100)
    beneficiary_name = models.CharField(max_length=100)
    document_type = models.CharField(max_length=100)
    document_number = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    stratum = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    study = models.CharField(max_length=100)
    level_study = models.CharField(max_length=100)
    dissability = models.CharField(max_length=100)
    type_dissability = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    ethnicity = models.CharField(max_length=100)
    medical_service = models.CharField(max_length=100)
    entity_name = models.CharField(max_length=100)
    health_status = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.monitor_name

    class Meta:
        db_table = 'beneficiaries_2022b'

class BeneficiariesCapacity2022b(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    monitor_name = models.CharField(max_length=100)
    type_binnacle = models.CharField(max_length=100)
    modality = models.CharField(max_length=100)
    cultural_right = models.CharField(max_length=100)
    nac = models.CharField(max_length=100)
    activity_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    final_time = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    experiential_objective = models.CharField(max_length=100)
    lineament = models.CharField(max_length=100)
    orientation = models.CharField(max_length=100)
    goal_achieved = models.CharField(max_length=100)
    explication = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    development = models.CharField(max_length=100)
    final = models.CharField(max_length=100)
    observations = models.CharField(max_length=100)
    assistant_number = models.CharField(max_length=100)
    capacity_number = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.monitor_name

    class Meta:
        db_table = 'beneficiaries_capacity_2022b'
        
class MeansVerification2023a(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField(max_length=100)
    document_number = models.IntegerField(default=0)
    rol = models.TextField(max_length=100)
    nac_user = models.TextField(max_length=100)
    email = models.TextField(max_length=100)
    
    def __str__(self):
        return self.username

    class Meta:
        db_table = 'means_verification_2023a'
        
class VerificationFollow2023a(models.Model):
    
    id = models.AutoField(primary_key=True)
    consecutive = models.TextField(null=True)
    user = models.TextField(null=True)
    user_id = models.IntegerField(default=0)
    nac_user = models.TextField(null=True)
    rol_user = models.TextField(null=True)
    nac = models.TextField(null=True)
    user_visit = models.TextField(null=True)
    rol_user_visit = models.TextField(null=True)
    date = models.TextField(null=True)
    start_date = models.TextField(null=True)
    end_date = models.TextField(null=True)
    place = models.TextField(null=True)
    objective = models.TextField(null=True)
    purpose_visit = models.TextField(null=True)
    topics = models.TextField(null=True)
    perception = models.TextField(null=True)
    identified_problems = models.TextField(null=True)
    actions = models.TextField(null=True)
    comments = models.TextField(null=True)
    status = models.TextField(null=True)
    
    def __str__(self):
        return self.user

    class Meta:
        db_table = 'verification_follow_2023a'
        
class DialogueTables2023a(models.Model):
    
    id = models.AutoField(primary_key=True)
    consecutive = models.TextField(null=True)
    user = models.TextField(null=True)
    document_number = models.IntegerField(default=0)
    nac = models.TextField(null=True)
    rol_user = models.TextField(null=True)
    nac_activity = models.TextField(null=True)
    number_attendees = models.IntegerField(default=0)
    date = models.TextField(null=True)
    start_time = models.TextField(null=True)
    end_time = models.TextField(null=True)
    objective = models.TextField(null=True)
    topic = models.TextField(null=True)
    agenda_day = models.TextField(null=True)
    description = models.TextField(null=True)
    achievements_difficulties = models.TextField(null=True)
    alerts = models.TextField(null=True)
    methodological_support = models.TextField(null=True)
    status = models.TextField(null=True)
    
    def __str__(self):
        return self.user

    class Meta:
        db_table = 'dialogue_tables_2023a'
    
class Activations2023a(models.Model):
    
    id = models.AutoField(primary_key=True)
    consecutive = models.TextField(null=True)
    user = models.TextField(null=True)
    user_document_number = models.IntegerField(null=True)
    user_role = models.TextField(null=True)
    user_nac = models.TextField(null=True)
    activity_name = models.TextField(null=True)
    activity_date = models.TextField(null=True)
    start_time = models.TextField(null=True)
    end_time = models.TextField(null=True)
    location = models.TextField(null=True)
    nac = models.TextField(null=True)
    expertise = models.TextField(null=True)
    cultural_rights = models.TextField(null=True)
    experiential_objective = models.TextField(null=True)
    guidelines = models.TextField(null=True)
    orientations = models.TextField(null=True)
    experiential_objective_fulfilled = models.TextField(null=True)
    explain_why = models.TextField(null=True)
    start = models.TextField(null=True)
    development = models.TextField(null=True)
    end = models.TextField(null=True)
    observations = models.TextField(null=True)
    number_of_attendees = models.IntegerField(null=True)
    status = models.TextField(null=True)

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'activations_2023a'

class Circulation2023a(models.Model):
    
    id = models.AutoField(primary_key=True)
    consecutive = models.TextField(null=True)
    circulation = models.TextField(null=True)
    user = models.TextField(null=True)
    user_document_number = models.IntegerField(null=True)
    user_nac = models.TextField(null=True)
    user_role = models.TextField(null=True)
    activity_date = models.TextField(null=True)
    key_actors_for_circulation = models.TextField(null=True)
    pec = models.TextField(null=True)
    methodological_planning_cards = models.TextField(null=True)
    event_name = models.TextField(null=True)
    participant_domain_level = models.TextField(null=True)
    description = models.TextField(null=True)
    circulation_territory = models.TextField(null=True)
    other_territory_if_any = models.TextField(null=True)
    number_of_seedlings_members = models.IntegerField(null=True)
    audience_characteristics = models.TextField(null=True)
    cultural_rights = models.TextField(null=True)
    guidelines = models.TextField(null=True)
    orientations = models.TextField(null=True)
    artistic_expertise_to_work_on = models.TextField(null=True)
    participation_observations = models.TextField(null=True)
    number_of_attendees = models.IntegerField(null=True)
    status = models.TextField(null=True)

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'circulations_2023a'

class ShowCultural2023a(models.Model):
    
    id = models.AutoField(primary_key=True)
    consecutive = models.TextField(null=True)
    user = models.TextField(null=True)
    user_id = models.IntegerField(null=True)
    rol = models.TextField(null=True)
    nac_user = models.TextField(null=True)
    date = models.TextField(null=True)
    activity_name = models.TextField(null=True)
    expertise = models.TextField(null=True)
    artistic_participation = models.TextField(null=True)
    succesfull = models.TextField(null=True)
    sustentation = models.TextField(null=True)
    number_attendees = models.IntegerField(null=True)
    status = models.TextField(null=True)
    
    def __str__(self):
        return self.user

    class Meta:
        db_table = 'show_cultural_2023a'
        
class Ensamble2023a(models.Model):
    
    id = models.AutoField(primary_key=True)
    consecutive = models.TextField(null=True)
    cultural_assembly = models.TextField(null=True)
    user = models.TextField(null=True)
    date = models.TextField(null=True)
    pec = models.TextField(null=True)
    methodological_planning_cards = models.TextField(null=True)
    seedlings_domain_level = models.TextField(null=True)
    assembly_characteristics = models.TextField(null=True)
    description = models.TextField(null=True)
    process_objective = models.TextField(null=True)
    audience_characteristics = models.TextField(null=True)
    cultural_rights = models.TextField(null=True)
    guidelines = models.TextField(null=True)
    orientations = models.TextField(null=True)
    value = models.TextField(null=True)
    artistic_expertise_to_work_on = models.TextField(null=True)
    aspects_to_evaluate = models.TextField(null=True)
    comments = models.TextField(null=True)
    number_of_attendees = models.IntegerField(null=True)
    status = models.TextField(null=True)
    
    def __str__(self):
        return self.user

    class Meta:
        db_table = 'assembly_2023a'
        
class TransferMethodological2023a(models.Model):
    
    id = models.AutoField(primary_key=True)
    consecutive = models.TextField(null=True)
    user = models.TextField(null=True)
    user_id = models.IntegerField(null=True)
    rol = models.TextField(null=True)
    nac_user = models.TextField(null=True)
    nac = models.TextField(null=True)
    place = models.TextField(null=True)
    expertise = models.TextField(null=True)
    date = models.TextField(null=True)
    start_date = models.TextField(null=True)
    end_date = models.TextField(null=True)
    goal_achieved = models.TextField(null=True)
    explication = models.TextField(null=True)
    pedagogical = models.TextField(null=True)
    technical_practice = models.TextField(null=True)
    methodological = models.TextField(null=True)
    others_observation = models.TextField(null=True)
    number_assitants = models.IntegerField(null=True)
    status = models.TextField(null=True)
    
    def __str__(self):
        return self.user

    class Meta:
        db_table = 'transfer_methodological_2023a'
    
class TransferPsychosocial2023a(models.Model):
    
    id = models.AutoField(primary_key=True)
    consecutive = models.TextField(null=True)
    psychosocial = models.TextField(null=True)
    id_psychosocial = models.IntegerField(null=True)
    nac_psychosocial = models.TextField(null=True)
    rol = models.TextField(null=True)
    nac_activity = models.TextField(null=True)
    date = models.TextField(null=True)
    start_time = models.TextField(null=True)
    end_time = models.TextField(null=True)
    objective = models.TextField(null=True)
    themes = models.TextField(null=True)
    development = models.TextField(null=True)
    conclutions = models.TextField(null=True)
    alerts = models.TextField(null=True)
    status = models.TextField(null=True)
    
    def __str__(self):
        return self.psychosocial

    class Meta:
        db_table = 'transfer_psychosocial_2023a'
        
class PlanningMonitors2023a(models.Model):
    
    id = models.AutoField(primary_key=True)
    consecutive = models.TextField(null=True)
    user = models.TextField(null=True)
    user_id = models.IntegerField(null=True)
    nac_user = models.TextField(null=True)
    rol = models.TextField(null=True)
    date = models.TextField(null=True)
    activity = models.TextField(null=True)
    expertise = models.TextField(null=True)
    nac = models.TextField(null=True)
    cultural_right = models.TextField(null=True)
    lineaments = models.TextField(null=True)
    orientation = models.TextField(null=True)
    objective = models.TextField(null=True)
    manifestation = models.TextField(null=True)
    process = models.TextField(null=True)
    product = models.TextField(null=True)
    resources = models.TextField(null=True)
    status = models.TextField(null=True)
    
    def __str__(self):
        return self.user

    class Meta:
        db_table = 'pedagogical_planning_monitors_2023a'
        
class PlanningInstructors2023a(models.Model):
    
    id = models.AutoField(primary_key=True)
    consecutive = models.TextField(null=True)
    user = models.TextField(null=True)
    user_id = models.IntegerField(null=True)
    nac_user = models.TextField(null=True)
    rol = models.TextField(null=True)
    cultural_seedbed = models.TextField(null=True)
    start = models.TextField(null=True)
    end = models.TextField(null=True)
    group = models.TextField(null=True)
    filter = models.TextField(null=True)
    cultural_right = models.TextField(null=True)
    lineaments = models.TextField(null=True)
    orientations = models.TextField(null=True)
    value = models.TextField(null=True)
    expertise = models.TextField(null=True)
    characteristics = models.TextField(null=True)
    objective = models.TextField(null=True)
    observations = models.TextField(null=True)
    status = models.TextField(null=True)
    
    def __str__(self):
        return self.user

    class Meta:
        db_table = 'pedagogical_planning_instructors_2023a'
        
class Binnacles2023a(models.Model):
    
    id = models.AutoField(primary_key=True)
    consecutive = models.TextField(null=True)
    user = models.TextField(null=True)
    user_id = models.IntegerField(null=True)
    rol = models.TextField(null=True)
    nac_user = models.TextField(null=True)
    activity = models.TextField(null=True)
    date = models.TextField(null=True)
    start = models.TextField(null=True)
    end = models.TextField(null=True)
    place = models.TextField(null=True)
    pec = models.TextField(null=True)
    pedagogical = models.TextField(null=True)
    nac = models.TextField(null=True)
    expertise = models.TextField(null=True)
    cultural_right = models.TextField(null=True)
    objective = models.TextField(null=True)
    lineaments = models.TextField(null=True)
    orientations = models.TextField(null=True)
    goal_achieved = models.TextField(null=True)
    why = models.TextField(null=True)
    start_0 = models.TextField(null=True)
    development = models.TextField(null=True)
    end_0 = models.TextField(null=True)
    observations = models.TextField(null=True)
    group = models.TextField(null=True)
    number_attendants = models.IntegerField(null=True)
    status = models.TextField(null=True)
    
    def __str__(self):
        return self.user

    class Meta:
        db_table = 'binnacles_2023a'  
    
class CulturalSeedbed2023a(models.Model):
    
    id = models.AutoField(primary_key=True)
    consecutive = models.TextField(null=True)
    seedbed = models.TextField(null=True)
    user = models.TextField(null=True)
    user_id = models.IntegerField(null=True)
    nac_user = models.TextField(null=True)
    rol = models.TextField(null=True)
    date = models.TextField(null=True)
    pec = models.TextField(null=True)
    planning = models.TextField(null=True)
    domain_seedbed = models.TextField(null=True)
    description = models.TextField(null=True)
    objective = models.TextField(null=True)
    participants_seedbed = models.IntegerField(null=True)
    cultural_right = models.TextField(null=True)
    lineament = models.TextField(null=True)
    orientation = models.TextField(null=True)
    expertise = models.TextField(null=True)
    observations = models.TextField(null=True)
    group = models.TextField(null=True)
    number_assitants = models.IntegerField(null=True)
    status = models.TextField(null=True)
    
    def __str__(self):
        return self.user

    class Meta:
        db_table = 'seedbeds_2023a' 
        
class JornalityAsym2023a(models.Model):
    
    id = models.AutoField(primary_key=True)
    consecutive = models.TextField(null=True)
    user = models.TextField(null=True)
    user_id = models.IntegerField(null=True)
    rol = models.TextField(null=True)
    nac_user = models.TextField(null=True)
    nac = models.TextField(null=True)
    rol_0 = models.TextField(null=True)
    user_name = models.TextField(null=True)
    date = models.TextField(null=True)
    start_date = models.TextField(null=True)
    end_date = models.TextField(null=True)
    place = models.TextField(null=True)
    objectives = models.TextField(null=True)
    purpose = models.TextField(null=True)
    topics = models.TextField(null=True)
    perception = models.TextField(null=True)
    dificulties = models.TextField(null=True)
    recommendations = models.TextField(null=True)
    comments = models.TextField(null=True)
    status = models.TextField(null=True)
    
    def __str__(self):
        return self.user

    class Meta:
        db_table = 'jornality_support_asym_2023a' 
        
class JornalityMetho2023a(models.Model):
    
    id = models.AutoField(primary_key=True)
    consecutive = models.TextField(null=True)
    user = models.TextField(null=True)
    user_id = models.IntegerField(null=True)
    rol = models.TextField(null=True)
    nac_user = models.TextField(null=True)
    nac = models.TextField(null=True)
    rol_0 = models.TextField(null=True)
    date = models.TextField(null=True)
    aspects = models.TextField(null=True)
    others = models.TextField(null=True)
    objective = models.TextField(null=True)
    previous_aspects = models.TextField(null=True)
    observations = models.TextField(null=True)
    number_attendees = models.IntegerField(null=True)
    status = models.TextField(null=True)
    
    def __str__(self):
        return self.user

    class Meta:
        db_table = 'jornality_support_metho_2023a'
        
class JornalitySuper2023a(models.Model):
    
    id = models.AutoField(primary_key=True)
    consecutive = models.TextField(null=True)
    user = models.TextField(null=True)
    user_id = models.IntegerField(null=True)
    rol = models.TextField(null=True)
    nac_user = models.TextField(null=True)
    nac = models.TextField(null=True)
    rol_supervised = models.TextField(null=True)
    date = models.TextField(null=True)
    user_supervised = models.TextField(null=True)
    date_registration = models.TextField(null=True)
    address = models.TextField(null=True)
    goal = models.TextField(null=True)
    pedagogical = models.TextField(null=True)
    attendance_list = models.TextField(null=True)
    monitor_pec = models.TextField(null=True)
    description = models.TextField(null=True)
    observations = models.TextField(null=True)
    status = models.TextField(null=True)
    
    def __str__(self):
        return self.user

    class Meta:
        db_table = 'jornality_support_super_2023a'
    
class JornalityPsychosocial2023a(models.Model):
    
    id = models.AutoField(primary_key=True)
    consecutive = models.TextField(null=True)
    user = models.TextField(null=True)
    user_id = models.IntegerField(null=True)
    rol = models.TextField(null=True)
    nac_user = models.TextField(null=True)
    nac = models.TextField(null=True)
    date = models.TextField(null=True)
    start_date = models.TextField(null=True)
    end_date = models.TextField(null=True)
    name_person = models.TextField(null=True)
    rol_0 = models.TextField(null=True)
    objective = models.TextField(null=True)
    development = models.TextField(null=True)
    conclutions = models.TextField(null=True)
    alerts = models.TextField(null=True)
    number_assistants = models.IntegerField(null=True)
    number_monitors = models.IntegerField(null=True)
    status = models.TextField(null=True)
    
    def __str__(self):
        return self.user

    class Meta:
        db_table = 'support_psycho_2023a'
    
    
class StrategysCirculation2023a(models.Model):
    
    id = models.AutoField(primary_key=True)
    consecutive = models.TextField(null=True)
    user = models.TextField(null=True)
    user_id = models.BigIntegerField(null=True)
    rol = models.TextField(null=True)
    nac_user = models.TextField(null=True)
    activity = models.TextField(null=True)
    date = models.TextField(null=True)
    start_date = models.TextField(null=True)
    end_date = models.TextField(null=True)
    place = models.TextField(null=True)
    nac = models.TextField(null=True)
    expertise = models.TextField(null=True)
    cultural_right = models.TextField(null=True)
    objective = models.TextField(null=True)
    lineament = models.TextField(null=True)
    orientation = models.TextField(null=True)
    goal_achieved = models.TextField(null=True)
    why = models.TextField(null=True)
    start = models.TextField(null=True)
    development = models.TextField(null=True)
    final = models.TextField(null=True)
    observation = models.TextField(null=True)
    number_attendees = models.IntegerField(null=True)
    status = models.TextField(null=True)
    
    def __str__(self):
        return self.user

    class Meta:
        db_table = 'strategys_circulation_2023a'
    
class Registro2024(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.TextField()
    initial_goal = models.IntegerField(default=0)
    enero = models.IntegerField(default=0)
    febrero = models.IntegerField(default=0)
    marzo = models.IntegerField(default=0)
    abril = models.IntegerField(default=0)
    mayo = models.IntegerField(default=0)
    junio = models.IntegerField(default=0)
    julio = models.IntegerField(default=0)
    agosto = models.IntegerField(default=0)
    septiembre = models.IntegerField(default=0)
    octubre = models.IntegerField(default=0)
    noviembre = models.IntegerField(default=0)
    diciembre = models.IntegerField(default=0)
    quantia = models.IntegerField()
    advance = models.TextField(default=0)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Formatear la fecha como "YYYY-MM-DD"
        return self.date.strftime("%Y-%m-%d %H:%M:%S")
    
    class Meta:
        db_table = 'registros_2024'
        
class GraficoIndicador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    datos = models.TextField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'graphics_indicator'
        
class Monitors2024(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=255)
    cedula_monitor = models.CharField(max_length=255)
    nac_monitor = models.CharField(max_length=255)
    
    marzo_semana_1 = models.IntegerField(default=0)
    marzo_semana_2 = models.IntegerField(default=0)
    marzo_semana_3 = models.IntegerField(default=0)
    marzo_semana_4 = models.IntegerField(default=0)
    
    abril_semana_1 = models.IntegerField(default=0)
    abril_semana_2 = models.IntegerField(default=0)
    abril_semana_3 = models.IntegerField(default=0)
    abril_semana_4 = models.IntegerField(default=0)
    
    mayo_semana_1 = models.IntegerField(default=0)
    mayo_semana_2 = models.IntegerField(default=0)
    mayo_semana_3 = models.IntegerField(default=0)
    mayo_semana_4 = models.IntegerField(default=0)
    
    junio_semana_1 = models.IntegerField(default=0)
    junio_semana_2 = models.IntegerField(default=0)
    junio_semana_3 = models.IntegerField(default=0)
    junio_semana_4 = models.IntegerField(default=0)
    
    julio_semana_1 = models.IntegerField(default=0)
    julio_semana_2 = models.IntegerField(default=0)
    julio_semana_3 = models.IntegerField(default=0)
    julio_semana_4 = models.IntegerField(default=0)
    
    agosto_semana_1 = models.IntegerField(default=0)
    agosto_semana_2 = models.IntegerField(default=0)
    agosto_semana_3 = models.IntegerField(default=0)
    agosto_semana_4 = models.IntegerField(default=0)
    
    septiembre_semana_1 = models.IntegerField(default=0)
    septiembre_semana_2 = models.IntegerField(default=0)
    septiembre_semana_3 = models.IntegerField(default=0)
    septiembre_semana_4 = models.IntegerField(default=0)
    
    octubre_semana_1 = models.IntegerField(default=0)
    octubre_semana_2 = models.IntegerField(default=0)
    octubre_semana_3 = models.IntegerField(default=0)
    octubre_semana_4 = models.IntegerField(default=0)
    
    noviembre_semana_1 = models.IntegerField(default=0)
    noviembre_semana_2 = models.IntegerField(default=0)
    noviembre_semana_3 = models.IntegerField(default=0)
    noviembre_semana_4 = models.IntegerField(default=0)
    
    diciembre_semana_1 = models.IntegerField(default=0)
    diciembre_semana_2 = models.IntegerField(default=0)
    diciembre_semana_3 = models.IntegerField(default=0)
    diciembre_semana_4 = models.IntegerField(default=0)
    
    total_registros_ben = models.CharField(max_length=255)
    
    marzo_semana_1_fp = models.IntegerField(default=0)
    marzo_semana_2_fp = models.IntegerField(default=0)
    marzo_semana_3_fp = models.IntegerField(default=0)
    marzo_semana_4_fp = models.IntegerField(default=0)
    
    abril_semana_1_fp = models.IntegerField(default=0)
    abril_semana_2_fp = models.IntegerField(default=0)
    abril_semana_3_fp = models.IntegerField(default=0)
    abril_semana_4_fp = models.IntegerField(default=0)
    
    mayo_semana_1_fp = models.IntegerField(default=0)
    mayo_semana_2_fp = models.IntegerField(default=0)
    mayo_semana_3_fp = models.IntegerField(default=0)
    mayo_semana_4_fp = models.IntegerField(default=0)
    
    junio_semana_1_fp = models.IntegerField(default=0)
    junio_semana_2_fp = models.IntegerField(default=0)
    junio_semana_3_fp = models.IntegerField(default=0)
    junio_semana_4_fp = models.IntegerField(default=0)
    
    julio_semana_1_fp = models.IntegerField(default=0)
    julio_semana_2_fp = models.IntegerField(default=0)
    julio_semana_3_fp = models.IntegerField(default=0)
    julio_semana_4_fp = models.IntegerField(default=0)
    
    agosto_semana_1_fp = models.IntegerField(default=0)
    agosto_semana_2_fp = models.IntegerField(default=0)
    agosto_semana_3_fp = models.IntegerField(default=0)
    agosto_semana_4_fp = models.IntegerField(default=0)
    
    septiembre_semana_1_fp = models.IntegerField(default=0)
    septiembre_semana_2_fp = models.IntegerField(default=0)
    septiembre_semana_3_fp = models.IntegerField(default=0)
    septiembre_semana_4_fp = models.IntegerField(default=0)
    
    octubre_semana_1_fp = models.IntegerField(default=0)
    octubre_semana_2_fp = models.IntegerField(default=0)
    octubre_semana_3_fp = models.IntegerField(default=0)
    octubre_semana_4_fp = models.IntegerField(default=0)
    
    noviembre_semana_1_fp = models.IntegerField(default=0)
    noviembre_semana_2_fp = models.IntegerField(default=0)
    noviembre_semana_3_fp = models.IntegerField(default=0)
    noviembre_semana_4_fp = models.IntegerField(default=0)
    
    diciembre_semana_1_fp = models.IntegerField(default=0)
    diciembre_semana_2_fp = models.IntegerField(default=0)
    diciembre_semana_3_fp = models.IntegerField(default=0)
    diciembre_semana_4_fp = models.IntegerField(default=0)
    
    total_registros_fp = models.CharField(max_length=255)
    
    marzo_semana_1_pacto = models.IntegerField(default=0)
    marzo_semana_2_pacto = models.IntegerField(default=0)
    marzo_semana_3_pacto = models.IntegerField(default=0)
    marzo_semana_4_pacto = models.IntegerField(default=0)
    
    abril_semana_1_pacto = models.IntegerField(default=0)
    abril_semana_2_pacto = models.IntegerField(default=0)
    abril_semana_3_pacto = models.IntegerField(default=0)
    abril_semana_4_pacto = models.IntegerField(default=0)
    
    mayo_semana_1_pacto = models.IntegerField(default=0)
    mayo_semana_2_pacto = models.IntegerField(default=0)
    mayo_semana_3_pacto = models.IntegerField(default=0)
    mayo_semana_4_pacto = models.IntegerField(default=0)
    
    junio_semana_1_pacto = models.IntegerField(default=0)
    junio_semana_2_pacto = models.IntegerField(default=0)
    junio_semana_3_pacto = models.IntegerField(default=0)
    junio_semana_4_pacto = models.IntegerField(default=0)
    
    julio_semana_1_pacto = models.IntegerField(default=0)
    julio_semana_2_pacto = models.IntegerField(default=0)
    julio_semana_3_pacto = models.IntegerField(default=0)
    julio_semana_4_pacto = models.IntegerField(default=0)
    
    agosto_semana_1_pacto = models.IntegerField(default=0)
    agosto_semana_2_pacto = models.IntegerField(default=0)
    agosto_semana_3_pacto = models.IntegerField(default=0)
    agosto_semana_4_pacto = models.IntegerField(default=0)
    
    total_registros_pacto = models.CharField(max_length=255)

    estado = models.CharField(max_length=255)
    
    upload_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'monitors_2024'
        
class PDF(models.Model):
    period = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='pdf_files/')
    observation = models.CharField(max_length=255)
    upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'pdf_file'
        
class Impact2024(models.Model):
    id = models.AutoField(primary_key=True)
    nac = models.CharField(max_length=255)
    beneficiaries = models.IntegerField()
    early_childhood = models.IntegerField()
    childhood = models.IntegerField()
    adolescence = models.IntegerField()
    youth = models.IntegerField()
    adult = models.IntegerField()
    elderly = models.IntegerField()
    high_school = models.IntegerField()
    none_school = models.IntegerField()
    postgraduate = models.IntegerField()
    preschool = models.IntegerField()
    undergraduate = models.IntegerField()
    primary_school = models.IntegerField()
    technical = models.IntegerField()
    technologist = models.IntegerField()
    disability = models.IntegerField()
    non_disability = models.IntegerField()
    afrodescendant = models.IntegerField()
    indigenous = models.IntegerField()
    black = models.IntegerField()
    none_ethnicity = models.IntegerField()
    palenquero = models.IntegerField()
    raizal = models.IntegerField()
    rom = models.IntegerField()
    male = models.IntegerField()
    female = models.IntegerField()
    lgtbiq_plus = models.IntegerField()
    other_gender = models.IntegerField()
    conflict_victims = models.IntegerField()

    def __str__(self):
        return self.nac
    
    class Meta:
        db_table = 'impact_2024'