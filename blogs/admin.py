from django.contrib import admin
from .models import Category, Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('title',)}
  list_display = ('title', 'category', 'author', 'is_featured','status', 'created_at') 
  search_fields = ('id','title', 'category__category__name', 'author__username')     
  list_filter = ('category', 'author', 'is_featured', 'status')


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
