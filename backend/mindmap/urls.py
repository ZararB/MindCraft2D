from django.urls import path

from . import views 


urlpatterns = [
        path('', views.index, name='index'),
        path('new', views.new, name='new'),
        path('load', views.load, name='load'),
        path('learning', views.learning, name='learning'),
        path('settings', views.settings, name='settings'),
        path('save', views.save, name='save'),
        path('open', views.open, name="open"),
        path('deleteNode', views.deleteNode, name='deleteNode'),
        path('setup', views.setupDb, name='setupDb'),
        path('<str:rootNodeLabel>', views.mindmap, name='mindmap')
]


