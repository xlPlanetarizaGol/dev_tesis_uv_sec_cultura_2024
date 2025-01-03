from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    
    path('', views.index, name='index'),
    
    #Autenticación
    
    path('accounts/register/', views.UserRegistrationView.as_view(), name='register'),
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/auth-password-change-done.html'
    ), name="password_change_done"),

    path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', views.UserPasswrodResetConfirmView.as_view(), name="password_reset_confirm"),

    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/auth-password-reset-done.html'
    ), name='password_reset_done'),

    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/auth-password-reset-complete.html'
    ), name='password_reset_complete'),
    
    #Formularios
    
    path('media-dissemination-2020/', views.listar_media, name='listar_media'),
    path('dialogue-tables-2020/', views.listar_dialogue_tables_2020, name='listar_dialogue_tables_2020'),
    path('beneficiaries-2020/', views.listar_beneficiarios_2020, name='listar_beneficiarios_2020'),
    path('attendants-2020/', views.listar_acudientes_2020, name='listar_acudientes_2020'),
    path('contracts-2020/', views.listar_contratos_2020, name='listar_contratos_2020'),
    path('transfers-2020/', views.listar_transfers_2020, name='listar_transfers_2020'),
    path('care-appointments-2020/', views.listar_citas_2020, name='listar_citas_2020'),
    path('synchronous-meetings-2020/', views.listar_sincronicos_2020, name='listar_sincronicos_2020'),
    path('beneficiaries-2021a/', views.listar_beneficiarios_2021a, name='listar_beneficiarios_2021a'),
    path('binnacles-2021a/', views.listar_bitacoras_2021a, name='listar_bitacoras_2021a'),
    path('dialogue-tables-2021a/', views.listar_dialogue_tables_2021a, name='listar_dialogue_tables_2021a'),
    path('instruments-load-2021a/', views.listar_instruments_2021a, name='listar_instruments_2021a'),
    path('methodological-transfers-2021a/', views.listar_metho_transf_2021a, name='listar_metho_transf_2021a'),
    path('beneficiaries-impact-2021a/', views.listar_beneficiarios_impacto, name='listar_beneficiarios_impacto'),
    path('pedagogical-sheets-2021a/', views.listar_pedagogical_2021a, name='listar_pedagogical_2021a'),
    path('platform-training-2021a/', views.listar_plataform_training_2021a, name='listar_plataform_training_2021a'),
    path('psychosocial-care-2021a/', views.listar_psychosocial_2021a, name='listar_psychosocial_2021a'),
    path('psychosocial-transfers-2021a/', views.listar_psycho_transfer_2021a, name='listar_psycho_transfer_2021a'),
    path('beneficiaries-impact-2021b-2022a/', views.listar_follow_participants_2021b, name='listar_follow_participants_2021b'),
    path('cultural-activation-2021b-2022a/', views.listar_actcultural_2021b, name='listar_actcultural_2021b'),
    path('feedback-cultural-activation-2021b-2022a/', views.listar_feedactcultural_2021b, name='listar_feedactcultural_2021b'),
    path('methodological-instructions-2021b-2022a/', views.listar_metho_instruc_2021b, name='listar_metho_instruc_2021b'),
    path('psychosocial-instructions-2021b-2022a/', views.listar_psycho_instruc_2021b, name='listar_psycho_instruc_2021b'),
    path('territorial-tables-2021b-2022a/', views.listar_territorial_tables_2021b, name='listar_territorial_tables_2021b'),
    path('beneficiaries-capacity-2021b-2022a/', views.listar_ben_capacity_2021b, name='listar_ben_capacity_2021b'),
    path('beneficiaries-2021b-2022a/', views.listar_beneficiaries_2021b, name='listar_beneficiaries_2021b'),
    path('pedagogical-sheets-2021b-2022a/', views.listar_pedagogical_2021b, name='listar_pedagogical_2021b'),
    path('binnacles-2021b-2022a/', views.listar_dev_cultural_act_2021b, name='listar_dev_cultural_act_2021b'),
    path('psychosocial-care-2021b-2022a/', views.listar_psychosocial_2021b, name='listar_psychosocial_2021b'),
    path('circulations-cultural-2021b-2022a/', views.listar_circulations_cultural_2021b, name='listar_circulations_cultural_2021b'),
    path('artistic-show-2021b-2022a/', views.listar_artistic_sample_2021b, name='listar_artistic_sample_2021b'),
    path('validation-users-2022b/', views.listar_validation_users_2022b, name='listar_validation_users_2022b'),
    path('dialogue-tables-2022b/', views.listar_dialogue_tables_2022b, name='listar_dialogue_tables_2022b'),
    path('cultural-activation-2022b/', views.listar_cut_act_2022b, name='listar_cut_act_2022b'),
    path('methodological-instructions-2022b/', views.listar_metho_instruct_2022b, name='listar_metho_instruct_2022b'),
    path('psychosocial-instructions-2022b/', views.listar_psycho_instruc_2022b, name='listar_psycho_instruc_2022b'),
    path('pedagogical-sheets-2022b/', views.listar_pedagogical_2022b, name='listar_pedagogical_2022b'),
    path('binnacles-2022b/', views.listar_binnacles_2022b, name='listar_binnacles_2022b'),
    path('psychosocial-care-2022b/', views.listar_care_2022b, name='listar_care_2022b'),
    path('cultural-seedbed-2022b/', views.listar_seedbed_2022b, name='listar_seedbed_2022b'),
    path('cultural-ensemble-2022b/', views.listar_ensemble_2022b, name='listar_ensemble_2022b'),
    path('methodological-carpet-2022b/', views.listar_tap_metho_2022b, name='listar_tap_metho_2022b'),
    path('parents-school-2022b/', views.listar_parents_2022b, name='listar_parents_2022b'),
    path('strategys-circulation-2022b/', views.listar_strategys_2022b, name='listar_strategys_2022b'),
    path('beneficiaries-2022b/', views.listar_beneficiaries_2022b, name='listar_beneficiaries_2022b'),
    path('beneficiaries-capacity-2022b/', views.listar_beneficiaries_capacity_2022b, name='listar_beneficiaries_capacity_2022b'),

    #2020

    path('dash-sociodemographic-2020/', login_required(views.cs_2020), name='cs_2020'),
    path('dash-join-annexes-2020/', login_required(views.an_2020), name='an_2020'),
    path('dash-summary-contracts-2020/', login_required(views.ct_2020), name='ct_2020'),
    path('ranking-2020/', login_required(views.rank_2020), name='rank_2020'),

    #2021a

    path('dash-sociodemographic-2021a/', login_required(views.cs_2021a), name='cs_2021a'),
    path('dash-cultural-activities-2021a/', login_required(views.ca_2021a), name='ca_2021a'),
    path('dash-cultural-dialogues-2021a/', login_required(views.dc_2021a), name='dc_2021a'),
    path('dash-transfers-2021a/', login_required(views.tr_2021a), name='tr_2021a'),
    path('dash-pedagogicals-2021a/', login_required(views.fpd_2021a), name='fpd_2021a'),
    path('dash-care-appointments-2021a/', login_required(views.cap_2021a), name='cap_2021a'),
    path('dash-instruments-2021a/', login_required(views.icp_2021a), name='icp_2021a'),
    path('ranking-2021a/', login_required(views.rank_2021a), name='rank_2021a'),
    
    #2021b-2022a

    path('dash-sociodemographic-2021b-2022a/', login_required(views.cs_2021b_2022a), name='cs_2021b_2022a'),
    path('dash-binnacles-2021b-2022a/', login_required(views.bjp_2021b_2022a), name='bjp_2021b_2022a'),
    path('dash-cultural-activations-2021b-2022a/', login_required(views.ac_2021b_2022a), name='ac_2021b_2022a'),
    path('dash-feedback-2021b-2022a/', login_required(views.fed_2021b_2022a), name='fed_2021b_2022a'),
    path('dash-methodological-instructions-2021b-2022a/', login_required(views.im_2021b_2022a), name='im_2021b_2022a'),
    path('dash-pedagogicals-2021b-2022a/', login_required(views.fp_2021b_2022a), name='fp_2021b_2022a'),
    path('dash-care-appointments-2021b-2022a/', login_required(views.cap_2021b_2022a), name='cap_2021b_2022a'),
    path('dash-psychosocial-instructions-2021b-2022a/', login_required(views.ip_2021b_2022a), name='ip_2021b_2022a'),
    path('dash-territorial-tables-2021b-2022a/', login_required(views.mt_2021b_2022a), name='mt_2021b_2022a'),
    path('ranking-2021b-2022a/', login_required(views.rank_2021b_2022a), name='rank_2021b_2022a'),

    #2022b
    
    path('dash-sociodemographic-2022b/', login_required(views.cs_2022b), name='cs_2022b'),
    path('dash-binnacles-2022b/', login_required(views.bjp_2022b), name='bjp_2022b'),
    path('dash-pedagogicals-2022b/', login_required(views.fp_2022b), name='fp_2022b'),
    path('dash-activations-2022b/', login_required(views.ac_2022b), name='ac_2022b'),
    path('dash-ensembles-2022b/', login_required(views.ec_2022b), name='ec_2022b'),
    path('dash-seedbeds-2022b/', login_required(views.sc_2022b), name='sc_2022b'),
    path('dash-dialogues-2022b/', login_required(views.md_2022b), name='md_2022b'),
    path('dash-carpet-2022b/', login_required(views.tpm_2022b), name='tpm_2022b'),
    path('dash-parents-2022b/', login_required(views.ep_2022b), name='ep_2022b'),
    path('dash-care-appointments-2022b/', login_required(views.cap_2022b), name='cap_2022b'),
    path('dash-estragies-2022b/', login_required(views.sv_2022b), name='sv_2022b'),
    path('ranking-2022b/', login_required(views.rank_2022b), name='rank_2022b'),
    
    #2023a
    
    path('means-verification-2023a/', login_required(views.listar_means_verification), name='listar_means_verification'),
    path('verification-follow-2023a/', login_required(views.listar_verification_follow), name='listar_verification_follow'),
    path('dialogue-tables-2023a/', login_required(views.listar_dialogue_tables), name='listar_dialogue_tables'),
    path('activations-2023a/', login_required(views.listar_activations), name='listar_activations'),
    path('circulations-2023a/', login_required(views.listar_circulation), name='listar_circulation'),
    path('show-cultural-2023a/', login_required(views.listar_show_cultural), name='listar_show_cultural'),
    path('assembly-2023a/', login_required(views.listar_ensamble), name='listar_ensamble'),
    path('transfer-methodological-2023a/', login_required(views.listar_transfer_methodological), name='listar_transfer_methodological'),
    path('transfer-psychosocial-2023a/', login_required(views.listar_transfer_psychosocial), name='listar_transfer_psychosocial'),
    path('pedagogical-planning-monitors-2023a/', login_required(views.listar_planning_monitors), name='listar_planning_monitors'),
    path('pedagogical-planning-instructors-2023a/', login_required(views.listar_planning_instructors), name='listar_planning_instructors'),
    path('binnacles-2023a/', login_required(views.listar_binnacles), name='listar_binnacles'),
    path('seedbeds-2023a/', login_required(views.listar_cultural_seedbed), name='listar_cultural_seedbed'),
    path('jornality-support-asym-2023a/', login_required(views.listar_jornality_asym), name='listar_jornality_asym'),
    path('jornality-support-metho-2023a/', login_required(views.listar_jornality_metho), name='listar_jornality_metho'),
    path('jornality-support-super-2023a/', login_required(views.listar_jornality_super), name='listar_jornality_super'),
    path('support-psycho-2023a/', login_required(views.listar_jornality_psychosocial), name='listar_jornality_psychosocial'),
    path('strategys-circulation-2023a/', login_required(views.listar_strategys_circulation), name='listar_strategys_circulation'),
    
    #2023 Dashboards
    
    path('dash-sociodemographic-2023a/', login_required(views.pb_2023a), name='pb_2023a'),
    path('dash-activations-2023a/', login_required(views.ac_2023a), name='ac_2023a'),
    path('dash-assembly-2023a/', login_required(views.eb_2023a), name='eb_2023a'),
    path('dash-circulations-2023a/', login_required(views.cc_2023a), name='cc_2023a'),
    path('dash-seedbeds-2023a/', login_required(views.sd_2023a), name='sd_2023a'),
    path('dash-jornalitys/', login_required(views.js_2023a), name='js_2023a'),
    path('dash-pedagogicals-2023a/', login_required(views.pd_2023a), name='pd_2023a'),
    path('dash-show-cultural-2023a/', login_required(views.sc_2023a), name='sc_2023a'),
    path('dash-transfers-2023a/', login_required(views.tr_2023a), name='tr_2023a'),
    path('dash-psicopedagogicals-2023a/', login_required(views.btp_2023a), name='btp_2023a'),
    path('ranking-2023a/', login_required(views.rank_2023a), name='rank_2023a'),

    #2024
  
    path('indicadores-2024/', login_required(views.indicadores_2024), name='indicadores_2024'),
    path('payment-monitors-2024/', login_required(views.calcular_registros_por_semana), name='calcular_registros_por_semana'),
    path('eliminar_registros_por_fecha/', views.eliminar_registros_por_fecha, name='eliminar_registros_por_fecha'),
    path('eliminar_corte_pago/', views.eliminar_corte_pago, name='eliminar_corte_pago'),
    path('impact_2024/', login_required(views.impact_2024), name='impact_2024'),
    path('obtener-fechas-unicas/', login_required(views.obtener_fechas_unicas), name='obtener_fechas_unicas'),
    path('obtener-fechas-unicas_indicators/', login_required(views.obtener_fechas_unicas_indicators), name='obtener_fechas_unicas_indicators'),
    path('cultural-marginalization/', login_required(views.mc_2024), name='mc_2024'),
    
    #Generación de PDF
  
    path('create-pdf/', login_required(views.pdf_view), name='pdf_view'),
    path('view-pdf/', login_required(views.ver_pdf), name='ver_pdf'),
    path('update-pdf/<int:pdf_id>/', login_required(views.editar_pdf), name='editar_pdf'),
    path('eliminar-pdf/<int:pdf_id>/', login_required(views.eliminar_pdf), name='eliminar_pdf'),
    path('descargar-pdf/<int:pdf_id>/', login_required(views.descargar_pdf), name='descargar_pdf'),
    
    path('pdf', views.pdf_listar, name='pdf_listar'),


]
