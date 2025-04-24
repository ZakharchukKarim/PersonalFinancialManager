from django.shortcuts import render

def index_page(request):
    return render(request, 'index.html')

def meeting_sessions_page(request):
    return render(request, 'meeting_sessions.html')
