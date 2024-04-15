from django.contrib import admin
from .models import user,product

@admin.register(user)

class useradmin(admin.ModelAdmin):
    list_display=('email','is_approved','is_admin')
    search_fields=('emails',)
    list_filter=('is_approved','is_admin')

@admin.register(product)

class productadmin(admin.ModelAdmin):
    list_display=('name','price','user')
    search_fields=('name',)
    list_filter=('user',)

