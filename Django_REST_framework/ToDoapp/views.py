from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from ToDoapp.filters import ProjectFilter
from ToDoapp.models import Project, TODO
from ToDoapp.serializers import ProjectModelSerializer, TODOModelSerializer, \
    TestProjectSerializer, TestProjectSerializerBase


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    # serializer_class = TestProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = ProjectFilter

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TestProjectSerializer

        return TestProjectSerializerBase


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
    permission_classes = [permissions.IsAuthenticated]
