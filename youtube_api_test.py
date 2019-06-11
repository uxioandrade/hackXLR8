from youtube_transcript_api import YouTubeTranscriptApi

list = YouTubeTranscriptApi.get_transcript("uIb1JU9j-Bk", languages=['en','es'])

print(list)
