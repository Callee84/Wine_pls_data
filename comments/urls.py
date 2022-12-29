from django.urls import path
from comments import views

urlpatterns = [
    path('comments/', views.CommentsList.as_view()),
    path('comments/<int:pk>', views.CommentDetails.as_view()),
    path('comments/wines/', views.CommentWineList.as_view()),
    path('comments/wines/<int:pk>', views.CommentWineDetails.as_view()),
]
