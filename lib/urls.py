from turtle import home
from django.urls import path
from . import views


app_name = 'lib'
urlpatterns =[
    path('', views.HomeView.as_view(), name = 'home'),
    path('signup/', views.SignUpView.as_view(), name = 'signup'),
    path('', views.LogInView.as_view(), name ='login'),
    path('<int:pk>/', views.DetailView.as_view(), name= 'detail'),
    path('search_book/', views.BookSearchView.as_view(), name= 'search_book'),

]