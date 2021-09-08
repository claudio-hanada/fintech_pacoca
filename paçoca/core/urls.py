from django.urls import path
from core.views import homeView, resultView

urlpatterns = [
    path('home', homeView.as_view(), name='home'),
    path('result', resultView.as_view(), name='result'),
]