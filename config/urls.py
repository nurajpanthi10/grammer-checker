from django.contrib import admin
from django.urls import path, include
from users import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('', views.login_view, name='login'),
    path('registration/', views.registration_view, name='registration'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]