from django.contrib import admin
from .models import *

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display =("fullname", "email","number", "message")

class DigitalAdmin(admin.ModelAdmin):
    list_display =("fullname", "username", "email", "number", "country", "state", "city", "address", "occupation", "whatsapp", "instagram", "twitter", "linkedin")

class SMEAdmin(admin.ModelAdmin):
    list_display =("fullname", "brandname", "email", "number", "country", "state", "city","category", "address", "occupation", "whatsapp", "instagram", "twitter", "linkedin")

class CouponAdmin(admin.ModelAdmin):
    list_display =("fullname", "username", "email", "number", "country", "state", "city", "address", "occupation", "idno", "utility", "bvn", "whatsapp", "instagram", "twitter", "linkedin")

class VocationAdmin(admin.ModelAdmin):
    list_display =("fullname", "username", "email", "number", "country", "state", "city", "address", "field", "whatsapp", "instagram", "twitter", "linkedin")

class InfluencerAdmin(admin.ModelAdmin):
    list_display =("fullname", "username", "email", "number", "country", "state", "city", "address", "occupation", "whatsapp", "instagram", "twitter", "linkedin")


admin.site.register(Contact, ContactAdmin)
admin.site.register(Digital, DigitalAdmin)
admin.site.register(SME, SMEAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Vocation, VocationAdmin)
admin.site.register(Influencer, InfluencerAdmin)