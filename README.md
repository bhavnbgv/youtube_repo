# youtube_repo
 This is a small program using Python/Django
 
 1. A Django application with a simple ORM class to work with YouTube videos. with following parameters:#
      - YouTube video ID
      - Video Title
      - Video Description
 
 2. Using Python YouTube API client to search YouTube for videos with given Channel ID.
      Example Channel ID: UCMDV6J2hWXet7ZCfgrXGgeg
      If we pass the channel ID as filter without any search query we'll get all the videos in channel with a paginated result.
 
 3. Using Django Rest Framework to create a couple of API endpoint to list the YouTube videos.
      - GET request to list all videos
      - GET request to get video details based on ID
 
 4. very minimal HTML page to consume the above API and display results to user.
      - Video list page
      - Video detail page
