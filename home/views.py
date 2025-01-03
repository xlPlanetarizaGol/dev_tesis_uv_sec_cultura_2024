from django.shortcuts import render, redirect
from django.shortcuts import render
from django.conf import settings
import os
from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.http import HttpRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from datetime import datetime
from django.db import transaction
from django import forms
import time
from django.core.cache import cache
from django.db import models
from .models import *
from .models import (MediaDissemination2020, DialogueTables2020, Beneficiaries2020, Contracts2020, Transfer2020,
                     SynchronousMeetings2020, Beneficiaries2021a, Binnacles2021a, Instruments2021a,
                     MethodologicalTransfers2021a, MonitoringParticipants2021a, PedagogicalSheets2021a,
                     PlataformTraining2021a, PsychosocialCare2021a, PsychosocialTransfers2021a,
                     MonitoringParticipants2021b, CulturalActivation2021b, FeedbackCulturalActivation2021b,
                     MethodologicalInstructions2021b, PsychosocialInstructions2021b, TerritorialTables2021b,
                     BeneficiariesCapacity2021b, Beneficiaries2021b, PedagogicalSheets2021b, PsychosocialCare2021b,
                     CirculationCultural2021b, ShowArtistic2021b, ValidationUsers2022b, DialogueTables2022b,
                     CulturalActivation2022b, Binnacles2022b, PsychosocialCareAppointments2022b,
                     CulturalSeedbed2022b, CulturalEnsemble2022b, MethodologicalCarpet2022b, ParentsSchool2022b,
                     StrategysCirculation2022b, Beneficiaries2022b, Registro2024, GraficoIndicador, Monitors2024)
import numpy as np

def logout_view(request):
  logout(request)
  return redirect('/accounts/login/')

@login_required(login_url='/accounts/login/')
def profile(request):
  context = {
    'segment': 'profile',
  }
  return render(request, 'pages/profile.html', context)

@login_required(login_url='/accounts/login/')
def sample_page(request):
  context = {
    'segment': 'sample_page',
  }
  return render(request, 'pages/sample-page.html', context)

def index(request):

  context = {
    'segment'  : 'index',
  }
  return render(request, "pages/index.html", context)

# Authentication
class UserRegistrationView(CreateView):
  template_name = 'accounts/auth-signup.html'
  form_class = RegistrationForm
  success_url = '/accounts/login/'

class UserLoginView(LoginView):
  template_name = 'accounts/auth-signin.html'
  form_class = LoginForm

class UserPasswordResetView(PasswordResetView):
  template_name = 'accounts/auth-reset-password.html'
  form_class = UserPasswordResetForm

class UserPasswrodResetConfirmView(PasswordResetConfirmView):
  template_name = 'accounts/auth-password-reset-confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(PasswordChangeView):
  template_name = 'accounts/auth-change-password.html'
  form_class = UserPasswordChangeForm

def logout_view(request):
  logout(request)
  return redirect('/accounts/login/')

@login_required(login_url='/accounts/login/')
def profile(request):
  context = {
    'segment': 'profile',
  }
  return render(request, 'pages/profile.html', context)

@login_required(login_url='/accounts/login/')
def sample_page(request):
  context = {
    'segment': 'sample_page',
  }
  return render(request, 'pages/sample-page.html', context)


@login_required
def obtain_user(request):
    nombre_usuario = request.user.username
    # Hacer algo con el nombre de usuario
    return render(request, 'navigation.html', {'nombre_usuario': nombre_usuario})

@login_required
def listar_media(request):
    media_list = MediaDissemination2020.objects.all()
    return render(request, 'pages/components/2020/media.html', {'media_list': media_list})

@login_required
def listar_dialogue_tables_2020(request):
    diagtab_2020 = DialogueTables2020.objects.all()
    return render(request, 'pages/components/2020/dialogue_tables.html', {'diagtab_2020': diagtab_2020})

@login_required
def listar_beneficiarios_2020(request):
    registros_por_pagina = 100

    all_beneficiaries = Beneficiaries2020.objects.only(
        'id',
        'cultural_monitor',
        'nac_beneficiary',
        'beneficiary_name',
        'document_type',
        'document_number'
    )

    paginator = Paginator(all_beneficiaries, registros_por_pagina)

    page = request.GET.get('page', 1)

    try:
        beneficiaries_page = paginator.page(page)
    except PageNotAnInteger:
        beneficiaries_page = paginator.page(1)
    except EmptyPage:
        beneficiaries_page = paginator.page(paginator.num_pages)

    beneficiaries_2020 = beneficiaries_page.object_list

    return render(request, 'pages/components/2020/beneficiaries.html', {'beneficiaries_2020': beneficiaries_2020})

def listar_acudientes_2020(request):
    registros_por_pagina = 100

    all_beneficiaries = Attendants2020.objects.only(
        'id',
        'cultural_monitor',
        'nac',
        'beneficiary_name',
        'document_type',
        'document_number'
    )

    paginator = Paginator(all_beneficiaries, registros_por_pagina)

    page = request.GET.get('page', 1)

    try:
        beneficiaries_page = paginator.page(page)
    except PageNotAnInteger:
        beneficiaries_page = paginator.page(1)
    except EmptyPage:
        beneficiaries_page = paginator.page(paginator.num_pages)

    attendants_2020 = beneficiaries_page.object_list

    return render(request, 'pages/components/2020/attendants.html', {'attendants_2020': attendants_2020})

@login_required
def listar_contratos_2020(request):
    contratos_2020 = Contracts2020.objects.all()
    return render(request, 'pages/components/2020/contracts.html', {'contratos_2020': contratos_2020})

@login_required
def listar_transfers_2020(request):
    transferencias_2020 = Transfer2020.objects.all()
    return render(request, 'pages/components/2020/transfers.html', {'transferencias_2020': transferencias_2020})

@login_required
def listar_citas_2020(request):
    citas_2020 = PsychosocialCareAppointments2020.objects.all()
    return render(request, 'pages/components/2020/care_appointments.html', {'citas_2020': citas_2020})

@login_required
def listar_sincronicos_2020(request):
    sincronicos_2020 = SynchronousMeetings2020.objects.all()
    return render(request, 'pages/components/2020/synchronous_meetings.html', {'sincronicos_2020': sincronicos_2020})

@login_required
def listar_beneficiarios_2021a(request):
    # Ajusta estos campos según tus necesidades
    fields_to_select = [
        'id',
        'code',
        'monitor_name',
        'nac_tab',
        'name_parents',
        'name_beneficiary',
        'document_number',
        'upload_data',
    ]

    # Aplica paginación en el lado del servidor
    page_size = 100
    page = request.GET.get('page', 1)

    all_beneficiaries = Beneficiaries2021a.objects.values(*fields_to_select)

    paginator = Paginator(all_beneficiaries, page_size)

    try:
        beneficiaries_page = paginator.page(page)
    except PageNotAnInteger:
        beneficiaries_page = paginator.page(1)
    except EmptyPage:
        beneficiaries_page = paginator.page(paginator.num_pages)

    return render(request, 'pages/components/2021a/beneficiaries.html', {'beneficiaries_2021a': beneficiaries_page})

@login_required
def listar_bitacoras_2021a(request):
    bitacoras_2021a = Binnacles2021a.objects.all()
    return render(request, 'pages/components/2021a/binnacles.html', {'bitacoras_2021a': bitacoras_2021a})

@login_required
def listar_dialogue_tables_2021a(request):
    dialogue_tables_2021a = DialogueTables2021a.objects.all()
    return render(request, 'pages/components/2021a/dialogue_tables.html', {'dialogue_tables_2021a': dialogue_tables_2021a})

@login_required
def listar_instruments_2021a(request):
    instruments_2021a = Instruments2021a.objects.all()
    return render(request, 'pages/components/2021a/instruments.html', {'instruments_2021a': instruments_2021a})

@login_required
def listar_metho_transf_2021a(request):
    metho_transf_2021a = MethodologicalTransfers2021a.objects.all()
    return render(request, 'pages/components/2021a/methodological_transfers.html', {'metho_transf_2021a': metho_transf_2021a})

@login_required
def listar_beneficiarios_impacto(request):
    beneficiaries_impacto_2021a = MonitoringParticipants2021a.objects.all()
    return render(request, 'pages/components/2021a/beneficiaries_impact.html', {'beneficiaries_impacto_2021a': beneficiaries_impacto_2021a})

@login_required
def listar_pedagogical_2021a(request):
    pedagogical_2021a = PedagogicalSheets2021a.objects.all()
    return render(request, 'pages/components/2021a/pedagogical_sheets.html', {'pedagogical_2021a': pedagogical_2021a})

@login_required
def listar_plataform_training_2021a(request):
    training_2021a = PlataformTraining2021a.objects.all()
    return render(request, 'pages/components/2021a/training_plataform.html', {'training_2021a': training_2021a})

@login_required
def listar_psychosocial_2021a(request):
    psychosocial_care_2021a = PsychosocialCare2021a.objects.all()
    return render(request, 'pages/components/2021a/psychosocial_care.html', {'psychosocial_care_2021a': psychosocial_care_2021a})

@login_required
def listar_psycho_transfer_2021a(request):
    psychosocial_transfer_2021a = PsychosocialTransfers2021a.objects.all()
    return render(request, 'pages/components/2021a/psychosocial_transfers.html', {'psychosocial_transfer_2021a': psychosocial_transfer_2021a})

@login_required
def listar_follow_participants_2021b(request):
    beneficiaries_impacto_2021b = MonitoringParticipants2021b.objects.all()
    return render(request, 'pages/components/2021b_2022a/beneficiaries_impact.html', {'beneficiaries_impacto_2021b': beneficiaries_impacto_2021b})

@login_required
def listar_actcultural_2021b(request):
    cultural_activation_2021b = CulturalActivation2021b.objects.all()
    return render(request, 'pages/components/2021b_2022a/cultural_activation.html', {'cultural_activation_2021b': cultural_activation_2021b})

@login_required
def listar_feedactcultural_2021b(request):
    feed_cultural_activation_2021b = FeedbackCulturalActivation2021b.objects.all()
    return render(request, 'pages/components/2021b_2022a/feedback_cultural_activation.html', {'feed_cultural_activation_2021b': feed_cultural_activation_2021b})

@login_required
def listar_metho_instruc_2021b(request):
    metho_instruc_2021b = MethodologicalInstructions2021b.objects.all()
    return render(request, 'pages/components/2021b_2022a/methodological_instructions.html', {'metho_instruc_2021b': metho_instruc_2021b})

@login_required
def listar_psycho_instruc_2021b(request):
    psycho_instruc_2021b = PsychosocialInstructions2021b.objects.all()
    return render(request, 'pages/components/2021b_2022a/psychosocial_instructions.html', {'psycho_instruc_2021b': psycho_instruc_2021b})

@login_required
def listar_territorial_tables_2021b(request):
    territorial_2021b = TerritorialTables2021b.objects.all()
    return render(request, 'pages/components/2021b_2022a/territorial_tables.html', {'territorial_2021b': territorial_2021b})

@login_required
def listar_ben_capacity_2021b(request):
    beneficiaries_cap_2021b = BeneficiariesCapacity2021b.objects.all()
    return render(request, 'pages/components/2021b_2022a/beneficiaries_capacity.html', {'beneficiaries_cap_2021b': beneficiaries_cap_2021b})

