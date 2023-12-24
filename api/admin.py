from django.contrib import admin
from .models import Student1
# Register your models here.
@admin.register(Student1)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','stuname','email']