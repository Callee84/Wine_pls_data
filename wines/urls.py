from django.urls import path
from wines import views

urlpatterns = [
    path('wines/', views.WineList.as_view()),
    path('wines/<int:pk>/', views.WineDetail.as_view()),
]
