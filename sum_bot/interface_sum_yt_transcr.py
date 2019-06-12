import requests
from yt_transcript.youtube_transcript_api._api import YouTubeTranscriptApi as yt
import json



def access_youtube_json(link):
    try:
        lista = yt.get_transcript(link, languages=['en'])
        return lista
        
    except yt.CouldNotRetrieveTranscript as err:
        print("ERROR: ", err)

def json_to_text(json_list):

    text = ""
    for frag in json_list:
        text += frag.get("text")
    
    return text 

def sum_bot_call(text):

    post_body = bytes(text.encode("utf-8"))

    api_url = "https://www.summarizebot.com/api/summarize?apiKey=ba63c1dc1fae4c04bddc32c6ebae1a4b&size=20&keywords=10&fragments=15&filename=1.txt"

    header = {'Content-Type': "application/octet-stream"}
    r = requests.post(api_url, headers = header, data = post_body)
    json_res = r.json()
    
    return json_res

print("Hola")
if __name__ == "__main__":
    print("Sa")
    videoId_with22_subtitles = "uIb1JU9j-Bk"
    lista = access_youtube_json(videoId_with22_subtitles)

    lista =  json_to_text(lista)

    print(sum_bot_call(lista))