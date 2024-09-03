from django.contrib import admin
from .models import TextPost,PollPost,Choice
# Register your models here.

admin.site.register(TextPost)
admin.site.register(PollPost)
admin.site.register(Choice)
