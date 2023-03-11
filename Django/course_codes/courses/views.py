from datetime import date
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from .models import Course,Category
from django.core.paginator import Paginator


def index(request):
    kurslar = Course.objects.filter(isActive=1)
    kategoriler = Category.objects.all()
    
    return render(request, 'courses/index.html',{
        'categories': kategoriler,
        'courses':kurslar,
    })

def search(request):
    if "q" in request.GET and request.GET["q"] !="":
        q=request.GET["q"]
        kurslar = Course.objects.filter(isActive=True,title__contains=q).order_by("date")
        kategoriler = Category.objects.all()
    else:
        return redirect("/kurslar")

    paginator=Paginator(kurslar,4)
    page=request.GET.get('page',1)
    page_obj = paginator.page(page)
    # kac_urun=pagi.count
    return render(request,'courses/list.html',{
        'categories': kategoriler,
        'page_obj':page_obj,
    })

def detaylar(request,slug):
    try:
        course=Course.objects.get(slug=slug)
    except:
        raise Http404()
    context={
        'course':course
    }
    return render(request,"courses/detaylar.html",context)

def getCoursesByCategory(request,slug):
    kurslar = Course.objects.filter(category__slug=slug,isActive=True)
    kategoriler = Category.objects.all()

    paginator=Paginator(kurslar,4)
    page=request.GET.get('page',1)
    page_obj = paginator.page(page)
    # kac_urun=pagi.count
    return render(request,'courses/index_2.html',{
        'categories': kategoriler,
        #'courses':kurslar,
        'page_obj':page_obj,
        'seciliKategori':slug,
        # 'kac_urun':kac_urun,
    })




    