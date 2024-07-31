from django.urls import path
from .import views


# abc.com/client/home => anasayfa
# abc.com/client/ => anasayfa
# abc.com/kurslar 0 => 

 # 

urlpatterns = [
    path('',views.index), 
    path('list',views.kurslar), 
    path('<kurs_adi>', views.details),
    path('kategori/<int:category_id>', views.getCoursesByCategoryID),
    path('kategori/<str:category_name>/<>', views.getCoursesByCategory, name = 'courses_by_category'),

]
