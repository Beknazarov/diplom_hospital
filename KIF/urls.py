from django.conf.urls import url

from KIF.views import InfoTable

urlpatterns = [
    url(r'^info-table/$', InfoTable.as_view(), name="info-table")
]
