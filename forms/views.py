from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "forms/index.html")
    else:
        fullname = request.POST["fullname"]
        email = request.POST["email"]
        number = "nill"
        message = request.POST["message"]

        contact = Contact(fullname=fullname, email=email, number=number, message=message)
        contact.save()
        return HttpResponseRedirect(reverse("index"))

def about(request):
    return render(request, "forms/about.html")

def contact(request):
    if request.method == "GET":
        return render(request, "forms/contact.html")
    else:
        fullname = request.POST["fullname"]
        email = request.POST["email"]
        number = request.POST["number"]
        message = request.POST["message"]

        contact = Contact(fullname=fullname, email=email, number=number, message=message)
        contact.save()
        return render(request, "forms/contact.html", {
            "message": "true"
        })

def form1(request):#digital marketer's form
    if request.method == "GET":
        return render(request, "forms/form1.html")
    else:
        fullname = request.POST["fullname"]
        username = request.POST["username"]
        email = request.POST["email"]
        number = request.POST["number"]
        country = request.POST["country"]
        state = request.POST["state"]
        city = request.POST["city"]
        address = request.POST["address"]
        occupation = request.POST["occupation"]
        whatsapp = request.POST["whatsapp"]
        facebook = request.POST["facebook"]
        instagram = request.POST["instagram"]
        twitter = request.POST["twitter"]
        linkedin = request.POST["linkedin"]

        digital = Digital(fullname=fullname, username=username, email=email, number=number, country=country, state=state, city=city,
        address=address, occupation=occupation, whatsapp=whatsapp, facebook=facebook, instagram=instagram, twitter=twitter, linkedin=linkedin)
        digital.save()
        return render(request, "forms/form1.html", {
            "message": "true"
        })

def form2(request):#small and medium enterprises
    if request.method == "GET":
        return render(request, "forms/form2.html")
    else:
        fullname = request.POST["fullname"]
        brandname = request.POST["brandname"]
        email = request.POST["email"]
        number = request.POST["number"]
        country = request.POST["country"]
        state = request.POST["state"]
        city = request.POST["city"]
        category = request.POST["category"]
        address = request.POST["address"]
        occupation = request.POST["occupation"]
        whatsapp = request.POST["whatsapp"]
        facebook = request.POST["facebook"]
        instagram = request.POST["instagram"]
        twitter = request.POST["twitter"]
        linkedin = request.POST["linkedin"]

        sme = SME(fullname=fullname, brandname=brandname, email=email, number=number, country=country, state=state, city=city, category=category,
        address=address, occupation=occupation, whatsapp=whatsapp, facebook=facebook, instagram=instagram, twitter=twitter, linkedin=linkedin)
        sme.save()
        return render(request, "forms/form2.html", {
            "message": "true"
        })

def form3(request):#COUPON RETAILERS
    if request.method == "GET":
        return render(request, "forms/form3.html")
    else:
        fullname = request.POST["fullname"]
        username = request.POST["username"]
        email = request.POST["email"]
        number = request.POST["number"]
        country = request.POST["country"]
        state = request.POST["state"]
        city = request.POST["city"]
        address = request.POST["address"]
        occupation = request.POST["occupation"]
        idno = request.POST["idno"]
        utility = request.POST["utility"]
        bvn= request.POST["bvn"]
        whatsapp = request.POST["whatsapp"]
        facebook = request.POST["facebook"]
        instagram = request.POST["instagram"]
        twitter = request.POST["twitter"]
        linkedin = request.POST["linkedin"]

        coupon = Coupon(fullname=fullname, username=username, email=email, number=number,
        country=country, state=state, city=city, address=address, occupation=occupation,
        idno=idno, utility=utility, bvn=bvn,
        whatsapp=whatsapp, facebook=facebook, instagram=instagram, twitter=twitter, linkedin=linkedin)
        coupon.save()
        return render(request, "forms/form3.html", {
            "message": "true"
        })

def form4(request):#BUSINESS/VOCATIONAL COACHES 
    if request.method == "GET":
        return render(request, "forms/form4.html")
    else:
        fullname = request.POST["fullname"]
        username = request.POST["username"]
        email = request.POST["email"]
        number = request.POST["number"]
        country = request.POST["country"]
        state = request.POST["state"]
        city = request.POST["city"]
        address = request.POST["address"]
        field = request.POST["field"]
        whatsapp = request.POST["whatsapp"]
        facebook = request.POST["facebook"]
        instagram = request.POST["instagram"]
        twitter = request.POST["twitter"]
        linkedin = request.POST["linkedin"]

        vocation = Vocation(fullname=fullname, username=username, email=email, number=number, country=country, state=state, city=city,
        address=address, field=field, whatsapp=whatsapp, facebook=facebook, instagram=instagram, twitter=twitter, linkedin=linkedin)
        vocation.save()
        return render(request, "forms/form4.html", {
            "message": "true"
        })

def form5(request):#Influencers
    if request.method == "GET":
        return render(request, "forms/form5.html")
    else:
        fullname = request.POST["fullname"]
        username = request.POST["username"]
        email = request.POST["email"]
        number = request.POST["number"]
        country = request.POST["country"]
        state = request.POST["state"]
        city = request.POST["city"]
        address = request.POST["address"]
        occupation = request.POST["occupation"]
        whatsapp = request.POST["whatsapp"]
        facebook = request.POST["facebook"]
        instagram = request.POST["instagram"]
        twitter = request.POST["twitter"]
        linkedin = request.POST["linkedin"]

        influencer = Influencer(fullname=fullname, username=username, email=email, number=number, country=country, state=state, city=city,
        address=address, occupation=occupation, whatsapp=whatsapp, facebook=facebook, instagram=instagram, twitter=twitter, linkedin=linkedin)
        influencer.save()
        return render(request, "forms/form5.html", {
            "message": "true"
        })