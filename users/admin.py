from django.contrib import admin

from users.models import User

@admin.register(User)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('email', )
    search_fields = ('email', )