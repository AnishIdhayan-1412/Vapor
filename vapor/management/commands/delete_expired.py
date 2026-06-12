from django.core.management.base import BaseCommand
from django.utils import timezone
from vapor.models import Confession

class Command(BaseCommand):
    help = 'Deletes confessions older than 96 hours'

    def handle(self, *args, **kwargs):
        expiry_threshold = timezone.now() - timezone.timedelta(hours=48)
        expired = Confession.objects.filter(created_at__lt=expiry_threshold)
        count = expired.count()
        expired.delete()
        self.stdout.write(f'Deleted {count} expired confessions.')