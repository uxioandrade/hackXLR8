from transcript.youtube_transcript_api._api import YouTubeTranscriptApi as yt

seeYouLater_ClashOfClans_videoId = "uIb1JU9j-Bk"
try:
    list = yt.get_transcript("QXSDT3v8wsQ")
except yt.CouldNotRetrieveTranscript as err:
    print("ERROR: ", err)