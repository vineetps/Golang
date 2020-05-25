from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ShareDetails
from .forms import Form_Stock_Details
# Create your views here.


def index(request):
    web_page = ShareDetails.objects.order_by('company_name')
    topic_dict = {'topic': web_page}
    return render(request, 'first_app/index.html', context=topic_dict)

def form_stock_market(request):
    form = Form_Stock_Details()
    if request.method == 'POST':
        form = Form_Stock_Details(request.POST)
        
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            date_bought = form.cleaned_data['date_bought']
            share_price = form.cleaned_data['share_price']
            shares_bought = form.cleaned_data['shares_bought']

            model = ShareDetails(company_name=company_name, date_bought=date_bought, share_price=share_price, shares_bought=shares_bought)
            model.save()
            return HttpResponseRedirect('/')
        else:
            form = Form_Stock_Details()
    return render(request, 'first_app/form_stock_market.html', {'form': form})

def portfolio(request):
    return render(request, 'first_app/portfolio.html')