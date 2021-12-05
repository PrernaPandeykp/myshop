import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()
from myapp.add_products import add_product

add_product()
