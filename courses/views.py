from django.http import HttpResponse

# Create your views here.


def kurslar(request):
    return HttpResponse('kurs listesi')


def details(request):
    return HttpResponse('kurs detay sayfası')


def getCoursesByCategory(request, category):
    text = ""
    
    if (category == "programlama"):
        text = "Programlama kategorisine ait kurslar" 
    elif(category == "web-gelistirme"):
        text = "web gelistirme kategorisine ait kurslar"
    else: 
        text = "yanlis kategori secimi"
        
    return HttpResponse(text)