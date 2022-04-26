from reco.models import AllData
from rest_framework import serializers


class AllDataSerializer(serializers.HyperlinkedModelSerializer):
    img = serializers.ImageField(use_url=True)

    class Meta:
        model = AllData
        fields = ('id', 'url', 'title','genre','img','desc','key_word')
