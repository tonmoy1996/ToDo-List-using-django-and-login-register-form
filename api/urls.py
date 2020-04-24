from django.urls import path

from api.views import TaskApiView
urlpatterns = [
    
    path('',TaskApiView.as_view())
    
]