from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Keyword)
admin.site.register(Merchant)
admin.site.register(Transaction)