@login_required


def listar_beneficiaries_2021b(request):
    # Obtener todos los objetos de Beneficiaries2021b
    all_beneficiaries_2021b = Beneficiaries2021b.objects.all()

    # Configurar el paginador con un tamaño de página de 10,000
    paginator = Paginator(all_beneficiaries_2021b, 10000)

    # Obtener el número de página de la solicitud GET, o usar la primera página por defecto
    page_number = request.GET.get('page', 1)

    # Obtener los objetos para la página especificada
    beneficiaries_2021b_page = paginator.get_page(page_number)

    # Renderizar la plantilla con los datos paginados
    return render(request, 'pages/components/2021b_2022a/beneficiaries.html', {'beneficiaries_2021b': beneficiaries_2021b_page})


   

@login_required
def listar_pedagogical_2021b(request):
    pedagogical_2021b = PedagogicalSheets2021b.objects.all()
    return render(request, 'pages/components/2021b_2022a/pedagogical_sheets.html', {'pedagogical_2021b': pedagogical_2021b})

@login_required
def listar_dev_cultural_act_2021b(request):
    dev_cultural_activation_2021b = DevCulturalActivation2021b.objects.all()
    return render(request, 'pages/components/2021b_2022a/binnacles.html', {'dev_cultural_activation_2021b': dev_cultural_activation_2021b})

@login_required
def listar_psychosocial_2021b(request):
    psychosocial_care_2021b = PsychosocialCare2021b.objects.all()
    return render(request, 'pages/components/2021b_2022a/psychosocial_care.html', {'psychosocial_care_2021b': psychosocial_care_2021b})

@login_required
def listar_circulations_cultural_2021b(request):
    circulations_2021b = CirculationCultural2021b.objects.all()
    return render(request, 'pages/components/2021b_2022a/circulation_cultural.html', {'circulations_2021b': circulations_2021b})

@login_required
def listar_artistic_sample_2021b(request):
    artistic_sample_2021b = ShowArtistic2021b.objects.all()
    return render(request, 'pages/components/2021b_2022a/artistic_sample.html', {'artistic_sample_2021b': artistic_sample_2021b})

@login_required
def listar_validation_users_2022b(request):
    validation_users_2022b = ValidationUsers2022b.objects.all()
    return render(request, 'pages/components/2022b/validation_users.html', {'validation_users_2022b': validation_users_2022b})

@login_required
def listar_dialogue_tables_2022b(request):
    dialogue_tables_2022b = DialogueTables2022b.objects.all()
    return render(request, 'pages/components/2022b/dialogue_tables.html', {'dialogue_tables_2022b': dialogue_tables_2022b})

@login_required
def listar_cut_act_2022b(request):
    cultural_act_2022b = CulturalActivation2022b.objects.all()
    return render(request, 'pages/components/2022b/cultural_activation.html', {'cultural_act_2022b': cultural_act_2022b})

@login_required
def listar_metho_instruct_2022b(request):
    metho_instruc_2022b = MethodologicalInstructions2022b.objects.all()
    return render(request, 'pages/components/2022b/methodological_instructions.html', {'metho_instruc_2022b': metho_instruc_2022b})

@login_required
def listar_psycho_instruc_2022b(request):
    psycho_instruc_2022b = PsychosocialInstructions2022b.objects.all()
    return render(request, 'pages/components/2022b/psychosocial_instructions.html', {'psycho_instruc_2022b': psycho_instruc_2022b})

@login_required
def listar_pedagogical_2022b(request):
    pedagogical_2022b = PedagogicalSheets2022b.objects.all()
    return render(request, 'pages/components/2022b/pedagogical_sheets.html', {'pedagogical_2022b': pedagogical_2022b})

@login_required
def listar_binnacles_2022b(request):
    binnacles_2022b = Binnacles2022b.objects.all()
    return render(request, 'pages/components/2022b/binnacles.html', {'binnacles_2022b': binnacles_2022b})

@login_required
def listar_care_2022b(request):
    care_2022b = PsychosocialCareAppointments2022b.objects.all()
    return render(request, 'pages/components/2022b/psychosocial_care.html', {'care_2022b': care_2022b})

@login_required
def listar_seedbed_2022b(request):
    cultural_seedbed_2022b = CulturalSeedbed2022b.objects.all()
    return render(request, 'pages/components/2022b/cultural_seedbed.html', {'cultural_seedbed_2022b': cultural_seedbed_2022b})
    
@login_required
def listar_ensemble_2022b(request):
    cultural_ensemble_2022b = CulturalEnsemble2022b.objects.all()
    return render(request, 'pages/components/2022b/cultural_ensemble.html', {'cultural_ensemble_2022b': cultural_ensemble_2022b})

@login_required
def listar_tap_metho_2022b(request):
    tap_metho_2022b = MethodologicalCarpet2022b.objects.all()
    return render(request, 'pages/components/2022b/methodological_carpet.html', {'tap_metho_2022b': tap_metho_2022b})

@login_required
def listar_parents_2022b(request):
    parents_school_2022b = ParentsSchool2022b.objects.all()
    return render(request, 'pages/components/2022b/parents_school.html', {'parents_school_2022b': parents_school_2022b})

@login_required
def listar_strategys_2022b(request):
    strategys_circulation_2022b = StrategysCirculation2022b.objects.all()
    return render(request, 'pages/components/2022b/strategys_circulation.html', {'strategys_circulation_2022b': strategys_circulation_2022b})

@login_required
def listar_beneficiaries_2022b(request):
    beneficiaries_2022b = Beneficiaries2022b.objects.all()
    return render(request, 'pages/components/2022b/beneficiaries.html', {'beneficiaries_2022b': beneficiaries_2022b})    

@login_required
def listar_beneficiaries_capacity_2022b(request):
    beneficiaries__capacity_2022b = BeneficiariesCapacity2021b.objects.all()
    return render(request, 'pages/components/2022b/beneficiaries_capacity.html', {'beneficiaries__capacity_2022b': beneficiaries__capacity_2022b})

#2020

def cs_2020(request):
    return render(request, 'pages/components/2020/sociodemographic.html') 

def an_2020(request):
    return render(request, 'pages/components/2020/join_annexes.html')

def ct_2020(request):
    return render(request, 'pages/components/2020/dash_contracts.html')      

#2021a

def cs_2021a(request):
    return render(request, 'pages/components/2021a/sociodemographic.html') 

def ca_2021a(request):
    return render(request, 'pages/components/2021a/cultural_activities.html') 

def dc_2021a(request):
    return render(request, 'pages/components/2021a/cultural_dialogues.html') 

def tr_2021a(request):
    return render(request, 'pages/components/2021a/transfers.html') 

def fpd_2021a(request):
    return render(request, 'pages/components/2021a/dash_pedagogical.html') 

def cap_2021a(request):
    return render(request, 'pages/components/2021a/dash_care_appointments.html') 

def icp_2021a(request):
    return render(request, 'pages/components/2021a/dash_instruments.html')

def rank_2021a(request):
    return render(request, 'pages/components/2021a/rank_2021a.html')

def rank_2021b_2022a(request):
    return render(request, 'pages/components/2021b_2022a/rank_2021b_2022a.html')

def rank_2022b(request):
    return render(request, 'pages/components/2022b/rank_2022b.html')

def rank_2020(request):
    return render(request, 'pages/components/2020/rank_2020.html')

#2021b_2022a

def cs_2021b_2022a(request):
    return render(request, 'pages/components/2021b_2022a/dash_sociodemographic.html')

def bjp_2021b_2022a(request):
    return render(request, 'pages/components/2021b_2022a/dash_binnacles.html')

def ac_2021b_2022a(request):
    return render(request, 'pages/components/2021b_2022a/dash_activations.html')

def fed_2021b_2022a(request):
    return render(request, 'pages/components/2021b_2022a/dash_feedback.html')

def im_2021b_2022a(request):
    return render(request, 'pages/components/2021b_2022a/dash_methodological_instructions.html')

def fp_2021b_2022a(request):
    return render(request, 'pages/components/2021b_2022a/dash_pedagogicals.html')

def cap_2021b_2022a(request):
    return render(request, 'pages/components/2021b_2022a/dash_care_appointments.html')

def ip_2021b_2022a(request):
    return render(request, 'pages/components/2021b_2022a/dash_psycho_instructions.html')

def mt_2021b_2022a(request):
    return render(request, 'pages/components/2021b_2022a/dash_territorials.html')

#2022b

def cs_2022b(request):
    return render(request, 'pages/components/2022b/dash_sociodemographic.html')      

def bjp_2022b(request):
    return render(request, 'pages/components/2022b/dash_binnacles.html')

def fp_2022b(request):
    return render(request, 'pages/components/2022b/dash_pedagogicals.html')

def ac_2022b(request):
    return render(request, 'pages/components/2022b/dash_activations.html')

def ec_2022b(request):
    return render(request, 'pages/components/2022b/dash_ensembles.html')

def sc_2022b(request):
    return render(request, 'pages/components/2022b/dash_seedbeds.html')

def md_2022b(request):
    return render(request, 'pages/components/2022b/dash_dialogues.html')

def tpm_2022b(request):
    return render(request, 'pages/components/2022b/dash_carpet.html')

def ep_2022b(request):
    return render(request, 'pages/components/2022b/dash_parents.html')

def cap_2022b(request):
    return render(request, 'pages/components/2022b/dash_care_appointments.html')

def sv_2022b(request):
    return render(request, 'pages/components/2022b/dash_estragies.html')

def cantidades_2024(request):
    return render(request, 'pages/components/2024/payment_monitors.html')

#2023a

def listar_means_verification(request):
    means_verification_2023a = MeansVerification2023a.objects.all()
    return render(request, 'pages/components/2023a/means_verification.html', {'means_verification_2023a': means_verification_2023a})

def listar_verification_follow(request):
    verification_follow_2023a = VerificationFollow2023a.objects.all()
    return render(request, 'pages/components/2023a/verification_follow.html', {'verification_follow_2023a': verification_follow_2023a})

def listar_dialogue_tables(request):
    dialogue_tables_2023a= DialogueTables2023a.objects.all()
    return render(request, 'pages/components/2023a/dialogue_table.html', {'dialogue_tables_2023a': dialogue_tables_2023a})

def listar_activations(request):
    activations_2023 = Activations2023a.objects.all()
    return render(request, 'pages/components/2023a/activations.html', {'activations_2023': activations_2023})

def listar_circulation(request):
    circulations_2023 = Circulation2023a.objects.all()
    return render(request, 'pages/components/2023a/circulations.html', {'circulations_2023': circulations_2023})

def listar_show_cultural(request):
    show_cultural_2023 = ShowCultural2023a.objects.all()
    return render(request, 'pages/components/2023a/show_cultural.html', {'show_cultural_2023': show_cultural_2023})

def listar_ensamble(request):
    ensamble_2023 = Ensamble2023a.objects.all()
    return render(request, 'pages/components/2023a/ensamble.html', {'ensamble_2023': ensamble_2023})

