
from django.db import models


class FDB_entities(models.Model):
    entity_id = models.IntegerField(primary_key = True)
    category = models.CharField(max_length=100, null=True)
    category_readable = models.CharField(max_length=100, null=True)
    entity_alias = models.CharField(max_length=100, null=True)
    entity_alias_basket = models.CharField(max_length=500, null=True)
    entity_alias_readable = models.CharField(max_length=100, null=True)
    # entity_name = models.CharField(max_length=100, null=True)
    entity_alias_synonyms = models.CharField(max_length=1000, null=True)
    entity_alias_url = models.CharField(max_length=200, null=True)
    natural_source_name = models.CharField(max_length=100, null=True)
    natural_source_url = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'fdb_entities'
