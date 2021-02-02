from django.db import models
from neomodel import StructuredNode, StringProperty, DateProperty, UniqueIdProperty, Relationship 


# Create your models here.

class User(StructuredNode):

    uid = UniqueIdProperty()
    username = StringProperty()


class Idea(StructuredNode):
    uid = UniqueIdProperty()
    title = StringProperty()
    description = StringProperty()
    author = Relationship(User, 'created_by')
