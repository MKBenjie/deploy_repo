from django.shortcuts import render,redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import Book
from django.contrib.auth import authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import LogInForm, SignUpForm
from django.contrib.auth.views import LoginView


# Create your views here.

# Sign Up Form
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class LogInView(LoginView):
    form_class = LogInForm
    # success_url = reverse_lazy('bookstore/index.html')
    template_name = 'registration/login.html'



# def home(reque
#     title_list = Book.objects.all() [:5]
#     return render (request, 'bookstore/home.html', {'title_list': title_list })

class HomeView(LoginRequiredMixin, generic.ListView):
    template_name = 'lib/home.html'
    # context_object_name = 'title_list'

    def get_queryset(self):
        return Book.objects.all()[:5]

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Book
    template_name = 'lib/detail.html'

class BookSearchView(generic.ListView):

    # model = Book
    template_name = 'lib/search.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(title__icontains = query)

