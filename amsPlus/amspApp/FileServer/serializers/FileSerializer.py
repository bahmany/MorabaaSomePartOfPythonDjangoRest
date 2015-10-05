from rest_framework_mongoengine.serializers import DocumentSerializer, DynamicDocumentSerializer
from amspApp.FileServer.models import File


class FileSerializer(DynamicDocumentSerializer):
    class Meta:
        model = File
        # dept = 2
        fields = (
            "userID",
            "originalFileName",
            "decodedFileName",
            "dateOfPost",
            "downloadTimes",
            "uploaderIP",
            "extra",

        )