def listar_transfer_methodological(request):
    transfer_metho_2023a = TransferMethodological2023a.objects.all()
    return render(request, 'pages/components/2023a/transfer_methodological.html', {'transfer_metho_2023a': transfer_metho_2023a})

def listar_transfer_psychosocial(request):
    transfer_psychosocial_2023a = TransferPsychosocial2023a.objects.all()
    return render(request, 'pages/components/2023a/transfer_psycho.html', {'transfer_psychosocial_2023a': transfer_psychosocial_2023a})

def listar_planning_monitors(request):
    planning_monitors_2023a = PlanningMonitors2023a.objects.all()
    return render(request, 'pages/components/2023a/planning_monitors.html', {'planning_monitors_2023a': planning_monitors_2023a})

def listar_planning_instructors(request):
    planning_instructors_2023a = PlanningInstructors2023a.objects.all()
    return render(request, 'pages/components/2023a/planning_instructors.html', {'planning_instructors_2023a': planning_instructors_2023a})

def listar_binnacles(request):
    binnacles_2023a = Binnacles2023a.objects.all()
    return render(request, 'pages/components/2023a/binnacles.html', {'binnacles_2023a': binnacles_2023a})

def listar_cultural_seedbed(request):
    seedbeds_2023a = CulturalSeedbed2023a.objects.all()
    return render(request, 'pages/components/2023a/cultural_seedbed.html', {'seedbeds_2023a': seedbeds_2023a})

def listar_jornality_asym(request):
    jornality_asym_2023a = JornalityAsym2023a.objects.all()
    return render(request, 'pages/components/2023a/jornality_asym.html', {'jornality_asym_2023a': jornality_asym_2023a})

def listar_jornality_metho(request):
    jornality_metho_2023a = JornalityMetho2023a.objects.all()
    return render(request, 'pages/components/2023a/jornality_metho.html', {'jornality_metho_2023a': jornality_metho_2023a})

def listar_jornality_super(request):
    jornality_super_2023a = JornalitySuper2023a.objects.all()
    return render(request, 'pages/components/2023a/jornality_super.html', {'jornality_super_2023a': jornality_super_2023a})

def listar_jornality_psychosocial(request):
    jornality_psycho_2023a = JornalityPsychosocial2023a.objects.all()
    return render(request, 'pages/components/2023a/jornality_psycho.html', {'jornality_psycho_2023a': jornality_psycho_2023a})

def listar_strategys_circulation(request):
    stategys_circulation_2023a = StrategysCirculation2023a.objects.all()
    return render(request, 'pages/components/2023a/strategys_circulation.html', {'stategys_circulation_2023a': stategys_circulation_2023a})

def pb_2023a(request):
    return render(request, 'pages/components/2023a/dash_sociodemographic.html')

def ac_2023a(request):
    return render(request, 'pages/components/2023a/dash_activations.html')

def eb_2023a(request):
    return render(request, 'pages/components/2023a/dash_assembly.html')

def cc_2023a(request):
    return render(request, 'pages/components/2023a/dash_circulation.html')

def sd_2023a(request):
    return render(request, 'pages/components/2023a/dash_seedbed.html')

def js_2023a(request):
    return render(request, 'pages/components/2023a/dash_jornality.html')

def pd_2023a(request):
    return render(request, 'pages/components/2023a/dash_pedagogicals.html')

def sc_2023a(request):
    return render(request, 'pages/components/2023a/dash_show_cultural.html')

def tr_2023a(request):
    return render(request, 'pages/components/2023a/dash_transfer.html')

def btp_2023a(request):
    return render(request, 'pages/components/2023a/dash_psicopedagogicals.html')

def rank_2023a(request):
    return render(request, 'pages/components/2023a/rank_2023a.html')

def mc_2024(request):
    return render(request, 'pages/components/2024/cultural_marginalization.html')

class ArchivoForm(forms.Form):
    archivos = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

import plotly.graph_objs as go
from datetime import datetime
import pandas as pd
from plotly.offline import plot

def get_registros_2024():
    return Registro2024.objects.all()

def parse_date(date_str):
    if date_str.startswith('00'):
        # Reemplaza el año con uno más apropiado, por ejemplo, 2023
        date_str = '2023' + date_str[4:]
    return pd.to_datetime(date_str)

