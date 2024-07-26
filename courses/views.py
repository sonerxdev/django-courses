from django.http import HttpResponse

# Create your views here.


def kurslar(request):
    return HttpResponse('kurs listesi')


def details(request,kurs_adi):
    return HttpResponse(f'{kurs_adi} detay sayfasi')


def getCoursesByCategory(request, category_name):
    text = ""
    
    if (category_name == "programlama"):
        text = "Programlama kategorisine ait kurslar" 
    elif(category_name == "web-gelistirme"):
        text = "web gelistirme kategorisine ait kurslar"
    else: 
        text = "yanlis kategori secimi"     
    return HttpResponse(text)



def getCoursesByCategoryID(request, category_id):
    return HttpResponse(category_id)