from django.conf.urls import url

from doctor.views import LoginView, LogoutView, GetDoctorInfo, AjaxGetDoctorStatus, DoctorAttendingPatient, \
    DoctorMedCartPrint

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login-doctor'),
    url(r'^logout/$', LogoutView.as_view(), name='logout-doctor'),
    url(r'^getStatus/$', AjaxGetDoctorStatus, name='get-status-doctor'),
    url(r'^doctor_info/$', GetDoctorInfo, name='doctor-info'),
    url(r'^med_karta/$', DoctorAttendingPatient.as_view(), name='med-karta-for-doctor'),
    url(r'print_med_karta/(?P<pk>\d+)/$', DoctorMedCartPrint.as_view(), name='print-med-karta'),
]
