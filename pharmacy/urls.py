from django.conf.urls import url

from pharmacy.views import GetAllDrugs, AjaxPostDrugCreate, SheetAssignmentView, EditStockTackingView, \
    UseDrugForPatientView, AjaxDrugForPatient, ShowAllDrugReportForDoctor, AjaxDrugReportForPatient, \
    AjaxDrugReportRangeDateForPatient, ShowEatDrugReport, GetAjaxRecordPatient, DetailShowEatDrugReport

urlpatterns = [
    url(r'^admin_pharmacy/$', GetAllDrugs.as_view(), name='admin-pharmacy'),
    url(r'^admin_pharmacy/report/$', ShowAllDrugReportForDoctor.as_view(), name='admin-pharmacy-report'),
    url(r'^edit_admin_pharmacy/$', EditStockTackingView, name='edit-admin-pharmacy'),
    url(r'^drug_create/$', AjaxPostDrugCreate, name="admin-pharmacy-drug-create"),
    url(r'^sheet_assignment/$', SheetAssignmentView, name="sheet-assignment"),
    url(r'^drug_for_patient/$', UseDrugForPatientView, name="drug-for-patient"),
    url(r'^ajax_get_drug_pat/$', AjaxDrugForPatient, name="ajax-get-drug-pat"),
    url(r'^ajax_get_report_drug/$', AjaxDrugReportForPatient, name="ajax-get-report-drug-pat"),
    url(r'^ajax_get_report_drug_range_date/$', AjaxDrugReportRangeDateForPatient,
        name="ajax-get-report-drug-range-date-pat"),
    url(r'^report_assignment_sheet/$', ShowEatDrugReport.as_view(), name="assignment-sheet-report"),
    url(r'^report_assignment_sheet/(?P<pk>\d+)/$', DetailShowEatDrugReport.as_view(),
        name="assignment-sheet-report-detail"),
    url(r'^ajax_get_patient/$', GetAjaxRecordPatient, name="ajax-get-record-patient"),

]
