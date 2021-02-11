from django.db import models
from neomodel import * 
from neomodel import StructuredNode, StructuredRel, StringProperty, DateProperty, UniqueIdProperty, Relationship, RelationshipTo, RelationshipFrom

# Create your models here.

class User(StructuredNode):

    uid = UniqueIdProperty()
    username = StringProperty()
    
    ''' 
    #TODO User Authentication 
    friends = Relationship('User', 'FRIEND')
    '''

class Idea(StructuredNode):
    uid = UniqueIdProperty()
    label = StringProperty()
    description = StringProperty()
    author = Relationship('User', 'created_by')

    parents = RelationshipFrom('Idea', 'parent')
    siblings = Relationship('Idea', 'sibling')
    children = RelationshipTo('Idea', 'child')


'''

### Improvements, but not necessary


class FriendRel(StructuredRel):
    pass

class IdeaRel(StructuredRel)
    pass

'''
