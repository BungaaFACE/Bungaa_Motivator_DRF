from django.contrib import admin

from motivator.models import Habit, HabitSubscription

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('user', 'place', 'time', 'action', 'is_nice', 'related_habit', 'period', 'reward', 'time_to_do', 'is_public')
    list_filter = ('is_nice', 'is_public')
    search_fields = ('user', 'action')

@admin.register(HabitSubscription)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('user', 'habit', 'next_date_send')
    search_fields = ('user', 'habit')