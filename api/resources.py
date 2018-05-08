from tastypie.resources import ModelResource
from api.models import Note
from tastypie.authorization import Authorization

from api.models import User
from tastypie.authentication import BasicAuthentication
from tastypie.resources import ModelResource


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()
        fields = ['name', 'password']

class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'
        authorization = Authorization()
        fields = ['title', 'body']