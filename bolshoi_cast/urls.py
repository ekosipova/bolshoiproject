from django.urls import path
from . import views

urlpatterns = [
    path('main/',views.show_all_cast,name='cast'),
    path('<str:subdivision>',views.get_info_about_subdivision,name= 'subdivision'),
    path('<str:subdivision>/<str:position>', views.show_information_about_position,name = 'position'),
]
