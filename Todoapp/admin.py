from django.contrib import admin
from .models import User
from .models import Todo
from .models import Comment
from .models import Category
from .models import TodoCategory
# Register your models here.

admin.site.register(User)
admin.site.register(Todo)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(TodoCategory)