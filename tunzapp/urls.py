from tunzapp import views
from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('register/', views.signup, name='register'),
    path('logout/',  views.logout_user, name='logout'),
    path('about/', views.about, name='about'),
    path('details/<str:pk>/', views.details, name='details'),
    path('list/', views.list, name='list'),
    path('api/child-list', views.ChildList.as_view()),
    path('api/child-detail/<int:pk>/', views.ChildDetail.as_view()),
]
