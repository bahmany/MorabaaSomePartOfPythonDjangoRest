from datetime import datetime
from mongoengine import Document
from mongoengine import *

__author__ = 'mohammad'

class File(DynamicDocument):
    userID = IntField(required=True)
    originalFileName = StringField(max_length=50,required=True)
    decodedFileName = StringField(max_length=250,required=True)
    dateOfPost = DateTimeField(default=datetime.now(), required=False)
    downloadTimes = DictField(required=False)
    uploaderIP = DictField(required=False)
    extra = DictField(required=False)



