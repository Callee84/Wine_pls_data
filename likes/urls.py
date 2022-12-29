from django.urls import path
from likes import views

urlpatterns = [
    path('likes/', views.LikesList.as_view()),
    path('likes/<int:pk>', views.LikesListDetails.as_view()),
    path('likes/wines/', views.LikesWineList.as_view()),
    path('likes/wines/<int:pk>', views.LikesWineListDetails.as_view()),
]
