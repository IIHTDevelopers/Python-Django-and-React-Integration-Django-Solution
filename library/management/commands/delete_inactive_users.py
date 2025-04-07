
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import timedelta

class Command(BaseCommand):
    help = 'Deletes all inactive users who have not logged in within the past 6 months.'

    def handle(self, *args, **kwargs):
        # Define the cutoff time for inactivity (6 months)
        cutoff_date = timezone.now() - timedelta(days=180)
        
        # Find all users who haven't logged in within the last 6 months
        inactive_users = User.objects.filter(last_login__lte=cutoff_date)
        
        # Count how many users are inactive
        count = inactive_users.count()

        if count > 0:
            # Delete inactive users
            inactive_users.delete()

