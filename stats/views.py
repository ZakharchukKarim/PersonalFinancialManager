from django.shortcuts import render

def index_page(request):
    return render(request, 'index.html')

def stats_page(request):
    return render(request, 'stats.html')