from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from apiclient.discovery import build
from apiclient.errors import HttpError
from globalconfig import API_KEY,API_NAME,API_VERSION
from django.http.response import HttpResponse
from webapp.models import YoutubeVideo
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from webapp.serializers import YoutubeVideoSerializer

# Create your views here.
@api_view(['GET','POST'])
def VideoList(request):
    
    if request.method=='POST':
        data = request.POST
        print data,"data******\n"
        
        query = data.get('searchkeyword')
        channel = data.get('channelid')
        page_token = data.get('pagetoken')
        
        print page_token,"page token"
        
        print query,channel
        
        if query == "":
            query=None
        if channel=="":
            channel=None
        if page_token=="":
            page_token=None
        
        print query,channel,page_token
        
        youtube = build(API_NAME,API_VERSION,developerKey=API_KEY)
        
        print youtube,"youtube********\n"
        
        try:
        
            search_response = youtube.search().list(
            q=query,
            part="id,snippet",
            channelId=channel,
            pageToken=page_token,
            maxResults=10).execute()
            
        except Exception, ex:
            msg = json.loads(ex.content)
            ret_msg = msg['error']['message']
            return HttpResponse(json.dumps({"videos_list":ret_msg}), content_type="application/json")
        
        print search_response,"search response********\n"
        
        next_page = search_response.get('nextPageToken')
        prev_page = search_response.get('prevPageToken')
        
        if next_page == None:
            next_page=""
        if prev_page == None:
            prev_page=""
            
        videos = []
        
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                videos.append("%s ---- %s " % (search_result["id"]["videoId"],search_result["snippet"]["title"]))
                videos.append("<br>")
                if not YoutubeVideo.objects.filter(video_id=search_result["id"]["videoId"]).exists():
                    yt = YoutubeVideo(video_id=search_result["id"]["videoId"],video_title=search_result["snippet"]["title"],video_description=search_result["snippet"]["description"])
                    yt.save()
        
        print videos        
        
        return HttpResponse(json.dumps({"videos_list":videos,"next_page" : next_page, "prev_page" : prev_page}), content_type="application/json")
        
    return render_to_response('videolist.html',context_instance=RequestContext(request))


@api_view(['GET', 'POST'])
def RestApiList(request):
    
    videos = YoutubeVideo.objects.all()
    serializer = YoutubeVideoSerializer(videos, many=True)
    
    if request.method == 'POST':
        serializer = YoutubeVideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def VideoDetail(request, pk):
    try:
        videos = YoutubeVideo.objects.get(pk=pk)
    except Exception, ex:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = YoutubeVideoSerializer(videos)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = YoutubeVideoSerializer(videos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        videos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







