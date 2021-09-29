from core.views import  IndexView
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    #path('teste', Error404View.as_view(), name="error404"),
    #path('', IndexView.as_view(), name="index"),
]
