from django.urls import path
from posts.views import NewsView, DetailView

urlpatterns = [
    path('', NewsView.as_view()),
    path('category/<int:pk>/', NewsView.as_view(), name='category'),
    path('detail/<int:pk>/', DetailView.as_view(), name='detail'),
]
