from django.shortcuts import render
from myapp.models import Student
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView

# Create your views here.

class StudentCreateView(CreateView):
    model = Student
    fields = ['name','email','roll']
    template_name = 'myapp/student_form.html'
    success_url = '/student/'

class StudentListView(ListView):
    model = Student
    template_name = 'myapp/student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'myapp/student_detail.html'
    context_object_name = 'student'

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name','email','roll']
    success_url = '/student/'
    template_name = 'myapp/student_form.html'

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'myapp/student_confirm_delete.html'
    success_url = '/student/'