def indicadores_2024(request):
    datos_indicadores = None
    graficos_indicadores = None
    meta_beneficiarios = 41200
    meta_activaciones = 816
    meta_circulaciones = 1000
    meta_ensamble = 3000
    meta_usuarios = 700
    meta_fichas_ped = 13000
    meta_bitacoras = 41200
    meta_mesas_dialogo = 2000
    meta_instruc_meto = 1500
    meta_semilleros = 12000
    meta_escuelas_padres = 400
    meta_citas_atencion =  1500
    meta_instruc_psico = 800
    meta_show_cultural = 3000
    
    registros_2024 = get_registros_2024()
    
    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                archivos = request.FILES.getlist('archivos')
                
                # Palabras clave para identificar los archivos
                palabras_clave = ['beneficiarios', 'activación', 'circulación', 'ensamble', 'embajadores',
                                'usuarios', 'pedagógicos', 'monitores', 'mesa',
                                'metodológica', 'semilleros', 'escuela',
                                'psicopedagógica', 'psicosocial']
                
                # Diccionario para mapear nombres de archivo a variables
                archivos_dict = {}

                # Iterar sobre los archivos y mapearlos por nombre
                for archivo in archivos:
                    nombre_archivo = archivo.name
                    # Verificar si el nombre del archivo contiene al menos una palabra clave
                    for palabra in palabras_clave:
                        if palabra in nombre_archivo.lower():
                            archivos_dict[palabra] = archivo
                            break  # Salir del bucle cuando se encuentra una palabra clave

                # Obtener los archivos según sus nombres
                archivo_beneficiarios_excel = archivos_dict.get('beneficiarios')
                activaciones_excel = archivos_dict.get('activación')
                circulaciones_excel = archivos_dict.get('circulación')
                ensamble_excel = archivos_dict.get('ensamble')
                show_cultural_excel = archivos_dict.get('embajadores')
                archivo_usuarios_excel = archivos_dict.get('usuarios')
                archivo_pedagogicas_excel = archivos_dict.get('pedagógicos')
                archivo_bitacoras_pacto_excel = archivos_dict.get('monitores')
                mesas_excel = archivos_dict.get('mesa')
                instrucciones_meto_excel = archivos_dict.get('metodológica')
                semilleros_excel = archivos_dict.get('semilleros')
                escuelas_excel = archivos_dict.get('escuela')
                psicopedagogica_excel = archivos_dict.get('psicopedagógica')
                instrucciones_psico_excel = archivos_dict.get('psicosocial')

                # Procesamiento de archivos y cálculo de indicadores

                # Beneficiarios
                df_beneficiarios = pd.read_excel(archivo_beneficiarios_excel)
                df_beneficiarios = df_beneficiarios[df_beneficiarios['USUARIO'] != "Prueba monitor"]
                registros_beneficiarios = len(df_beneficiarios)
                
                df_beneficiarios['FECHA DE CARGUE'] = pd.to_datetime(df_beneficiarios['FECHA DE CARGUE'])
                beneficiarios_por_mes = df_beneficiarios['FECHA DE CARGUE'].dt.month.value_counts().sort_index()
                
                if meta_beneficiarios > 0:
                    porcentaje_avance_ben = (registros_beneficiarios / meta_beneficiarios) * 100
                else:
                    porcentaje_avance_ben = 0 
                    
                # Usuarios
                df_usuarios = pd.read_excel(archivo_usuarios_excel)
                df_usuarios = df_usuarios[~df_usuarios['NOMBRE COMPLETO'].str.contains('Prueba', case=False)]
                cantidad_usuarios = len(df_usuarios)
                df_usuarios['FECHA DE CREACION'] = pd.to_datetime(df_usuarios['FECHA DE CREACION'])
                usuarios_por_mes =  df_usuarios['FECHA DE CREACION'].dt.month.value_counts().sort_index()
                
                if meta_usuarios > 0:
                    porcentaje_avance_user = (cantidad_usuarios / meta_usuarios) * 100
                else:
                    porcentaje_avance_user = 0
                
                # Activaciones
                df_activaciones = pd.read_excel(activaciones_excel)
                df_activaciones = df_activaciones[~df_activaciones['USUARIO'].str.contains('Prueba', case=False)]
                df_activaciones['FECHA DE CARGUE'] = pd.to_datetime(df_activaciones['FECHA DE CARGUE'])
                cantidad_activaciones = len(df_activaciones)
                df_activaciones['FECHA DE ACTIVIDAD'] = pd.to_datetime(df_activaciones['FECHA DE ACTIVIDAD'])
                # Ahora puedes usar el método .dt para extraer componentes de fecha
                activaciones_por_mes = df_activaciones['FECHA DE ACTIVIDAD'].dt.month.value_counts().sort_index()
                                
                if meta_activaciones > 0:
                    porcentaje_avance_act = (cantidad_activaciones / meta_activaciones) * 100
                else:
                    porcentaje_avance_act = 0
                
                # Circulaciones
                df_circulaciones = pd.read_excel(circulaciones_excel)
                df_circulaciones = df_circulaciones[~df_circulaciones['USUARIO'].str.contains('Prueba', case=False)]
                df_circulaciones['FECHA CREACION'] = pd.to_datetime(df_circulaciones['FECHA CREACION'])
                cantidad_circulaciones = len(df_circulaciones)
                df_circulaciones['FECHA ACTIVIDAD'] = pd.to_datetime(df_circulaciones['FECHA ACTIVIDAD'], errors='coerce')
                circulaciones_por_mes = df_circulaciones['FECHA ACTIVIDAD'].dt.month.value_counts().sort_index()
                                                
                if meta_circulaciones > 0:
                    porcentaje_avance_cir = (cantidad_circulaciones / meta_circulaciones) * 100
                else:
                    porcentaje_avance_cir = 0

                # Ensamble
                df_ensamble = pd.read_excel(ensamble_excel)
                df_ensamble = df_ensamble[~df_ensamble['USUARIO'].str.contains('Prueba', case=False)]
                df_ensamble['FECHA CREACION'] = pd.to_datetime(df_ensamble['FECHA CREACION'])
                cantidad_ensamble = len(df_ensamble)
                df_ensamble['FECHA'] = pd.to_datetime(df_ensamble['FECHA'], errors='coerce')
                ensamble_por_mes = df_ensamble['FECHA'].dt.month.value_counts().sort_index()
                                                                
                if meta_ensamble > 0:
                    porcentaje_avance_ens = (cantidad_ensamble / meta_ensamble) * 100
                else:
                    porcentaje_avance_ens = 0

                # Show Cultural
                df_show_cultural = pd.read_excel(show_cultural_excel)
                df_show_cultural = df_show_cultural[~df_show_cultural['USUARIO'].str.contains('Prueba', case=False)]
                df_show_cultural['FECHA DE CREACION'] = pd.to_datetime(df_show_cultural['FECHA DE CREACION'])
                cantidad_show_cultural = len(df_show_cultural)
                df_show_cultural['FECHA DE LA ACTIVIDAD'] = pd.to_datetime(df_show_cultural['FECHA DE LA ACTIVIDAD'], errors='coerce')
                show_cultural_por_mes = df_show_cultural['FECHA DE LA ACTIVIDAD'].dt.month.value_counts().sort_index()
                                                
                if meta_show_cultural > 0:
                    porcentaje_avance_show = (cantidad_show_cultural / meta_show_cultural) * 100
                else:
                    porcentaje_avance_show = 0

                # Pedagógicos
                df_pedagogicas = pd.read_excel(archivo_pedagogicas_excel, parse_dates=['FECHA DE ACTIVIDAD'])
                df_pedagogicas = df_pedagogicas[~df_pedagogicas['USUARIO'].str.contains('Prueba', case=False)]
                registros_pedagogicas = len(df_pedagogicas)
                df_pedagogicas['FECHA DE ACTIVIDAD'] = pd.to_datetime(df_pedagogicas['FECHA DE ACTIVIDAD'], errors='coerce')
                fichas_por_mes =  df_pedagogicas['FECHA DE ACTIVIDAD'].dt.month.value_counts().sort_index()
                                                        
                if meta_fichas_ped > 0:
                    porcentaje_avance_ped = (registros_pedagogicas / meta_fichas_ped) * 100
                else:
                    porcentaje_avance_ped = 0
                
                # Indicadores
                velocidad_indicator = create_platform_indicator(registros_beneficiarios)
                usuarios_indicator = create_users_indicator(cantidad_usuarios)
                activaciones_indicator = create_act_real_indicator(cantidad_activaciones)
                pedagogicos_indicator = create_pedagogicos_indicator(registros_pedagogicas) 

                # Bitácoras pacto
                df_bitacoras_pacto = pd.read_excel(archivo_bitacoras_pacto_excel)
                df_bitacoras_pacto = df_bitacoras_pacto[df_bitacoras_pacto['USUARIO'] != "Prueba monitor"]
                df_bitacoras_pacto['FECHA DE CARGUE'] = pd.to_datetime(df_bitacoras_pacto['FECHA DE CARGUE'])
                cantidad_pacto =  len(df_bitacoras_pacto)
                conteo_por_mes = df_bitacoras_pacto['FECHA DE CARGUE'].dt.to_period('M').value_counts().sort_index()
                bitacoras_indicator = create_bitacoras_indicator(conteo_por_mes)
                df_bitacoras_pacto['FECHA DE ACTIVIDAD'] = pd.to_datetime(df_bitacoras_pacto['FECHA DE ACTIVIDAD'], errors='coerce')
                bitacoras_por_mes =  df_bitacoras_pacto['FECHA DE ACTIVIDAD'].dt.month.value_counts().sort_index()
                                                                   
                if meta_bitacoras > 0:
                    porcentaje_avance_bit = (cantidad_pacto / meta_bitacoras) * 100
                else:
                    porcentaje_avance_bit = 0
                mapa_cali_valle = generar_mapa_cali_y_valle(df_beneficiarios, df_bitacoras_pacto, df_pedagogicas)
                #mesas de dialogo
                df_dialogo = pd.read_excel(mesas_excel)
                df_dialogo = df_dialogo[df_dialogo['USUARIO'] != "Prueba"]
                total_dialogo = len(df_dialogo)
                df_dialogo['FECHA DE ACTIVIDAD'] = pd.to_datetime(df_dialogo['FECHA DE ACTIVIDAD'], errors='coerce')
                dialogo_por_mes =  df_dialogo['FECHA DE ACTIVIDAD'].dt.month.value_counts().sort_index()
                                                                        
                if meta_mesas_dialogo > 0:
                    porcentaje_avance_mesas = (total_dialogo / meta_mesas_dialogo) * 100
                else:
                    porcentaje_avance_mesas = 0
                
                #instrucciones metodologicas
                df_in_metodologicas = pd.read_excel(instrucciones_meto_excel)
                df_in_metodologicas = df_in_metodologicas[df_in_metodologicas['USUARIO'] != "Prueba"]
                total_in_metodologicas = len(df_in_metodologicas)
                df_in_metodologicas['FECHA DE ACTIVIDAD'] = pd.to_datetime(df_in_metodologicas['FECHA DE ACTIVIDAD'], errors='coerce')
                metodologicas_por_mes =  df_in_metodologicas['FECHA DE ACTIVIDAD'].dt.month.value_counts().sort_index()
                
                if meta_instruc_meto > 0:
                    porcentaje_avance_ins_met = (total_in_metodologicas / meta_instruc_meto) * 100
                else:
                    porcentaje_avance_ins_met = 0
                     
                #semilleros
                df_semilleros = pd.read_excel(semilleros_excel)
                df_semilleros = df_semilleros[df_semilleros['USUARIO'] != "Prueba"]
                total_semilleros = len(df_semilleros)
                df_semilleros['FECHA'] = pd.to_datetime(df_semilleros['FECHA'], errors='coerce')
                semilleros_por_mes =  df_semilleros['FECHA'].dt.month.value_counts().sort_index()
                                
                if meta_semilleros > 0:
                    porcentaje_avance_semilleros = (total_semilleros / meta_semilleros) * 100
                else:
                    porcentaje_avance_semilleros = 0
                
                #psicosociales
                
                df_escuela = pd.read_excel(escuelas_excel)
                df_escuela = df_escuela[df_escuela['USUARIO'] != "Prueba"]
                total_escuela = len(df_escuela)
                df_escuela['FECHA'] = pd.to_datetime(df_escuela['FECHA'], errors='coerce')
                escuela_por_mes =  df_escuela['FECHA'].dt.month.value_counts().sort_index()
                                            
                if meta_escuelas_padres > 0:
                    porcentaje_avance_esc = (total_escuela / meta_escuelas_padres) * 100
                else:
                    porcentaje_avance_esc = 0
                 
                df_psicopedagogica = pd.read_excel(psicopedagogica_excel)
                df_psicopedagogica = df_psicopedagogica[df_psicopedagogica['USUARIO'] != "Prueba"]
                total_psicopedagogica = len(df_psicopedagogica)
                df_psicopedagogica['FECHA'] = pd.to_datetime(df_psicopedagogica['FECHA'], errors='coerce')
                psicopedagogica_por_mes =  df_psicopedagogica['FECHA'].dt.month.value_counts().sort_index()
                                                            
                if meta_citas_atencion > 0:
                    porcentaje_avance_citas = (total_psicopedagogica / meta_citas_atencion) * 100
                else:
                    porcentaje_avance_citas = 0
                
                df_inst_psico = pd.read_excel(instrucciones_psico_excel)
                df_inst_psico = df_inst_psico[df_inst_psico['PSICOSOCIAL'] != "Prueba"]
                total_ins_psico = len(df_inst_psico)
                df_inst_psico['FECHA DE ACTIVIDAD'] = pd.to_datetime(df_inst_psico['FECHA DE ACTIVIDAD'], errors='coerce')
                inst_psico_por_mes =  df_inst_psico['FECHA DE ACTIVIDAD'].dt.month.value_counts().sort_index()
                
                if meta_instruc_psico > 0:
                    porcentaje_avance_ins_psico = (total_ins_psico / meta_instruc_psico) * 100
                else:
                    porcentaje_avance_ins_psico = 0

                # Unir conteos por mes
                conteos_por_mes_join = {
                    'activaciones': df_activaciones['FECHA DE CARGUE'].dt.to_period('M').value_counts().sort_index(),
                    'circulaciones': df_circulaciones['FECHA CREACION'].dt.to_period('M').value_counts().sort_index(),
                    'ensamble': df_ensamble['FECHA CREACION'].dt.to_period('M').value_counts().sort_index(),
                    'show_cultural': df_show_cultural['FECHA DE CREACION'].dt.to_period('M').value_counts().sort_index()
                }

                join_indicator = create_join_indicator(conteos_por_mes_join)
                
                registros_guardados = []
                
                registros_por_mes_beneficiarios = {mes: 0 for mes in range(1, 13)}
                registros_por_mes_usuarios = {mes: 0 for mes in range(1, 13)}
                registros_por_mes_activaciones = {mes: 0 for mes in range(1, 13)}
                registros_por_mes_fichas = {mes: 0 for mes in range(1, 13)}
                registros_por_mes_bitacoras = {mes: 0 for mes in range(1, 13)}
                registros_por_mes_circulaciones = {mes: 0 for mes in range(1, 13)}
                registros_por_mes_ensamble = {mes: 0 for mes in range(1, 13)}
                registros_por_mes_show_cultural = {mes: 0 for mes in range(1, 13)}
                registros_por_mes_dialogo = {mes: 0 for mes in range(1, 13)}
                registros_por_mes_in_metodologicas = {mes: 0 for mes in range(1, 13)}
                registros_por_mes_semilleros = {mes: 0 for mes in range(1, 13)}
                registros_por_mes_escuelas = {mes: 0 for mes in range(1, 13)}
                registros_por_mes_psicopedagogica = {mes: 0 for mes in range(1, 13)}
                registros_por_mes_in_psicosocial = {mes: 0 for mes in range(1, 13)}

                # Contar registros de beneficiarios por mes
                for mes in range(1, 13):
                    registros_por_mes_beneficiarios[mes] += beneficiarios_por_mes.get(mes, 0)

                # Contar registros de usuarios por mes
                for mes in range(1, 13):
                    registros_por_mes_usuarios[mes] += usuarios_por_mes.get(mes, 0)
                    
                for mes in range(1, 13):
                    registros_por_mes_activaciones[mes] += activaciones_por_mes.get(mes, 0)
                
                for mes in range(1, 13):
                    registros_por_mes_fichas[mes] += fichas_por_mes.get(mes, 0)       
                    
                for mes in range(1, 13):
                    registros_por_mes_bitacoras[mes] += bitacoras_por_mes.get(mes, 0)    
                    
                for mes in range(1, 13):
                    registros_por_mes_circulaciones[mes] += circulaciones_por_mes.get(mes, 0)     
                    
                for mes in range(1, 13):
                    registros_por_mes_ensamble[mes] += ensamble_por_mes.get(mes, 0)    
                    
                for mes in range(1, 13):
                    registros_por_mes_show_cultural[mes] += show_cultural_por_mes.get(mes, 0)
                    
                for mes in range(1, 13):
                    registros_por_mes_dialogo[mes] += dialogo_por_mes.get(mes, 0)    
                                        
                for mes in range(1, 13):
                    registros_por_mes_in_metodologicas[mes] += metodologicas_por_mes.get(mes, 0)  
                    
                for mes in range(1, 13):
                    registros_por_mes_semilleros[mes] += semilleros_por_mes.get(mes, 0)
                                    
                for mes in range(1, 13):
                    registros_por_mes_escuelas[mes] += escuela_por_mes.get(mes, 0)    
                                        
                for mes in range(1, 13):
                    registros_por_mes_psicopedagogica[mes] += psicopedagogica_por_mes.get(mes, 0)  
                    
                for mes in range(1, 13):
                    registros_por_mes_in_psicosocial[mes] += inst_psico_por_mes.get(mes, 0)      
                
                registro_nuevo_beneficiarios = Registro2024(
                    initial_goal=meta_beneficiarios,
                    type='Beneficiarios',
                    quantia=registros_beneficiarios,
                    **{nombre_mes: registros_por_mes_beneficiarios[mes] for mes, nombre_mes in enumerate(['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'], 1)},
                    advance=porcentaje_avance_ben
                )

                registro_nuevo_usuarios = Registro2024(
                    initial_goal=meta_usuarios,
                    type='Usuarios',
                    quantia=cantidad_usuarios,
                    **{nombre_mes: registros_por_mes_usuarios[mes] for mes, nombre_mes in enumerate(['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'], 1)},
                    advance=porcentaje_avance_user
                )
                
                registro_nuevo_activaciones = Registro2024(
                    initial_goal=meta_activaciones,
                    type='Activaciones',
                    quantia=cantidad_activaciones,
                    **{nombre_mes: registros_por_mes_activaciones[mes] for mes, nombre_mes in enumerate(['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'], 1)},
                    advance=porcentaje_avance_act
                )
                
                registro_nuevo_fichas = Registro2024(
                    initial_goal=meta_fichas_ped,
                    type='Fichas Pedagógicas',
                    quantia=registros_pedagogicas,
                    **{nombre_mes: registros_por_mes_fichas[mes] for mes, nombre_mes in enumerate(['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'], 1)},
                    advance=porcentaje_avance_ped
                )
                
                registro_nuevo_pacto = Registro2024(
                    initial_goal=meta_bitacoras,
                    type='Bitácoras Pacto',
                    quantia=cantidad_pacto,
                    **{nombre_mes: registros_por_mes_bitacoras[mes] for mes, nombre_mes in enumerate(['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'], 1)},
                    advance=porcentaje_avance_bit
                )
                
                registro_nuevo_circulaciones = Registro2024(
                    initial_goal=meta_circulaciones,
                    type='Circulaciones',
                    quantia=cantidad_circulaciones,
                    **{nombre_mes: registros_por_mes_circulaciones[mes] for mes, nombre_mes in enumerate(['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'], 1)},
                    advance=porcentaje_avance_cir
                )
                
                registro_nuevo_ensamble = Registro2024(
                    initial_goal=meta_ensamble,
                    type='Ensamble',
                    quantia=cantidad_ensamble,
                    **{nombre_mes: registros_por_mes_ensamble[mes] for mes, nombre_mes in enumerate(['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'], 1)},
                    advance=porcentaje_avance_ens
                )
                                
                registro_nuevo_show_cultural = Registro2024(
                    initial_goal=meta_show_cultural,
                    type='Show Cultural',
                    quantia=cantidad_show_cultural,
                    **{nombre_mes: registros_por_mes_show_cultural[mes] for mes, nombre_mes in enumerate(['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'], 1)},
                    advance=porcentaje_avance_show
                )
                
                registro_nuevo_dialogo = Registro2024(
                    initial_goal=meta_mesas_dialogo,
                    type='Mesas de Diálogo',
                    quantia=total_dialogo,
                    **{nombre_mes: registros_por_mes_dialogo[mes] for mes, nombre_mes in enumerate(['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'], 1)},
                    advance=porcentaje_avance_mesas
                )
                
                registro_nuevo_meto = Registro2024(
                    initial_goal=meta_instruc_meto,
                    type='Instrucciones Metodologicas',
                    quantia=total_in_metodologicas,
                    **{nombre_mes: registros_por_mes_in_metodologicas[mes] for mes, nombre_mes in enumerate(['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'], 1)},
                    advance=porcentaje_avance_ins_met
                )
                
                registro_nuevo_semilleros = Registro2024(
                    initial_goal=meta_semilleros,
                    type='Semilleros',
                    quantia=total_semilleros,
                    **{nombre_mes: registros_por_mes_semilleros[mes] for mes, nombre_mes in enumerate(['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'], 1)},
                    advance=porcentaje_avance_semilleros
                )
                
                registro_nuevo_escuela = Registro2024(
                    initial_goal=meta_escuelas_padres,
                    type='Escuela de Padres',
                    quantia=total_escuela,
                    **{nombre_mes: registros_por_mes_escuelas[mes] for mes, nombre_mes in enumerate(['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'], 1)},
                    advance=porcentaje_avance_esc
                )
                
                registro_nuevo_psicopedagogica = Registro2024(
                    initial_goal=meta_citas_atencion,
                    type='Bitácoras Psicopedagogicas',
                    quantia=total_psicopedagogica,
                    **{nombre_mes: registros_por_mes_psicopedagogica[mes] for mes, nombre_mes in enumerate(['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'], 1)},
                    advance=porcentaje_avance_citas)
                
                registro_nuevo_ins_psico = Registro2024(
                    initial_goal=meta_instruc_psico,
                    type='Instrucciones Psicosociales',
                    quantia=total_ins_psico,
                    **{nombre_mes: registros_por_mes_in_psicosocial[mes] for mes, nombre_mes in enumerate(['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'], 1)},
                    advance=porcentaje_avance_ins_psico
                )
                
                registros_guardados.append(registro_nuevo_beneficiarios)
                registros_guardados.append(registro_nuevo_usuarios)
                registros_guardados.append(registro_nuevo_fichas)
                registros_guardados.append(registro_nuevo_pacto)
                registros_guardados.append(registro_nuevo_circulaciones)
                registros_guardados.append(registro_nuevo_ensamble)
                registros_guardados.append(registro_nuevo_show_cultural)
                registros_guardados.append(registro_nuevo_dialogo)
                registros_guardados.append(registro_nuevo_meto)
                registros_guardados.append(registro_nuevo_activaciones)
                registros_guardados.append(registro_nuevo_semilleros)
                registros_guardados.append(registro_nuevo_escuela)
                registros_guardados.append(registro_nuevo_psicopedagogica)
                registros_guardados.append(registro_nuevo_ins_psico)                   

                Registro2024.objects.bulk_create(registros_guardados)
                
                
                # Renderizar la página con los indicadores

                graficos_indicadores = {
                    'velocidad_indicator': velocidad_indicator,
                    'usuarios_indicator': usuarios_indicator,
                    'activaciones_indicator': activaciones_indicator,
                    'pedagogicos_indicator': pedagogicos_indicator,
                    'bitacoras_indicator': bitacoras_indicator,
                    'join_indicator': join_indicator,
                    
                    
                    'mapa_cali_valle': mapa_cali_valle,
                }

                if graficos_indicadores:
                    try:
                        with transaction.atomic():
                            for nombre, grafico in graficos_indicadores.items():
                                GraficoIndicador.objects.create(nombre=nombre, datos=grafico)
                    except Exception as e:
                        print("Error al guardar los gráficos:", e)

            except Exception as e:
                print("Error:", e)
    else:
        form = ArchivoForm()


        # Recuperar gráficos guardados de la base de datos
        graficos_guardados = GraficoIndicador.objects.all()
        graficos_indicadores = {}

        # Asegurarse de pasar los gráficos recuperados al contexto de renderizado
        for grafico in graficos_guardados:
            graficos_indicadores[grafico.nombre] = grafico.datos
        
    
    # Renderizar la página
    return render(request, 'pages/components/2024/indicadores.html', {
        'form': form,
        'registros_2024': registros_2024,
        'graficos_indicadores': graficos_indicadores,

        
    })   

