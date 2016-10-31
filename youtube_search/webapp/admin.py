from django.contrib import admin

# Register your models here.
from webapp.models import YoutubeVideo

class YoutubeAdmin(admin.ModelAdmin):
    list_display = ('video_id','video_title','video_description',)
    list_filter = ('video_title',)
    search_fields = ('video_title',)
    ordering = ('video_title',)
    readonly_fields = ('video_id',)

admin.site.register(YoutubeVideo, YoutubeAdmin)