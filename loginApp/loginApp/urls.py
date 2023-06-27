from django.contrib import admin
from django.urls import path, include
from mydb.views import login_view, register_view, dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='Login'),
    path('register/', register_view, name='Register'),
    path('dashboard/', dashboard_view, name='dashboard')
]
