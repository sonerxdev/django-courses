from django.urls import path
from .import views


# abc.com/client/home => anasayfa
# abc.com/client/ => anasayfa
# abc.com/kurslar 0 => 



urlpatterns = [
    path('',views.kurslar), 
    path('list',views.kurslar), 
    path('details', views.details),
    path('programlama', views.programlama),
    path('mobil-uygulamalar', views.mobiluygulamalar)


]
