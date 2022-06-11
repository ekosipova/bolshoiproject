from django.urls import path
from .views import form_review,done

urlpatterns = [
    path('',form_review),
    path('done',done)
]