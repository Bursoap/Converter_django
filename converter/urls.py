from django.urls import path

from converter.views import ConverterView

app_name = 'converter'

urlpatterns = [
    path('', ConverterView.as_view(), name='index'),
]