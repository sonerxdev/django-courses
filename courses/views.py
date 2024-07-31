from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
# Create your views here.


data = {
    "programlama" : "programlama kategorisine ait kurslar",
    "web-gelistirme" : "web-gelistirme kategorisine ait kurslar",
    "mobil" : "mobil kategorisine ait kurslar",
}

def kurslar(request):
    list_items = ''
    categpry_list = list(data.keys())
    
    for category in categpry_list:
        redirect_url = reverse('courses_by_category', args=[category])
        list_items += f'<li><a href="{redirect_url}">{category}</a></li>'
        
    html = f'<h1>kurs listesi</h1><br><ul>{list_items}</ul>'
    
    return HttpResponse(html)


def index(request):
    return render(request, 'index.html')

def details(request,kurs_adi):
    return HttpResponse(f'{kurs_adi} detay sayfasi')


def getCoursesByCategory(request, category_name):
    
    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
    except: HttpResponseNotFound("<h1>yanlış kategori secimi</h1>")
     
    
     

def getCoursesByCategoryID(request, category_id):
    # 1-2-3 => 
    category_list = list(data.keys())
    category_name = category_list[category_id -1]
    
    redirect_url = reverse('courses_by_category', args=[category_name])
    
    return redirect(redirect_url)