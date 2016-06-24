# coding=utf-8
from django.conf.urls import url
from .views import report_pdf, report_html
from .test_views import rendering_pdf, create_pdf, show_render_html, render_pdf  # временно потом удалить

urlpatterns = [
    url(r'^history/$', report_pdf),
    url(r'^show_history/$', report_html)
]



#
# urlpatterns += [
#     url(r'^create/$', create_pdf),
#     url(r'^render/$', render_pdf),
#     url(r'^rendering/$',rendering_pdf),
#     url(r'^show/$',show_render_html),
# ]
