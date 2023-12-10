from django.contrib import admin
from .models import Category,Post
# Register your models here.

#for Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',"image_tag","discription","urls","add_date")
    search_fields = ("title",)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ("title",)
    list_filter=("cat",)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post,PostAdmin)