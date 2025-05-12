from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('create_employee/', views.create_employee, name='create_employee'),
    path('displaypage/', views.data_page, name='displaypage'),
    path('delete/<uuid:emp_ID>/', views.delete_data, name='delete'),
    path('update/<uuid:emp_ID>/', views.update_form, name='update'),
    # path('update_details/<uuid:emp_ID>', views.update_data, name="update_details")
    
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
]

# Add media URL patterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)