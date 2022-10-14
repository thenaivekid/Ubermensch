from django.contrib import admin

from .models import Quotes
# Register your models here.
class MyAdminSite(admin.AdminSite):
    #for custom header in admin page
    site_header="DeepDive Administration"

#creating new instance of MyAdminSite class
admin_site = MyAdminSite(name="myadmin")

class QuotesAdmin(admin.ModelAdmin):
    list_display = ['quote','saidby']
    search_fields =['quote','saidby']

 #using custom instance of admin site   
admin_site.register(Quotes,QuotesAdmin)