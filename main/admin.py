from django.contrib import admin
from .models import Payment, Category

# Register your models here.
#@admin.register(Payment)
#class PaymentAdmin(admin.ModelAdmin):

admin.site.register(Payment)
admin.site.register(Category)