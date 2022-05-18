from django.urls import path

from kadastr_api.views import KadastrAPIView

app_name = 'kadastr'
urlpatterns = [
    path('<str:prefix>/', KadastrAPIView.as_view(), name='kadastr'),
    # path('', KadastrAPIView.as_view(), name='kadastr'),
]
