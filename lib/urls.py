from django.urls import path
from . import views


app_name = 'lib'
urlpatterns =[
    path('', views.HomeView.as_view(), name = 'home'),
    path('signup/', views.SignUpView.as_view(), name = 'signup'),
    path('', views.LogInView.as_view(), name ='login'),
    path('<int:pk>/', views.DetailView.as_view(), name= 'detail'),
    path('search_book/', views.BookSearchView.as_view(), name= 'search_book'),
    # path('borrow/', views.borrow, name='borrow_book'),
    path('<int:pk>/request_issue/', views.student_request_issue, name='request_issue'),

]