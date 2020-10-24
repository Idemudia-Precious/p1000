from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form1/', views.form1, name="form1"),
    path('form2/', views.form2, name="form2"),
    path('form3/', views.form3, name="form3"),
    path('form4/', views.form4, name="form4"),
    path('form5/', views.form5, name="form5"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]