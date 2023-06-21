
from django.contrib import admin
from app_agenda import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('app_agenda/', include('app_agenda.urls')),
]
