from django.contrib import admin
from .models import Group,Profile,Question,Choice

# Register your models here.
admin.site.register(Choice)
admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Group)
