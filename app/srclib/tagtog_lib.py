import requests
from app.srclib import interface_sum_yt_transcr as i_sum

tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"

auth = requests.auth.HTTPBasicAuth(username='uxioandrade', password='')

project_name = "hack_test2"
project_owner = "uxioandrade"

#videoId_with22_subtitles = "uIb1JU9j-Bk"
#videoId_withNone_Subtitles = "QXSDT3v8wsQ"

#how to learn a foreign language

def send_text_to_annotate(url):
    list_of_sentences = i_sum.access_youtube_transcript(url)
    text_to_annotate = i_sum.transcript_to_text(list_of_sentences)
    params = {'project': project_name, 'owner': project_owner, 'output':'weburl'}
    payload = {'text': text_to_annotate}
    response = requests.post(tagtogAPIUrl, params=params, auth=auth, data=payload)
    return response