from .models import Monitors2024
class ArchivoForm(forms.Form):
    archivos = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

from collections import defaultdict
from datetime import datetime
import pandas as pd

def calcular_registros_por_semana(request):
    form = ArchivoForm()  # Siempre se renderiza el formulario
    
    if request.method == 'POST':
        archivos = request.FILES.getlist('archivos')

        # Leer el archivo de beneficiarios
        df_beneficiarios = pd.read_excel(archivos[0])

        # Preparar datos de usuarios de beneficiarios
        usuarios_data_combined = defaultdict(lambda: ({
            'marzo': [0, 0, 0, 0],
            'abril': [0, 0, 0, 0],
            'mayo': [0, 0, 0, 0],
            'junio': [0, 0, 0, 0],
            'julio': [0, 0, 0, 0],
            'agosto': [0, 0, 0, 0]
        }, {
            'marzo': [0, 0, 0, 0],
            'abril': [0, 0, 0, 0],
            'mayo': [0, 0, 0, 0],
            'junio': [0, 0, 0, 0],
            'julio': [0, 0, 0, 0],
            'agosto': [0, 0, 0, 0]
        }))

        # Convertir la columna de fechas a formato datetime si no lo está ya
        df_beneficiarios['FECHA DE CARGUE'] = pd.to_datetime(df_beneficiarios['FECHA DE CARGUE'], errors='coerce')

        # Leer el archivo pedagógico
        df_pedagogico = pd.read_excel(archivos[1])

        # Convertir la columna de fechas a formato datetime si no lo está ya
        df_pedagogico['FECHA DE ACTIVIDAD'] = pd.to_datetime(df_pedagogico['FECHA DE ACTIVIDAD'], errors='coerce')

        for df, tipo_actividad in zip([df_beneficiarios, df_pedagogico], ['beneficiarios', 'pedagogico']):
            for index, month_name in enumerate(['marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto']):
                semanas_por_mes = {
                    'semana_1': (1, 8),
                    'semana_2': (9, 15),
                    'semana_3': (16, 23),
                    'semana_4': (24, 31) if month_name in ['marzo', 'mayo', 'julio', 'agosto'] and month_name != 'junio' and month_name != 'abril' else (24, 30)
                }

                for semana, (start_day, end_day) in semanas_por_mes.items():
                    df_week = df[(df['FECHA DE CARGUE' if tipo_actividad == 'beneficiarios' else 'FECHA DE ACTIVIDAD'].dt.month == index + 3) &
                                            (df['FECHA DE CARGUE' if tipo_actividad == 'beneficiarios' else 'FECHA DE ACTIVIDAD'].dt.day >= start_day) &
                                            (df['FECHA DE CARGUE' if tipo_actividad == 'beneficiarios' else 'FECHA DE ACTIVIDAD'].dt.day <= end_day)]
                    week_num = int(semana.split('_')[1])
                    for usuario in df_week['USUARIO'].unique():
                        beneficiarios_data, pedagogico_data = usuarios_data_combined[usuario]
                        if tipo_actividad == 'beneficiarios':
                            beneficiarios_data[month_name][week_num - 1] += df_week[df_week['USUARIO'] == usuario].shape[0]
                        else:
                            pedagogico_data[month_name][week_num - 1] += df_week[df_week['USUARIO'] == usuario].shape[0]
                        usuarios_data_combined[usuario] = (beneficiarios_data, pedagogico_data)

        monitors_to_create = []
        for usuario, (beneficiarios_data, pedagogico_data) in usuarios_data_combined.items():
            total_registros_ben = sum(sum(semana) for semana in beneficiarios_data.values())
            total_registros_fp = sum(sum(semana) for semana in pedagogico_data.values())
            estado = "APROBADO" if (total_registros_ben + total_registros_fp) > 60 else "NO APROBADO"

            monitors_to_create.append(
                Monitors2024(
                    usuario=usuario,
                    cedula_monitor=df_beneficiarios[df_beneficiarios['USUARIO'] == usuario]['CEDULA USUARIO'].iloc[0],
                    nac_monitor=df_beneficiarios[df_beneficiarios['USUARIO'] == usuario]['NAC USUARIO'].iloc[0],
                    marzo_semana_1 = beneficiarios_data['marzo'][0],
                    marzo_semana_2 = beneficiarios_data['marzo'][1],
                    marzo_semana_3 = beneficiarios_data['marzo'][2],
                    marzo_semana_4 = beneficiarios_data['marzo'][3],

                    abril_semana_1 = beneficiarios_data['abril'][0],
                    abril_semana_2 = beneficiarios_data['abril'][1],
                    abril_semana_3 = beneficiarios_data['abril'][2],
                    abril_semana_4 = beneficiarios_data['abril'][3],

                    mayo_semana_1 = beneficiarios_data['mayo'][0],
                    mayo_semana_2 = beneficiarios_data['mayo'][1],
                    mayo_semana_3 = beneficiarios_data['mayo'][2],
                    mayo_semana_4 = beneficiarios_data['mayo'][3],

                    junio_semana_1 = beneficiarios_data['junio'][0],
                    junio_semana_2 = beneficiarios_data['junio'][1],
                    junio_semana_3 = beneficiarios_data['junio'][2],
                    junio_semana_4 = beneficiarios_data['junio'][3],

                    julio_semana_1 = beneficiarios_data['julio'][0],
                    julio_semana_2 = beneficiarios_data['julio'][1],
                    julio_semana_3 = beneficiarios_data['julio'][2],
                    julio_semana_4 = beneficiarios_data['julio'][3],

                    agosto_semana_1 = beneficiarios_data['agosto'][0],
                    agosto_semana_2 = beneficiarios_data['agosto'][1],
                    agosto_semana_3 = beneficiarios_data['agosto'][2],
                    agosto_semana_4 = beneficiarios_data['agosto'][3],


                    total_registros_ben=total_registros_ben,
                    
                    marzo_semana_1_fp = pedagogico_data['marzo'][0],
                    marzo_semana_2_fp = pedagogico_data['marzo'][1],
                    marzo_semana_3_fp = pedagogico_data['marzo'][2],
                    marzo_semana_4_fp = pedagogico_data['marzo'][3],

                    abril_semana_1_fp = pedagogico_data['abril'][0],
                    abril_semana_2_fp = pedagogico_data['abril'][1],
                    abril_semana_3_fp = pedagogico_data['abril'][2],
                    abril_semana_4_fp = pedagogico_data['abril'][3],

                    mayo_semana_1_fp = pedagogico_data['mayo'][0],
                    mayo_semana_2_fp = pedagogico_data['mayo'][1],
                    mayo_semana_3_fp = pedagogico_data['mayo'][2],
                    mayo_semana_4_fp = pedagogico_data['mayo'][3],

                    junio_semana_1_fp = pedagogico_data['junio'][0],
                    junio_semana_2_fp = pedagogico_data['junio'][1],
                    junio_semana_3_fp = pedagogico_data['junio'][2],
                    junio_semana_4_fp = pedagogico_data['junio'][3],

                    julio_semana_1_fp = pedagogico_data['julio'][0],
                    julio_semana_2_fp = pedagogico_data['julio'][1],
                    julio_semana_3_fp = pedagogico_data['julio'][2],
                    julio_semana_4_fp = pedagogico_data['julio'][3],

                    agosto_semana_1_fp = pedagogico_data['agosto'][0],
                    agosto_semana_2_fp = pedagogico_data['agosto'][1],
                    agosto_semana_3_fp = pedagogico_data['agosto'][2],
                    agosto_semana_4_fp = pedagogico_data['agosto'][3],

                    total_registros_fp=total_registros_fp,
                    estado=estado,
                )
            )
            
        Monitors2024.objects.bulk_create(monitors_to_create)

    fechas_carga_disponibles = Monitors2024.objects.values_list('upload_date', flat=True).distinct()
    fechas_carga_disponibles_formateadas = [fecha.strftime('%Y-%m-%d %H:%M:%S') for fecha in fechas_carga_disponibles]
    
    registros = Monitors2024.objects.all()
    fecha_seleccionada = request.GET.get('fecha_seleccionada')
    if fecha_seleccionada:
        fecha_seleccionada_dt = datetime.strptime(fecha_seleccionada, '%Y-%m-%d %H:%M:%S')
        registros = Monitors2024.objects.filter(upload_date=fecha_seleccionada_dt)

    return render(request, 'pages/components/2024/payment_monitors.html', {'registros': registros, 'form': form, 'fechas_carga': fechas_carga_disponibles_formateadas})



