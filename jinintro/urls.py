from django.urls import path
from .views import item_list, item_detail

app_name = 'jinintro'

urlpatterns = [
    path('',item_list),
    path('<int:pk>/',item_detail),
]