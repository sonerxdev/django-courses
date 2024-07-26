from django.urls import path
from .import views


# abc.com/client/home => anasayfa
# abc.com/client/ => anasayfa
# abc.com/kurslar 0 => 



urlpatterns = [
    path('',views.home),
    path('anasayfa', views.home),
    path('kurslar',views.kurslar),
]
