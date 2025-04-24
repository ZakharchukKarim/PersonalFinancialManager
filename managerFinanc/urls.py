"""
URL configuration for managerFinanc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from finance.views import finance_page
from people.views import people_page
from meeting_sessions.views import index_page, meeting_sessions_page
from stats.views import stats_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_page),
    path("people/", people_page),
    path("meeting_sessions/", meeting_sessions_page),
    path("stats/", stats_page),
    path("finance/", finance_page),
]