def create_platform_indicator(value):
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=value,
        title={'text': "<b>Beneficiarios</b>", 'font': {'size': 16}},
        domain={'x': [0, 1], 'y': [0, 1]},
        delta={'reference': 41200, 'increasing': {'color': "RebeccaPurple"}},
        gauge={
            'axis': {'range': [0, 41200], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 13733], 'color': 'rgb(255,0,0)'},
                {'range': [13733, 27466], 'color': 'rgb(255,255,0)'},
                {'range': [27466, 41200], 'color': 'rgb(0,255,0)'}],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': value}
        }
    ))
    
    fig.update_layout(autosize=True, margin=dict(l=5, r=5, t=5, b=5),
                      paper_bgcolor="white", font={'color': "darkblue", 'family': "Open Sans"})
    plot_div = fig.to_html(full_html=False, include_plotlyjs=False)
    return plot_div

def create_users_indicator(users_value):
    import plotly.graph_objects as go

    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",  # Modo de indicador con gauge, número y delta
        value=users_value,
        title={'text': "<b>Usuarios</b>", 'font': {'size': 16}},
        domain={'x': [0, 1], 'y': [0, 1]},
        delta={'reference': 700, 'increasing': {'color': "RebeccaPurple"}},
        gauge={
            'axis': {'range': [0, 700], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 233], 'color': 'rgb(255,0,0)'},
                {'range': [233, 466], 'color': 'rgb(255,255,0)'},
                {'range': [466, 700], 'color': 'rgb(0,255,0)'}],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': users_value}
        }
    ))

    fig.update_layout(autosize=True, margin=dict(l=5, r=5, t=5, b=5),
                      paper_bgcolor="white", font={'color': "darkblue", 'family': "Open Sans"})
    plot_div = fig.to_html(full_html=False, include_plotlyjs=False)
    return plot_div


def create_act_real_indicator(value):
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",  # Modo de indicador con gauge, número y delta
        value=value,
        title={'text': "<b>Activaciones Culturales</b>", 'font': {'size': 16}},
        domain={'x': [0, 1], 'y': [0, 1]},
        delta={'reference': 700, 'increasing': {'color': "RebeccaPurple"}},
        gauge={
            'axis': {'range': [0, 700], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 233], 'color': 'rgb(255,0,0)'},
                {'range': [233, 466], 'color': 'rgb(255,255,0)'},
                {'range': [466, 700], 'color': 'rgb(0,255,0)'}],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': value}
        }
    ))


    fig.update_layout(autosize=True, margin=dict(l=5, r=5, t=5, b=5),
                      paper_bgcolor="white", font={'color': "darkblue", 'family': "Open Sans"})
    plot_div = fig.to_html(full_html=False, include_plotlyjs=False)
    return plot_div

def create_pedagogicos_indicator(value):
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",  # Modo de indicador con gauge, número y delta
        value=value,
        title={'text': "<b>Fichas Pedagógicas</b>", 'font': {'size': 16}},
        domain={'x': [0, 1], 'y': [0, 1]},
        delta={'reference': 700, 'increasing': {'color': "RebeccaPurple"}},
        gauge={
            'axis': {'range': [0, 700], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 233], 'color': 'rgb(255,0,0)'},
                {'range': [233, 466], 'color': 'rgb(255,255,0)'},
                {'range': [466, 700], 'color': 'rgb(0,255,0)'}],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': value}
        }
    ))


    fig.update_layout(autosize=True, margin=dict(l=5, r=5, t=5, b=5),
                      paper_bgcolor="white", font={'color': "darkblue", 'family': "Open Sans"})
    plot_div = fig.to_html(full_html=False, include_plotlyjs=False)
    return plot_div

import plotly.graph_objs as go

def create_bitacoras_indicator(conteo_por_mes):
    meses = conteo_por_mes.index.strftime('%Y-%m')
    registros = conteo_por_mes.values

    # Calcular el total de los totales
    total_de_totales = sum(registros)

    # Crear datos para el gráfico de barras
    data_bar = go.Bar(
        x=meses,  # Meses
        y=registros,  # Número de registros por mes
        name='Bitácoras por Mes',
        text=registros,  # Texto que se mostrará encima de cada columna
        textposition='auto',  # Posición del texto (encima de la columna)
        marker=dict(
            color=registros,  # Usar el valor de registros para el degradado de color
            colorscale='Viridis',  # Especificar la escala de color
            colorbar=dict(title='Número de Registros')  # Agregar barra de color
        ),
    )

    # Crear datos para la traza de línea
    data_line = go.Scatter(
        x=meses,
        y=registros,
        mode='lines+markers',
        name='Trayectoria',
        line=dict(color='red', width=2)
    )

    # Configurar el diseño del gráfico
    layout = go.Layout(
        title='<b>Bitácora Jornadas PACTO</b>',
        xaxis=dict(title='Mes'),
        yaxis=dict(title='Número de Registros'),
        bargap=0.2,  # Espacio entre barras
        autosize=True,  # Hacer que el gráfico sea responsive
        paper_bgcolor="white",
        font={'color': "darkblue", 'family': "Open Sans"},
        barmode='group',  # Agrupar las barras
        legend=dict(x=0.1, y=-0.2),  # Posición de la leyenda
    )

    # Crear la figura del gráfico
    fig = go.Figure(data=[data_bar, data_line], layout=layout)

    # Agregar texto con el total de los totales debajo del gráfico
    fig.add_annotation(
        x=0.5,
        y=-0.25,
        text=f'Total de Bitácoras: {total_de_totales}',
        showarrow=False,
        font=dict(size=12, color='black'),
        xref="paper",
        yref="paper"
    )

    # Convertir el gráfico a formato HTML
    plot_div = fig.to_html(full_html=False, include_plotlyjs=False)

    return plot_div

import pandas as pd


def create_join_indicator(conteo_por_mes_join):
    data_barras = []
    
    total_de_totales = 0  # Inicializamos el total de totales
    
    # Iterar sobre las categorías y registros
    for categoria, registros in conteo_por_mes_join.items():
        data_bar = go.Bar(
            x=registros.index.strftime('%Y-%m'),  # Etiquetas de las barras en el eje x (meses)
            y=registros.values,  # Valores de las barras en el eje y
            text=registros.values,  # Texto que se muestra en cada barra
            textposition='inside',  # Colocar el texto dentro de las barras
            name=categoria.title()  # Nombre de la categoría en título
        )
        data_barras.append(data_bar)
        
        total_de_totales += sum(registros.values)  # Sumamos los valores de la categoría actual

    # Configuración del diseño del gráfico
    layout = go.Layout(
        title='<b>Jornadas Artísticas Másivas</b>',
        xaxis=dict(title='Mes'),  # Etiqueta del eje x
        yaxis=dict(title='Número de Registros'),  # Etiqueta del eje y
        autosize=True,  # Hacer que el gráfico sea responsive
        paper_bgcolor="white",
        font={'color': "darkblue", 'family': "Open Sans"},
        barmode='group',  # Agrupar las barras
        legend=dict(x=1.05, y=1),  # Posición de la leyenda al lado derecho del gráfico
    )

    # Crear la figura del gráfico
    fig = go.Figure(data=data_barras, layout=layout)

    fig.add_annotation(
        x=0.5,
        y=-0.25,
        text=f'Total de Bitácoras: {total_de_totales}',
        showarrow=False,
        font=dict(size=12, color='black'),
        xref="paper",
        yref="paper"
    )

    # Convertir el gráfico a formato HTML
    plot_div = fig.to_html(full_html=False, include_plotlyjs=False)

    return plot_div

