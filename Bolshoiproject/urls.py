from django.contrib import admin
from django.urls import path,include
from bolshoi_cast.views import MainPage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',MainPage.as_view(),name= 'main'),
    path('bolshoi_cast/',include('bolshoi_cast.urls')),
    path('review/', include('review.urls')),
]
