from django.contrib import admin
from .models import *
from .models.resources import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    resources_classes = [CategoryResource]

@admin.register(Keyword)
class KeywordAdmin(ImportExportModelAdmin):
    resources_classes = [KeywordResource]

@admin.register(Merchant)
class MerchantAdmin(ImportExportModelAdmin):
    resources_classes = [MerchantResource]

@admin.register(Transaction)
class TransactionAdmin(ImportExportModelAdmin):
    resources_classes = [TransactionResource]