import pandas as pd
import plotly.express as px

def generar_mapa_cali_y_valle(df_beneficiarios, df_bitacoras_pacto, df_pedagogicas):
    # Datos de Cali
    cali_data = {
        'UBICACION': ['COMUNA 1', 'COMUNA 10', 'COMUNA 11', 'COMUNA 12', 'COMUNA 13', 'COMUNA 14', 'COMUNA 15', 'COMUNA 16', 'COMUNA 17', 'COMUNA 18', 'COMUNA 19', 'COMUNA 2', 'COMUNA 20', 'COMUNA 21', 'COMUNA 22', 'COMUNA 3', 'COMUNA 4', 'COMUNA 5', 'COMUNA 6', 'COMUNA 7', 'COMUNA 8', 'COMUNA 9', 'NODO 23', 'NODO 24', 'NODO 25'],
        'LATITUD': [3.4577833, 3.4204418, 3.42124605, 3.4342329, 3.42803075, 3.4265621, 3.404035, 3.40411065, 3.43722, 3.3817471, 3.42258705, 3.4722468, 3.42015195, 3.42437175, 3.3533442, 3.4505144, 3.47103625, 3.47306925, 3.48588965, 3.455683, 3.4460564, 3.44249145, 3.4464145, 3.32287445, 3.3267755],
        'LONGITUD': [-76.55584405, -76.52819577, -76.51355654, -76.50347065, -76.49155873, -76.47616592, -76.50282783, -76.51543145, -76.5225, -76.55237273, -76.54384227, -76.52314267, -76.56050099, -76.46429514, -76.53543091, -76.53573513, -76.51029824, -76.4950275, -76.48832019, -76.49308366, -76.50407408, -76.52505481, -76.68761171, -76.6096373, -76.4909546]
    }

    # Datos del Valle del Cauca
    valle_data = {
        "UBICACION": ["ALCALÁ", "ANDALUCÍA", "ANSERMANUEVO", "ARGELIA", "BOLÍVAR", "BUENAVENTURA", "BUGA", "BUGALAGRANDE", "CAICEDONIA", "CALIMA - EL DARIÉN", "CANDELARIA", "CARTAGO", "DAGUA", "EL ÁGUILA", "EL CAIRO", "EL CERRITO", "EL DOVIO", "FLORIDA", "GINEBRA", "GUACARÍ", "JAMUNDÍ", "LA CUMBRE", "LA UNIÓN", "LA VICTORIA", "OBANDO", "PALMIRA", "PRADERA", "RESTREPO", "RIOFRÍO", "ROLDANILLO", "SAN PEDRO", "SEVILLA", "TORO", "TRUJILLO", "TULUÁ", "ULLOA", "VERSALLES", "VIJES", "YOTOCO", "YUMBO", "ZARZAL"],
        "LATITUD": [4.67429, 4.1701, 4.79576, 4.72663, 4.333, 3.8801, 3.9, 4.2125, 4.33323, 3.9314, 3.4068, 4.7468, 3.6505, 4.91027, 4.76189, 3.68483, 4.50832, 3.32322, 3.72457, 3.767, 3.26289, 3.64877, 4.533, 4.5254, 4.573, 3.517, 3.41918, 3.8197, 4.1558, 4.4092, 3.9954, 4.2608, 4.6076, 4.2153, 4.083, 4.70359, 4.583, 3.69948, 3.8615, 3.58058, 4.3948],
        "LONGITUD": [-75.7832, -76.1658, -75.9956, -76.12082, -76.183, -77.03116, -76.3, -76.1552, -75.8283, -76.4868, -76.3474, -75.9116, -76.6901, -76.0421, -76.2194, -76.3134, -76.2373, -76.2328, -76.266, -76.333, -76.5384, -76.5679, -76.1, -76.0367, -75.9726, -76.3, -76.2428, -76.522, -76.2872, -76.1535, -76.2286, -75.9313, -76.082, -76.32, -76.2, -75.73791, -76.2, -76.4426, -76.3879, -76.4948, -76.0743]
    }

    # Combinar datos de Cali y Valle del Cauca en un solo DataFrame
    cali_df = pd.DataFrame(cali_data)
    valle_df = pd.DataFrame(valle_data)
    df = pd.concat([cali_df, valle_df])

    # Agregar una columna para distinguir entre Cali y Valle del Cauca
    df['TIPO'] = ['Santiago de Cali'] * len(cali_df) + ['Valle del Cauca'] * len(valle_df)

    # Obtener conteo por NAC en df_beneficiarios
    conteo_beneficiarios_por_nac = df_beneficiarios['NAC'].value_counts()

    # Agregar conteo de beneficiarios por NAC al DataFrame
    df = df.merge(conteo_beneficiarios_por_nac, left_on='UBICACION', right_index=True, how='left')
    df.rename(columns={'NAC': 'Cantidad por NAC'}, inplace=True)

    conteo_bitacoras_por_nac = df_bitacoras_pacto['NAC'].value_counts()
    conteo_bitacoras_por_nac.rename('Bitacoras', inplace=True)
    df = df.merge(conteo_bitacoras_por_nac, left_on='UBICACION', right_index=True, how='left')
    if 'Bitacoras' in df.columns:
        df.rename(columns={'Bitacoras': 'Bitacoras_temp'}, inplace=True)
    df.rename(columns={'Bitacoras_temp': 'Bitacoras'}, inplace=True)

    conteo_pedagogicas_por_nac = df_pedagogicas['NAC'].value_counts()
    conteo_pedagogicas_por_nac.rename('Pedagogicas', inplace=True)
    df = df.merge(conteo_pedagogicas_por_nac, left_on='UBICACION', right_index=True, how='left')
    if 'Pedagogicas' in df.columns:
        df.rename(columns={'Pedagogicas': 'Pedagogicas_temp'}, inplace=True)
    df.rename(columns={'Pedagogicas_temp': 'Pedagogicas'}, inplace=True)

    # Reemplazar los valores faltantes con 0
    df.fillna(0, inplace=True)

    # Calcular los tamaños de los marcadores en función de la cantidad del NAC
    # Crear los tamaños de las bolitas basados en el número de beneficiarios
    size_scale = [5, 10, 15]
    sizes = [size_scale[0] if count < 400 else size_scale[1] if count < 1000 else size_scale[2] for count in df['count']]

    # Crear el scattermapbox con los datos combinados
    fig = px.scatter_mapbox(df, 
                            lat="LATITUD", 
                            lon="LONGITUD", 
                            hover_name="UBICACION",
                            hover_data={'count': True, 'Bitacoras': True, 'Pedagogicas': True},
                            zoom=8,
                            size=sizes, 
                            color='count',
                            color_continuous_scale=px.colors.sequential.Plasma,
                            color_continuous_midpoint=750,  # Establecer el punto medio del color en 750
                            range_color=[0, 1500],
                            center={"lat": 3.8, "lon": -76.575},
                            labels={'UBICACION': 'Ubicación', 'count': 'POBLACIÓN BENEFICIARIA', 'Bitacoras': 'BITÁCORAS PACTO', 'Pedagogicas': 'FICHAS PEDAGÓGICAS'},
                            mapbox_style="carto-positron")

    # Añadir las líneas para conectar las comunas y nodos
    fig.add_scattermapbox(
        mode="lines",
        lat=df["LATITUD"],
        lon=df["LONGITUD"],
        hoverinfo='skip',  # Para evitar que aparezcan los tooltips sobre las líneas
        line=dict(width=2, color="blue"),  # Establecer el ancho y color de la línea
        opacity=0.5,  # Establecer la opacidad de las líneas
    )

    fig.update_layout(
    autosize=True,  # Ajustar dinámicamente el tamaño al contenedor
    margin=dict(l=1, r=1, t=1, b=1),
    yaxis=dict(
        autorange='reversed'  # Invertir el eje y para una disposición vertical
    ),
    mapbox=dict(
        pitch=100  # Inclinar el mapa horizontalmente
    ),
    height=800  # Ajustar la altura del mapa
)
    
    plot_div = fig.to_html(full_html=True, include_plotlyjs=False)
    return plot_div

from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

