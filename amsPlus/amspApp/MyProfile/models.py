from datetime import datetime
from mongoengine import *



#
# class ProfileDetailsField(EmbeddedDocument):
#     AboutMe=StringField(max_length=200)
#     Name
#     Phones
#     Title
#     profileAvatar
#     profileHeaderBackground
#     friends





class Profile(Document):
    userID = IntField()
    emails = ListField()
    friends = ListField()
    companyMembers = ListField()
    dateOfPost = DateTimeField(default=datetime.now())
    extra = DictField()

    meta = {'indexes': [

        {'fields': ['$extra.Name', "$extra.AboutMe.detail", "$extra.AboutMe.title", "$extra.Title"],
         'default_language': 'english',
         'weights': {'extra.Name':1, "extra.AboutMe.detail":1, "extra.AboutMe.title":1, "extra.Title":1}
        },

    ],
    }




class ProfileComments(EmbeddedDocument):
    authorUserID = IntField()
    profile = ReferenceField(Profile)
    dateOfPost = DateTimeField(default=datetime.now())
    text = StringField(max_length=400)
    likes = DictField()
    extra = DictField()


class Posts(Document):
    authorUserID = IntField()
    profile = ReferenceField(Profile)
    dateOfPost = DateTimeField(default=datetime.now())
    revisions = ListField() # this field saves revisions with old styles and last gesture ..
    likes = ListField()
    text = StringField(max_length=9000)
    extra = DictField()

class PostsComments(EmbeddedDocument):
    authorUserID = IntField()
    profile = ReferenceField(Posts)
    dateOfPost = DateTimeField(default=datetime.now())
    text = StringField(max_length=400)
    likes = DictField()
    extra = DictField()






