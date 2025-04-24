from django.shortcuts import render

def index_page(request):
    return render(request, 'index.html')

def finance_page(request):
    return render(request, 'finance.html')