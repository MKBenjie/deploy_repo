import datetime
from django.shortcuts import render,redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import Book, Borrowed, Student
from django.contrib.auth import authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import LogInForm, SignUpForm
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from django.db.models import Q


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
        return Book.objects.filter(
            Q(title__icontains = query) |  Q(author__icontains = query) |
            Q(status__icontains = query)
            )


# def borrow(request):
#     return render(request, 'lib/borrow_book.html')
@login_required
def student_request_issue(request, pk):
    obj = Book.objects.get(id=pk)
    stu=Student.objects.get(user = pk)
    s = get_object_or_404(Student, user = pk)
    # current = Book.objects.get(status)
    if s.total_books_due < 3:
        message = "Book has been isuued, You can collect book from library"
        a = Borrowed()
        a.student = s
        a.book = obj
        a.issue_date = datetime.datetime.now()
        a.return_date = a.issue_date + datetime.timedelta(days=4)
        obj.copies_available = obj.copies_available - 1
        obj.save()
        stu.total_books_due = stu.total_books_due+1
        stu.save()
        a.save()
        if obj.copies_available <= 0:
            st = Book(status = 'Borrowed')
            st.save()
        else:
            st = Book(status = 'Available')
            st.save()


    else:
        message = "You have exceeded your limit."
    return render(request, 'lib/borrow_book.html', locals())
