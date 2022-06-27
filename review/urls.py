from django.urls import path
from .views import FeedBackView,DoneView,FeedBackUpdateView,ListFeedBack

urlpatterns = [
    path('',FeedBackView.as_view()),
    path('done',DoneView.as_view()),
    path('<int:pk>',FeedBackUpdateView.as_view()),
    path('list/',ListFeedBack.as_view())
]