import django_filters
from amspApp.CompaniesManagment.Positions.models import PositionsDocument
__author__ = 'mohammad'
#
#
# def searcTxt(queryset,txt) :
#     queryest.

class MemberFilter():
    def __init__(self):
        pass
    def filter(self, querySet,kwargs):
        # amir = querySet._collection_obj.find({"$query": {
        #     "$text": {"$search": 'ce'},}})
        if not 'q' in kwargs.keys():
            return querySet
        if kwargs["q"] == "":
            return querySet
        return querySet.search_text(kwargs["q"]).order_by('$text_score')


