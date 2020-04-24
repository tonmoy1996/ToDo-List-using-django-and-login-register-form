from django.urls import path, include
from . import views 
urlpatterns=[

path('', views.index, name="index"),
path('delete/<str:pk>/',views.deletetask, name="delete"),
path('update/<str:pk1>/',views.update, name="update"),
path('create/',views.CreateUser,name='register'),
path('login/', views.LoginForm,name="login"),
path('profile/', views.Profile,name="profile"),
path('logout/', views.UserLogout,name="logout"),
]
