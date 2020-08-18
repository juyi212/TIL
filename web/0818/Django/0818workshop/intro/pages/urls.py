from django.urls import path
from . import views

app_names='dinner'
urlpatterns=[
    path('dinner/<str:dinner>/<int:people>',views.dinner,name='dinner'),
]