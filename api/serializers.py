from rest_framework import serializers
from api.models import COSbucket


class COSbucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = COSbucket
        fields = ('vodel_address', 'image_address')


