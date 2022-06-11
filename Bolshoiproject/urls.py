from django.contrib import admin
from django.urls import path,include
from bolshoi_cast.views import show_main_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',show_main_page,name= 'main'),
    path('bolshoi_cast/',include('bolshoi_cast.urls')),
    path('review/', include('review.urls'))
]
