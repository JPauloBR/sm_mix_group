from django.shortcuts import render
from .models import Employee, Group, History
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from datetime import datetime 

@login_required
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_employees=Employee.objects.all().count()
    creator_user_id=request.user
    last_runtime_obj=History.objects.filter(creator=request.user).order_by('runtime').first()
    last_runtime=last_runtime_obj.runtime
    num_groups=Group.objects.filter(runtime=last_runtime_obj).count()
    # Available books (status = 'a')
    last_group=Group.objects.filter(expiration_date__isnull=True)
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_employees':num_employees,'num_groups':num_groups, 'last_runtime': last_runtime, 'creator_user_id': creator_user_id},
    )

@login_required
def runprocess(request):

    #logic in creating groups
    new_runtime=History(runtime=datetime.now(), creator=request.user)
    new_runtime.save();
    new_group=Group(employee_list=[1,2,3], creation_date=datetime.now(),runtime=new_runtime)
    new_group.save()

    return render(
        request,
        'runprocess_success.html',
    )

class EmployeeListView(LoginRequiredMixin, generic.ListView):
    model = Employee

class EmployeeDetailView(LoginRequiredMixin, generic.DetailView):
	model = Employee

class GroupListView(LoginRequiredMixin, generic.ListView):
    model = Group

class GroupDetailView(LoginRequiredMixin, generic.DetailView):
	model = Group

class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['name']

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('employees')

