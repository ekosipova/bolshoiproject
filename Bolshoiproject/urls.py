from django.contrib import admin
from django.urls import path,include
from bolshoi_cast.views import show_main_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',show_main_page),
    path('bolshoi_cast/',include('bolshoi_cast.urls'))
]
