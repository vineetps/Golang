import importlib
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ShareDetails
from .forms import Form_Stock_Details, UserForm
# Create your views here.


@login_required
def portfolio(request):
    web_page = ShareDetails.objects.order_by('company_name')
    topic_dict = {'topic': web_page}
    return render(request, 'first_app/portfolio.html', context=topic_dict)

@login_required
def form_stock_market(request):
    form = Form_Stock_Details()
    if request.method == 'POST':
        form = Form_Stock_Details(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/portfolio/')
        else:
            form = Form_Stock_Details()
    return render(request, 'first_app/form_stock_market.html', {'form': form})

@login_required
def home(request):
    return render(request, 'first_app/home.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse('Inactive User!')

        else:
            print('INFO :: Invalid login attempt!')
            print('Username: {} and Password: {}'.format(username, password))
            return HttpResponse('Invalid login attempt!')

    else:
        return render(request, 'first_app/login.html')