def eliminar_registros_por_fecha(request):
    if request.method == 'POST' and request.is_ajax():
        fecha_str = request.POST.get('fecha')
        try:
            # Convertir la cadena en un objeto de fecha
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d %H:%M:%S')
            
            # Filtrar y eliminar registros por fecha
            Registro2024.objects.filter(upload_date=fecha).delete()
            
            return JsonResponse({'message': 'Registros eliminados exitosamente.'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
from django.shortcuts import render
from django.http import JsonResponse
from .models import Monitors2024
from datetime import datetime

def eliminar_corte_pago(request):
    if request.method == 'POST' and request.is_ajax():
        fecha_str = request.POST.get('fecha')
        try:
            # Convertir la cadena en un objeto de fecha
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d %H:%M:%S')
            
            # Filtrar y eliminar registros por fecha
            Monitors2024.objects.filter(upload_date=fecha).delete()
            
            return JsonResponse({'message': 'Registros eliminados exitosamente.'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
def obtener_fechas_unicas(request):
    # Obtener todas las fechas únicas de los registros
    fechas_unicas = Monitors2024.objects.values_list('upload_date', flat=True).distinct()

    # Formatear las fechas en el formato deseado
    fechas_unicas_formateadas = [fecha.strftime('%Y-%m-%d %H:%M:%S') for fecha in fechas_unicas]

    return JsonResponse({'fechas_unicas': fechas_unicas_formateadas})

def obtener_fechas_unicas_indicators(request):
    # Obtener todas las fechas únicas de los registros
    fechas_unicas_indicators = Registro2024.objects.values_list('upload_date', flat=True).distinct()

    # Formatear las fechas en el formato deseado
    fechas_unicas_formateadas_indicators = [fechas.strftime('%Y-%m-%d %H:%M:%S') for fechas in fechas_unicas_indicators]

    return JsonResponse({'fechas_unicas_indicators': fechas_unicas_formateadas_indicators})

from django.shortcuts import render, redirect
from django import forms
from .models import PDF
from django.http import HttpResponse


from django.contrib import messages
from django.shortcuts import render, redirect

def pdf_view(request):
    
    if request.method == 'POST':
        period = request.POST.get('period')
        name = request.POST.get('nombre_archivo')
        file = request.FILES.get('file')
        observation = request.POST.get('exampleTextarea')     
        try:
            # Crear un objeto PDF directamente desde los datos del formulario
            PDF.objects.create(period=period, name=name, file=file, observation=observation)
            messages.success(request, 'El archivo se ha cargado correctamente.')
        except Exception as e:
            messages.error(request, f'Ocurrió un error al cargar el archivo: {str(e)}')
        
        return redirect('pdf_view')
    else:

        pass
    
    pdfs = PDF.objects.all()
    return render(request, 'pages/components/reports/create_pdf.html', {'pdfs': pdfs})

def ver_pdf(request):
    pdfs = PDF.objects.all()
    return render(request, 'pages/components/reports/read_pdf.html', {'pdfs': pdfs})

from django.shortcuts import render, redirect, get_object_or_404
from .models import PDF
from django.contrib import messages

def editar_pdf(request, pdf_id):
    pdf = get_object_or_404(PDF, pk=pdf_id)
    
    if request.method == 'POST':
        pdf.period = request.POST.get('period')
        pdf.name = request.POST.get('nombre_archivo')
        pdf.observation = request.POST.get('exampleTextarea')
        
        # Manejar la actualización del archivo solo si se proporciona un nuevo archivo
        if 'file' in request.FILES:
            pdf.file = request.FILES['file']
        
        try:
            pdf.save()
            messages.success(request, 'PDF editado correctamente.')
            return redirect('ver_pdf')
        except Exception as e:
            messages.error(request, f'Ocurrió un error al editar el PDF: {str(e)}')
            
    return render(request, 'pages/components/reports/update_pdf.html', {'pdf': pdf})

def eliminar_pdf(request, pdf_id):
    pdf = get_object_or_404(PDF, pk=pdf_id)
    
    if request.method == 'POST':
        try:
            pdf.delete()
            messages.success(request, 'PDF eliminado correctamente.')
        except Exception as e:
            # Si hay algún error, mostrar un mensaje de error
            messages.error(request, f'Ocurrió un error al eliminar el PDF: {str(e)}')
        
        # Redirigir al usuario de vuelta a la página de ver PDF después de la eliminación
        return redirect('ver_pdf')
    else:
        # Si el método de solicitud no es POST, mostrar un mensaje de error
        messages.error(request, 'La eliminación de PDF solo se permite mediante una solicitud POST.')

        return redirect('ver_pdf')
    
from django.http import HttpResponse
from mimetypes import guess_type
    
def descargar_pdf(request, pdf_id):
    pdf = get_object_or_404(PDF, pk=pdf_id)
    
    if pdf.file:
        content = pdf.file.read()
        # Adivinar el tipo MIME del archivo
        content_type, _ = guess_type(pdf.file.name)
        if not content_type:
            content_type = 'application/octet-stream'
        response = HttpResponse(content, content_type=content_type)
        
        response['Content-Disposition'] = f'attachment; filename="{pdf.file.name}"'
        
        return response
    else:
        return HttpResponse("Archivo no encontrado", status=404)
    
from .models import Impact2024

def impact_2024(request):
    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                archivos = request.FILES.getlist('archivos')
                
                # Palabras clave para identificar los archivos
                palabras_clave = ['beneficiarios']
                
                # Diccionario para mapear nombres de archivo a variables
                archivos_dict = {}

                # Iterar sobre los archivos y mapearlos por nombre
                for archivo in archivos:
                    nombre_archivo = archivo.name
                    # Verificar si el nombre del archivo contiene al menos una palabra clave
                    for palabra in palabras_clave:
                        if palabra in nombre_archivo.lower():
                            archivos_dict[palabra] = archivo
                            break  # Salir del bucle cuando se encuentra una palabra clave

                # Obtener el archivo de beneficiarios según su nombre clave
                archivo_beneficiarios_excel = archivos_dict.get('beneficiarios')

                # Validar que el archivo sea Excel
                if not archivo_beneficiarios_excel.name.endswith('.xls'):
                    raise ValueError("El archivo de beneficiarios no es un archivo Excel válido.")

                # Limpiar el modelo Impact2024
                Impact2024.objects.all().delete()
                
                df = pd.read_excel(archivo_beneficiarios_excel)
                
                # Omitir registros de usuarios de "Prueba monitor"
                df = df[df['USUARIO'] != "Prueba Monitor"]
                
                # Contar el número de registros por valor único en la columna 'NAC'
                conteo_por_nac = df['NAC'].value_counts().to_dict()

                # Iterar sobre los resultados y guardar en el modelo Impact2024
                for nac, count in conteo_por_nac.items():
                    early_childhood_records = df[(df['EDAD'] >= 0) & (df['EDAD'] <= 5) & (df['NAC'] == nac)]
                    childhood_records = df[(df['EDAD'] >= 6) & (df['EDAD'] <= 12) & (df['NAC'] == nac)]
                    adolescence_records = df[(df['EDAD'] >= 13) & (df['EDAD'] <= 17) & (df['NAC'] == nac)]
                    youth_records = df[(df['EDAD'] >= 18) & (df['EDAD'] <= 28) & (df['NAC'] == nac)]
                    adult_records = df[(df['EDAD'] >= 29) & (df['EDAD'] <= 55) & (df['NAC'] == nac)]
                    elderly_records = df[(df['EDAD'] >= 56) & (df['EDAD'] <= 99) & (df['NAC'] == nac)]
                    high_school = df[(df['NAC'] == nac) & (df['¿NIVEL EDUCATIVO ALCANZADO?'] == 'Bachillerato')]
                    none_school = df[(df['NAC'] == nac) & (df['¿NIVEL EDUCATIVO ALCANZADO?'] == 'Ninguno')]
                    postgraduate = df[(df['NAC'] == nac) & (df['¿NIVEL EDUCATIVO ALCANZADO?'] == 'Posgrado')]
                    preschool = df[(df['NAC'] == nac) & (df['¿NIVEL EDUCATIVO ALCANZADO?'] == 'Preescolar')]
                    undergraduate = df[(df['NAC'] == nac) & (df['¿NIVEL EDUCATIVO ALCANZADO?'] == 'Pregrado')]
                    primary_school = df[(df['NAC'] == nac) & (df['¿NIVEL EDUCATIVO ALCANZADO?'] == 'Primaria')]
                    technical = df[(df['NAC'] == nac) & (df['¿NIVEL EDUCATIVO ALCANZADO?'] == 'Técnico')]
                    technologist = df[(df['NAC'] == nac) & (df['¿NIVEL EDUCATIVO ALCANZADO?'] == 'Tecnólogo')]
                    disability_records = df[(df['NAC'] == nac) & (df['¿PRESENTA ALGUNA DISCAPACIDAD?'] == 'Si')]
                    non_disability_records = df[(df['NAC'] == nac) & (df['¿PRESENTA ALGUNA DISCAPACIDAD?'] == 'No')]
                    afrodescendant_records = df[(df['NAC'] == nac) & (df['¿CON QUE TIPO DE ETNIA SE REPRESENTA?'] == 'Afrodescendiente')]
                    indigenous_records = df[(df['NAC'] == nac) & (df['¿CON QUE TIPO DE ETNIA SE REPRESENTA?'] == 'Indígena')]
                    black_records = df[(df['NAC'] == nac) & (df['¿CON QUE TIPO DE ETNIA SE REPRESENTA?'] == 'Negro')]
                    none_ethnicity_records = df[(df['NAC'] == nac) & (df['¿CON QUE TIPO DE ETNIA SE REPRESENTA?'] == 'Ninguno')]
                    palenquero_records = df[(df['NAC'] == nac) & (df['¿CON QUE TIPO DE ETNIA SE REPRESENTA?'] == 'Palenquero')]
                    raizal_records = df[(df['NAC'] == nac) & (df['¿CON QUE TIPO DE ETNIA SE REPRESENTA?'] == 'Raizal')]
                    rom_records = df[(df['NAC'] == nac) & (df['¿CON QUE TIPO DE ETNIA SE REPRESENTA?'] == 'ROM(Gitana)')]
                    male_records = df[(df['NAC'] == nac) & (df['GÉNERO'] == 'Masculino')]
                    female_records = df[(df['NAC'] == nac) & (df['GÉNERO'] == 'Femenino')]
                    lgtbiq_plus_records = df[(df['NAC'] == nac) & (df['GÉNERO'] == 'LGBTIQ+')]
                    other_gender_records = df[(df['NAC'] == nac) & (df['GÉNERO'] == 'Otro')]
                    conflict_victims_records = df[(df['NAC'] == nac) & (df['¿CONDICIÓN?'] == 'Desplazado/a')]
                    
                    count_early_childhood = len(early_childhood_records)
                    count_childhood = len(childhood_records)
                    count_adolescence = len(adolescence_records)
                    count_youth = len(youth_records)
                    count_adult = len(adult_records)
                    count_elderly = len(elderly_records)
                    count_high_school = len(high_school)
                    count_none_school = len(none_school)
                    count_postgraduate = len(postgraduate)
                    count_preschool = len(preschool)
                    count_undergraduate = len(undergraduate)
                    count_primary_school = len(primary_school)
                    count_technical = len(technical)
                    count_technologist = len(technologist)
                    count_disability = len(disability_records)
                    count_non_disability = len(non_disability_records)
                    count_afrodescendant = len(afrodescendant_records)
                    count_indigenous = len(indigenous_records)
                    count_black = len(black_records)
                    count_none_ethnicity = len(none_ethnicity_records)
                    count_palenquero = len(palenquero_records)
                    count_raizal = len(raizal_records)
                    count_rom = len(rom_records)
                    count_male = len(male_records)
                    count_female = len(female_records)
                    count_lgtbiq_plus = len(lgtbiq_plus_records)
                    count_other_gender = len(other_gender_records)
                    count_conflict_victims = len(conflict_victims_records)

                    impact_instance = Impact2024.objects.create(
                        nac=nac,
                        beneficiaries=count,
                        early_childhood=count_early_childhood,
                        childhood=count_childhood,
                        adolescence=count_adolescence,
                        youth=count_youth,
                        adult=count_adult,
                        high_school = count_high_school,
                        none_school = count_none_school,
                        postgraduate = count_postgraduate,
                        preschool = count_preschool,
                        undergraduate = count_undergraduate,
                        primary_school = count_primary_school,
                        technical = count_technical,
                        technologist = count_technologist,
                        elderly=count_elderly,
                        disability=count_disability,
                        non_disability=count_non_disability,
                        afrodescendant=count_afrodescendant,
                        indigenous=count_indigenous,
                        black=count_black,
                        none_ethnicity=count_none_ethnicity,
                        palenquero=count_palenquero,
                        raizal=count_raizal,
                        rom=count_rom,
                        male=count_male,
                        female=count_female,
                        lgtbiq_plus=count_lgtbiq_plus,
                        other_gender=count_other_gender,
                        conflict_victims=count_conflict_victims
                    )
                    impact_instance.save()
                
            except Exception as e:
                print("Error:", e)

    impact_objects = Impact2024.objects.all()

    return render(request, 'pages/components/2024/impacto.html', {'impact_objects': impact_objects})


from django.http import FileResponse
import os

def pdf_listar(request):
    # Ruta al PDF en tu proyecto Django
    pdf_path = "pages/components/2024/presentacion.pdf"
    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as pdf_file:
            return FileResponse(pdf_file, content_type='application/pdf')
    else:
        # Devuelve una respuesta de error si el archivo no se encuentra
        return HttpResponse("El archivo PDF no se encontró", status=404)
