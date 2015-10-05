from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from amspApp.CompaniesManagment.Charts.models import Chart
from amspApp._Share.DynamicFieldModelSerializer import DynamicFieldsModelSerializer


__author__ = 'mohammad'


class ChartSerializer(DynamicFieldsModelSerializer):
    title = serializers.CharField(
        required=True,
        help_text=_("Title of the position you prefer to make in your organization"),
        label=_("Position title"),
        max_length=30,
        min_length=3,
        allow_null=False,
        allow_blank=False,

        style={
            'ng-model': 'chart.title'
        }
    )

    CompanyID = serializers.CharField(source="owner.id")
    CompanyName = serializers.CharField(source="owner.name")

    class Meta:
        model = Chart
        fields = ("id", "title", "top", "post_date", "owner", 'CompanyID',"CompanyName",)



    """
    this def creates default chart for default company automatically after
     user registration
     and then return second chart created as CEO

    """

    def create_default_chart(self, companyInstance):
        newChart1 = Chart(
            top=None,
            title=companyInstance.name,
            owner=companyInstance,
        )
        newChart1.save()
        newChart2 = Chart(
            top=newChart1,
            title=_("CEO"),
            owner=companyInstance
        )
        newChart2.save()
        newChart3 = Chart(
            top=newChart2,
            title=_("Commerce Manager"),
            owner=companyInstance
        )
        newChart3.save()
        newChart4 = Chart(
            top=newChart2,
            title=_("Finance Manager"),
            owner=companyInstance
        )
        newChart4.save()
        newChart5 = Chart(
            top=newChart2,
            title=_("Assistant"),
            owner=companyInstance
        )
        newChart5.save()
        return newChart2

    def get_json_chart(self, companyInstace):
        charts = Chart.objects.all().filter(owner=companyInstace)
        # if charts.count() == 0:
        #     self.create_default_chart(companyInstace)
        #     self.get_json_chart(companyInstace)
        # # getting top level of chart
        for chart in charts:
            if chart.top == None:
                stater = chart

        output = {}

        def createDict(dict, parentItem, items):
            subitems = items.filter(top_id=parentItem)
            v = []
            for item in subitems:
                v.append({"name": item.title, "id": item.id, "children": createDict(output, item.id, charts)})
            return v

        output = {"name": stater.title, "id": stater.id,
                  "children": createDict(output, stater.id, charts)}
        return output






