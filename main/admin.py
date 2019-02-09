from django.contrib import admin
from .models import Payment, Category

# Register your models here.
#admin.site.register(Payment)
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'description', 'value')

    admin.site.register(Category)