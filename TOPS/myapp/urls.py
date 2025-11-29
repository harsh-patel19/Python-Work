from django.urls import path
from myapp.views import *


urlpatterns =[
    path("getuser",get_user,name="getuser"),
    path("postuser",post_user,name="postuser"),
    path("putuser",put_user,name="putuser"),
    path("deleteuser",delete_user,name="deleteuser"),

    path("students/",StudentView.as_view()),
    path("students/<id>",StudentViewId.as_view()),
]