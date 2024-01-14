from motivator.models import HabitSubscription
from datetime import timedelta, datetime, date
from django.conf import settings
from django.utils.timezone import make_aware
from celery import shared_task
import requests
import traceback


@shared_task
def habit_subscription_sender():
    TOKEN = settings.TELEGRAM_BOT_TOKEN
    SEND_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    
    subs = HabitSubscription.objects.filter(
        next_date_send__lte=make_aware(datetime.now())
    )
    
    for sub in subs:
        'я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]'
        text = f'В {sub.habit.time} я буду {sub.habit.action} в {sub.habit.place}.\n' + \
            'В награду я получу:'
        if sub.habit.reward:
            text += f' {sub.habit.reward}.'
        else:
            text += f' в {sub.habit.related_habit.time} я буду {sub.habit.related_habit.action} в {sub.habit.related_habit.place}.'

        response = requests.post(SEND_URL, json={'chat_id': sub.user.telegram_id, 'text': text})
        if response.status_code == 200:
            sub.next_date_send = datetime.combine(date.today() + timedelta(days=sub.habit.period), sub.habit.time)
            sub.save()