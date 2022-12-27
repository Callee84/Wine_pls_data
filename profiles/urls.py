from django.urls import path
from profiles import views

urlpatterns = [
    path('profiles/', views.WinePalsList.as_view()),
    path('profiles/<int:pk>/', views.WinePalDetails.as_view()),
]
