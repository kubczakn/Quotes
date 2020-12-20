from django.contrib import admin
from .models import Haiku, Choice, Question


admin.site.register(Haiku)
admin.site.register(Question)
admin.site.register(Choice)