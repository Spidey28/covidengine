from django.contrib import admin

from .models import Category, Address, Feedback, Post

# admin.site.register(User)
admin.site.register(Category)
admin.site.register(Address)
admin.site.register(Feedback)
admin.site.register(Post)
