from django.contrib import admin

from .models import Product, Category, Like, Comment

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Comment)
