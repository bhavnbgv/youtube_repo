from rest_framework import serializers
from webapp.models import YoutubeVideo

class YoutubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideo
        fields = ('video_id', 'video_title', 'video_description')


