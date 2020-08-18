from django.urls import path
from . import views

app_name="pages"
# 2차관문
urlpatterns=[
    path('lotto/',views.lotto),
    path('dtl/',views.dtl),
    path('index/',views.index),
]