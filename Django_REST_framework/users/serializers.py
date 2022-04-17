# from rest_framework.relations import StringRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer, StringRelatedField
from .models import User


class UserModelSerializer(HyperlinkedModelSerializer):
    uid = StringRelatedField(read_only=True)

    class Meta:
        model = User
        fields = ('uid', 'first_name', 'last_name', 'email', 'username')
        # fields = '__all__'
