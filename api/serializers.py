from rest_framework import serializers
from viewer.models import Media


class MediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'
