from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bolshoi_cast/',include('bolshoi_cast.urls'))
]
