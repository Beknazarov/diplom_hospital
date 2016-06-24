from django.conf.urls import url

from profileUser.views import LoginPatient, ChangePassword, ProfileInfo, thank_view, UpdatePatientInfo, LogoutPatient, \
    AppointmentListReport

urlpatterns = [
    url(r'^login/$', LoginPatient.as_view(), name='login'),
    url(r'^logout/$', LogoutPatient.as_view(), name='logout'),
    url(r'^repassword/$', ChangePassword.as_view(), name='repassword'),
    url(r'^info/$', ProfileInfo.as_view(), name='profileInfo'),
    url(r'^update_info/$', UpdatePatientInfo.as_view(), name='updateInfo'),
    url(r'^appoint_list_report/$', AppointmentListReport.as_view(), name='app-list-report'),
    url(r'^thenkey/$', thank_view, name='thanks'),
]
