from django.urls import path
from Myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path("categories/",CategoryView.as_view()),
    path("categories/<int:id>/", CategoryDetailView.as_view()),
]


urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

