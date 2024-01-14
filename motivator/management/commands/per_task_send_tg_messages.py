from django.core.management import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from datetime import datetime
from django.utils.timezone import make_aware


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        schedule, _ = IntervalSchedule.objects.get_or_create(
            every=5,
            period=IntervalSchedule.MINUTES,
        )

        PeriodicTask.objects.create(
            interval=schedule,
            name='Send motivations to Telegram',
            task='motivator.tasks.habit_subscription_sender',
            start_time=make_aware(datetime.now()),
            description='Send motivations to Telegram'
        )
