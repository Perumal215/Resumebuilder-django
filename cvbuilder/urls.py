# cvbuilder/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # path('logout/', views.custom_logout, name='logout'),
    # path('login/', views.login_view, name='login'),
    # path('register/', views.register_view, name='register'),
    path('templates/', views.template_list, name='template_list'),
    path('create_resume/', views.create_resume, name='create_resume'),
     path('preview/<int:resume_id>/<int:template_id>/', views.preview_resume, name='preview_resume'),
    path('edit/<int:resume_id>/<int:template_id>/', views.edit_resume, name='edit_resume'),
    path('preview/<int:resume_id>/<int:template_id>/download/', views.download_resume_pdf, name='download_resume_pdf'),
    path('download-word/<int:resume_id>/<int:template_id>/', views.download_word_resume, name='download_word_resume'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)