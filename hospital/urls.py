from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from Analyze.admin import admin_analyze
from Analyze.views import GenerateAnalyze
from KIF.views import AjaxForGetRegion, AjaxForGetTown, TemplateDoctorView
from news.views import AllNewsView, PageNotFound

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^admin_analyze/', include(admin_analyze.urls)),
    url(r'^nested_admin/', include('nested_admin.urls')),
    url(r'^get_region/$', AjaxForGetRegion.as_view(), name="get_region"),
    url(r'^get_town/$', AjaxForGetTown.as_view(), name="get_town"),
    url(r'^$', AllNewsView.as_view(), name='home'),
    url(r'^kif/', include('KIF.urls'), name='kif'),
    url(r'^profile/', include('profileUser.urls'), name='profile'),
    url(r'^pharmacy/', include('pharmacy.urls'), name='pharmacy'),
    url(r'^news/', include('news.urls'), name='news'),
    url(r'^analyze/$', GenerateAnalyze.as_view(), name='analyze'),
    url(r'^doctor/', include('doctor.urls'), name='doctor'),
    url(r'^report/', include('reports.urls'), name='report-kif'),
    url(r'^newadmin/$', TemplateDoctorView.as_view(), name='report-kif'),
    url(r'^datadir/',include('datadir.urls'), name='datadir'),
]

handler404 = PageNotFound.as_view()
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
