from rest_framework.serializers import ModelSerializer, StringRelatedField, \
    PrimaryKeyRelatedField, HyperlinkedModelSerializer

from users.models import User
from .models import Project, TODO


class SimpleUserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ProjectModelSerializer(HyperlinkedModelSerializer):
    # worker = StringRelatedField(many=True, )
    uid = StringRelatedField(read_only=True)

    class Meta:
        model = Project
        # exclude = ['uid']
        fields = '__all__'


# class TODOModelSerializer(HyperlinkedModelSerializer):
class TODOModelSerializer(ModelSerializer):
    # author = StringRelatedField()
    # project = StringRelatedField()
    uid = StringRelatedField(read_only=True)

    class Meta:
        model = TODO
        # exclude = ['uid']
        fields = '__all__'


class TestUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('uid', 'first_name', 'last_name', 'email', 'username')
        # fields = '__all__'


class TestProjectSerializerBase(ModelSerializer):
    # worker = TestUserSerializer(many=True, )

    class Meta:
        model = Project
        fields = ('name', 'link', 'worker')


class TestProjectSerializer(ModelSerializer):
    worker = TestUserSerializer(many=True, )

    class Meta:
        model = Project
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class UserSerializerWithFields(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'email', 'username',
                  'is_superuser', 'is_staff')
