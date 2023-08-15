# urls.py
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import FileUploadView, TextFileViewSet, RegisterAPI,LoginAPI,TextFileSearchView,TextFileListView, download_text_file
from knox import views as knox_views
from . import views

router = DefaultRouter()
router.register(r'textfiles', TextFileViewSet)

urlpatterns = [
    path('api/upload/',FileUploadView.as_view(), name='file-upload'),
    path('documents/', TextFileListView.as_view(), name='textfile-list'),
    path('search/', TextFileSearchView.as_view(), name='textfile-search'),
    path('api/textfiles/<int:file_id>/download/', views.download_text_file, name='download-text-file'),
    path('', include(router.urls)),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
