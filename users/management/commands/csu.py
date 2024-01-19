import os
from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@mail.ru',
            first_name='admin',
            last_name='admin',
            is_staff=True,
            is_superuser=True,
            chat_id=os.getenv('CHAT_ID_ADMIN'),
            is_active=True,
        )

        user.set_password(os.getenv('ADMIN_PASSWORD'))
        # user.set_password('19Sonnik94')
        user.save()
