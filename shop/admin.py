from django.contrib import admin
from shop.models.Slider import Slider
from django.utils.html import format_html
from shop.models.Collection import Collection
from shop.models.Product import Product
from shop.models.Category import Category
from shop.models.Image import Image

class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_image')
    list_display_links = ('title',)
    
    def display_image(self, obj):
        return format_html(f'<img src="{ obj.image.url }" width="150" />')
    
    display_image.short_description = 'image'
    
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_image')
    list_display_links = ('title',)
    
    def display_image(self, obj):
        return format_html(f'<img src="{ obj.image.url }" width="150" />')
    
    display_image.short_description = 'image'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_image')
    list_display_links = ('name',)
    
    def display_image(self, obj):
        return format_html(f'<img src="{ obj.image.url }" width="150" />')
    
    display_image.short_description = 'image'
    exclude = ('slug',)

class ImageInline(admin.TabularInline):
    model = Image
    extra = 3
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('id', 'name', 'solde_price', 'is_best_seller','is_featured', 'is_special_offer', 'is_new_arrival', 'regular_price', 'display_image')
    list_display_links = ('name',)
    list_editable = ('is_best_seller','is_featured', 'is_special_offer', 'is_new_arrival')
    list_per_page = 5
    
    def display_image(self, obj):
        first_image = obj.images.first()
        if not first_image:
            return ''
        return format_html(f'<img src="{ first_image.image.url }" height="90" width="80" />')
    
    exclude = ('slug',)
    display_image.short_description = 'image'

admin.site.register(Slider, SliderAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

