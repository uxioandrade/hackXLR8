import requests
from yt_transcript.youtube_transcript_api._api import YouTubeTranscriptApi as yt

tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"

auth = requests.auth.HTTPBasicAuth(username='uxioandrade', password='lalin2019')

project_name = "hack_test2"
project_owner = "uxioandrade"

#videoId_with22_subtitles = "uIb1JU9j-Bk"
#videoId_withNone_Subtitles = "QXSDT3v8wsQ"

 #how to learn a foreign language
video_id_test_countries = "P-b4SUOfn_4"

f = open("transcript_different_countries_text.txt", "a")



def send_text_to_annotate():
    video_id_test = "o_XVt5rdpFY"
    try:
        list = yt.get_transcript(video_id_test_countries, languages=['en'])
        text = ""
        for i in list:
            text_to_annotate += i['text']
    except yt.CouldNotRetrieveTranscript as err:
        print("ERROR: ", err)
    params = {'project': project_name, 'owner': project_owner, 'output':'weburl'}
    payload = {'text': text_to_annotate}
    response = requests.post(tagtogAPIUrl, params=params, auth=auth, data=payload)
    
