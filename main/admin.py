from django.contrib import admin
from .models import Payment, Cat, Post, Images, Treningi

# Register your models here.
#admin.site.register(Payment)
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'description', 'value', 'category')

    admin.site.register(Cat)

@admin.register(Treningi)
class TreningiAdmin(admin.ModelAdmin):

    list_display = ('title', 'description', 'date', 'ex01')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'content', 'date', 'thumbnail')

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):

    list_display = ('post', 'image')

    