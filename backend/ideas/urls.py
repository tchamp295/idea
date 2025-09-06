from django.urls import path
from . import views

urlpatterns = [
    path('submit-idea/', views.submit_idea, name='submit-idea'),
    path('admin-login/', views.admin_login, name='admin-login'),
    path('ideas/', views.get_ideas, name='get-ideas'),
]