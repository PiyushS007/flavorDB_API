from .models import FDB_entities
from django.db.models import Q


class ServiceLayer:

    @staticmethod
    def get_entity(id):
        return FDB_entities.objects.get(entity_id=id)

    @staticmethod
    def get_entities(category=None):
        query = Q()
        if category:
            query &= Q(category=category)

        return FDB_entities.objects.filter(query)

    @staticmethod
    def get_entity_by_natural_source(natural_source):
        return FDB_entities.objects.filter(natural_source_name=natural_source)

    @staticmethod
    def search(category, natural_source):

        if category:

            return FDB_entities.objects.filter(category__icontains=category).values_list('category', flat=True)

        if natural_source:
            return FDB_entities.objects.filter(natural_source_name__icontains=natural_source).values_list('natural_source_name', flat=True)
