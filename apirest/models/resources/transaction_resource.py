from import_export import resources
from .. import Transaction

class TransactionResource(resources.ModelResource):
    class Meta:
        model = Transaction