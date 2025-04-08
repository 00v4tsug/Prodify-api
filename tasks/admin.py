from django.contrib import admin

# Register your models here.
from .models import Task  # importa o modelo

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'completed', 'priority', 'due_date', 'created_at']
    list_filter = ['completed', 'priority', 'due_date']
    search_fields = ['title', 'description']
