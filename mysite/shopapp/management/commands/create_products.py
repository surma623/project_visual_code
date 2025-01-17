from django.core.management import BaseCommand

from shopapp.models import Product

class Command(BaseCommand):
    """
    Creates products
    """

    def handle(self, *args, **options):

        self.stdout.write('Create products')

        products_names = [
            'Laptop',
            'Desktop',
            'Smartphone',
        ]

        for products_name in products_names:
            product, created = Product.objects.get_or_create(name=products_name)
            self.stdout.write('Created product {products_name}'.format(products_name=product.name))

        self.stdout.write(self.style.SUCCESS('Products created'))