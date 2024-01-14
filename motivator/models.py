from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    user = models.ForeignKey(User, verbose_name=_("пользователь"), on_delete=models.CASCADE)
    place = models.CharField(verbose_name=_("место"), max_length = 150)
    time = models.TimeField(verbose_name=_("время"), auto_now=False, auto_now_add=False)
    action = models.CharField(verbose_name=_("действие"), max_length = 150)
    is_nice = models.BooleanField(verbose_name=_("приятная привычка"), default=False)
    related_habit = models.ForeignKey('self', verbose_name=_("связанная привычка"), on_delete=models.CASCADE, **NULLABLE)
    period = models.PositiveIntegerField(verbose_name=_("периодичность (в днях)"))
    reward = models.CharField(verbose_name=_("вознаграждение"), max_length = 150, **NULLABLE)
    time_to_do = models.PositiveIntegerField(verbose_name=_("время на выполнение (сек)"))
    is_public = models.BooleanField(verbose_name=_("публичная привычка"), default=False)
    
    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
    
    def __str__(self):
        return self.action

class HabitSubscription(models.Model):
    user = models.ForeignKey(User, verbose_name=_("пользователь"), on_delete=models.CASCADE)
    habit = models.ForeignKey(Habit, verbose_name=_("привычка"), on_delete=models.CASCADE)
    next_date_send = models.DateTimeField(verbose_name=_("Следующая дата отправки"), auto_now=False, auto_now_add=True)
    

    class Meta:
        verbose_name = 'Подписка на привычки'
        verbose_name_plural = 'Подписки на привычки'
    
    def __str__(self):
        return f'{self.habit.action} для {self.user.email}'