from django.core.management import BaseCommand

from motivator.tasks import habit_subscription_sender


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        habit_subscription_sender()