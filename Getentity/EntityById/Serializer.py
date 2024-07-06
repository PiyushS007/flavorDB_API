from rest_framework import serializers
from .models import FDB_entities


class FDBEntitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FDB_entities
        fields = ['entity_id','category','natural_source_name']
