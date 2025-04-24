from django.shortcuts import render

def index_page(request):
    return render(request, 'index.html')

def people_page(request):
    return render(request, 'people.html')
