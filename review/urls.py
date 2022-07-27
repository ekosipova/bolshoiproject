from django.urls import path
from .views import ReviewPage,DoneView


urlpatterns = [
    path('',ReviewPage.as_view(),name= 'review'),
    path('done',DoneView.as_view()),
      ]