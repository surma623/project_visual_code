from django.contrib.auth.models import User
from django.core.management import BaseCommand

from shopapp.models import Order


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Create order')
        user = User.objects.get(username='alexey')
        order = Order.objects.get_or_create(
            delivery_address='ul. Pushkina, 21-49',
            promocode='Sale234',
            user=user,
        )
        self.stdout.write('Created order {order}'.format(order=order))
