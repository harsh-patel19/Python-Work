from django.urls import path,include
from Myapp.views import CategoryView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("categories",CategoryView.as_view()),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)