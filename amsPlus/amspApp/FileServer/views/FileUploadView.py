import chunk
import json
import os
import shutil
import uuid
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from rest_framework import views
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from amspApp.FileServer.models import File
from amspApp.FileServer.serializers.FileSerializer import FileSerializer
from amspApp._Share.CharacterHandle import ShowUtfCharacterCode
from amspApp._Share.GetMime import GetMimeType


class FileUploadViewSet(views.APIView):
    parser_classes = (FileUploadParser,)

    fileFolder = "/var/www/amspfiles/"


    def generateGuidName(self):
        return uuid.uuid4().hex + uuid.uuid4().hex


    def loadFile(self, request, *args, **kwargs):
        pass
    @never_cache
    def get(self, request, format=None):
        fileEncoded = request.query_params["q"]
        fileToDownload = File.objects.get(decodedFileName=fileEncoded)
        # reading file into memory
        f = fileToDownload.originalFileName
        fsock = open(self.fileFolder + fileEncoded, "rb")
        mime = GetMimeType(f.split(".")[1])
        response = HttpResponse(fsock, content_type=mime)
        response['Content-Disposition'] = 'attachment; filename=%s' % (f)
        # response['Cache-Control'] = 'no-cache'
        return response


    def post(self, request, *args, **kwargs):
        file_obj = ""
        if "upload" in request.FILES:
            file_obj = request.FILES['upload']
        if "file" in request.FILES:
            file_obj = request.FILES['file']

        max_upload_size = 1024 * 1024 * 4
        if file_obj.size > max_upload_size:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        # ...
        # do some staff with uploaded file
        # ...
        decodeName = self.generateGuidName()
        chunk = request.REQUEST.get('chunk', '0')
        chunks = request.REQUEST.get('chunks', '0')

        temp_file = self.fileFolder + 'tmp_' + decodeName + '_insecure.tmp'
        with open(temp_file, ('wb' if chunk == '0' else 'ab')) as f:
            for content in file_obj.chunks():
                f.write(content)
        stored_filename = ""

        shutil.copyfile(temp_file, self.fileFolder + decodeName)
        os.remove(temp_file)

        env = request._request.environ
        newFile = {
            "userID": request.user.id,
            "originalFileName": ShowUtfCharacterCode(file_obj.name),
            "decodedFileName": decodeName,
            "uploaderIP": {
                "fileSize": file_obj.size,
                "home": env["HOME"],
                "browser": env["HTTP_USER_AGENT"],
                "ip": env["REMOTE_ADDR"]
            }
        }
        # newFileS = FileSerializer(data = newFile)
        newFile = File(**newFile)
        newFile.save()
        # if newFileS.is_valid():
        # newFileS.create(validated_data=newFile)
        result = {"name": decodeName}
        if "upload" in request.FILES:
            funcNum = request.QUERY_PARAMS["CKEditorFuncNum"]
            message = ""
            url = "/api/v1/file/upload?q=" + decodeName
            hh = "<script type='text/javascript'>window.parent.CKEDITOR.tools.callFunction({0}, '{1}', '{2}');</script>".format(
                funcNum, url, message)
            return HttpResponse(hh)

        return Response(result)