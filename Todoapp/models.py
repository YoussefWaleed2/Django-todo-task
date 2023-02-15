from django.db import models

# Create your models here.

class User (models.Model):
    name = models.CharField (max_length=50)
    email = models.EmailField ()
    sms = models.TextField ()
    created_at = models.DateField ()
    updated_at = models.DateField ()

class Todo (models.Model):
    title = models.CharField (max_length=50)
    description = models.TextField ()
    deadline = models.DateField()
    notifications = models.PositiveIntegerField()
    created_at = models.DateField()
    updated_at = models.DateField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

class Comment (models.Model):
    body = models.TextField()
    created_at = models.DateField()
    updated_at = models.DateField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    todo_id = models.ForeignKey(Todo,on_delete=models.CASCADE)


class Category (models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateField()
    updated_at = models.DateField()


class TodoCategory (models.Model):
    todo_id = models.ForeignKey(Todo,on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)