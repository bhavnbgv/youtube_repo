from django.db import models

# Create your models here.
class YoutubeVideo(models.Model):
    video_id = models.CharField(max_length=15,primary_key=True)
    video_title = models.CharField(max_length=400)
    video_description = models.TextField(max_length=2000)

    def __unicode__(self):
        return self.video_id
    
    class Meta:
        managed = True
        db_table = 'youtube_videos'
        app_label = 'webapp'