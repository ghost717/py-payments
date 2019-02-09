from django.contrib import admin
from .models import Payment, Cat

# Register your models here.
#admin.site.register(Payment)
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'description', 'value', 'category')

    admin.site.register(Cat)