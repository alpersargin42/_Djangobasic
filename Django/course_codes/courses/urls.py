from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('search',views.search,name="search"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('<slug:slug>',views.detaylar,name="course_details"),
    path('kategori/<slug:slug>',views.getCoursesByCategory,name='courses_by_category'),
    
]
