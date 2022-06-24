
from django.shortcuts import render
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import *
import requests
from rest_framework import generics
from .serializers import ChildSerializer

# Create your views here.
#View function for home: To be done by Julia
def home(request):
    '''view for home'''
    # queryset = requests.get('http://127.0.0.1:8000/api/child/').json()
    queryset = Child.objects.all().order_by('-first_name')
    return render(request, 'tunzapp/home.html', {'queryset': queryset})

class ChildList(generics.ListCreateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

class ChildDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer


#view function for registration: Done by Andre/Oliver
def signup(request):
    '''view for signup'''
    form = CreateUserForm()
    
        
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')
            
    context ={
        'form': form,
        }        
    
    return render(request,'accounts/register.html', context)


#view function for login_page:Done by Andre/Oliver
def login_page(request):
    '''view for login'''
    
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        print(username,password,user)
        if user is not None:
            login(request,user)
            return redirect ('home')
        else:
            messages.info(request, 'Check username or password !')
        
    return render(request, 'accounts/login.html')   


#view function for about section:To be done by Oliver
def about(request):
    return render(request, 'tunzapp/about.html')

#view function for specific details for the child:Ludwig
def details(request, pk):
    child = Child.objects.get(id=pk)
    child_data = Child.objects.filter(id=pk)
    if request.method == 'POST':
        the_child = child
        amount = request.POST.get('amount')
        donated_by = request.user
        
        donation = Donor.objects.create(child=the_child, amount=amount, donated_by = donated_by)
    
    transactions = Donor.objects.filter(id=pk)
    
    # financial = FinancialNeed.objects.filter()
    context= {
        'child':child,
        'child_data':child_data,
        'transactions': transactions
        
        }
    print(child)
    return render(request, 'tunzapp/details.html',context)

#view function for the list of children :To be done by Nimrod
def list(request):
    queryset = Child.objects.all().order_by('-first_name')
    return render(request, 'tunzapp/list.html', {'queryset': queryset})
     

#view function for logout_user:Done by Andre/Oliver
def logout_user(request):
    '''logout user'''
    logout(request)
    return redirect('login')