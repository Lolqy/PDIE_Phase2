from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('contact/', views.contact, name='contact'),  # Add this line
    path('', views.index, name='index'),  # Assuming you have an index view
    path('dashboard/', views.dashboard, name='dashboard'),
    path('update_status/<str:cust_id>/', views.update_status, name='update_status'),
    path('index/', include('django.contrib.auth.urls')),
    path('signup/', views.SignupWorker, name='signup'),
    path('signin/', views.Signin, name='signin'),
    path('booking/', views.booking_view, name='booking'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
    path('logout/', views.logout_view, name='logout'),
    
    
]