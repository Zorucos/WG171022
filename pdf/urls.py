from django.conf.urls import url

from . import views
from pdf.views import (GeneratePDF)

urlpatterns = [
    url(r'^pdf/(?P<pk>[0-9]+)/$', GeneratePDF.as_view(), name='pdf_rechnung')
]