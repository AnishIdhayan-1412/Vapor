from django.db import models

# Create your models here.

from django.utils import timezone

class Confession(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    report_count = models.IntegerField(default=0)
    is_removed = models.BooleanField(default=False)

    def expiry_time(self):
        return self.created_at + timezone.timedelta(hours=48)

    def is_expired(self):
        return timezone.now() > self.expiry_time()

    def time_remaining(self):
        remaining = self.expiry_time() - timezone.now()
        if remaining.total_seconds() <= 0:
            return "Vanished"
        hours = int(remaining.total_seconds() // 3600)
        minutes = int((remaining.total_seconds() % 3600) // 60)
        return f"{hours}h {minutes}m remaining"

    def __str__(self):
        return self.text[:50]
