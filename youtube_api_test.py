from yt_transcript.youtube_transcript_api._api import YouTubeTranscriptApi as yt
import json 

videoId_with22_subtitles = "uIb1JU9j-Bk"
videoId_withNone_Subtitles = "QXSDT3v8wsQ"
try:
    lista = yt.get_transcript(videoId_with22_subtitles, languages=['en'])
    print(lista)
    
except yt.CouldNotRetrieveTranscript as err:
    print("ERROR: ", err)