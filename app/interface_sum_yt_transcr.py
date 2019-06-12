################################################################################
#   Project: FastForward
#   Authors:
#           (c) Uxio Garcia Andrade - uxiog21@gmail.com
#           (c) Xabier Garcia Andrade - xabi.ag.7@gmail.com
#           (c) Alejandro Santorum Varela - alejandro.santorum@gmail.com
#           (c) Borja Docampo Alvarez - bdoc42@gmail.com
#   Date: June 12, 2019
################################################################################

# Importing libraries
import sys
import json
import requests
from yt_transcript.youtube_transcript_api._api import YouTubeTranscriptApi as yt

################################################################################
#   FUNCTION NAME: parse_url
#   INPUT:
#       · link - youtube video url
#   OUTPUT:
#       · youtube video ID
#   DESCRIPTION:
#       · It parses a given youtube video link, returning its ID
################################################################################
def parse_url(link):
    separator = "="
    link = link.split(separator)[1]
    return link


################################################################################
#   FUNCTION NAME: access_youtube_transcript
#   INPUT:
#       · url - youtube video url
#   OUTPUT:
#       · youtube video transcript
#   DESCRIPTION:
#       · It parses a given youtube video link (getting its ID) and it gets
#         its transcript using Youtube API. It returns the downloaded
#         transcript.
################################################################################
def access_youtube_transcript(url):

    link = parse_url(url)

    try:
        lista = yt.get_transcript(link, languages=['en'])
        return lista
    except yt.CouldNotRetrieveTranscript as err:
        raise ValueError(str(err))


################################################################################
#   FUNCTION NAME: transcript_to_text
#   INPUT:
#       · transcript_list - downloaded youtube transcript
#   OUTPUT:
#       · concatenated text of the transcript
#   DESCRIPTION:
#       · It parses a given youtube transcript (it is a list of dictionaries),
#         and concatenates all the subtitles, returning them
################################################################################
def transcript_to_text(transcript_list):
    text = ""
    for frag in transcript_list:
        frag_text = frag.get("text")
        if frag_text != "" and frag_text != " " and frag_text != None:
            text += " " + frag_text

    return text


################################################################################
#   FUNCTION NAME: summ_bot_call
#   INPUT:
#       · text - text of the transcript
#   OUTPUT:
#       · summarized text of the transcript
#   DESCRIPTION:
#       · It summarizes the given text. For prototype reasons, we are
#         getting some information from SumamrizeBot API:
#         https://www.summarizebot.com/summarization_business.html
################################################################################
def summ_bot_call(text):

    post_body = bytes(text.encode("utf-8"))

    api_url = "https://www.summarizebot.com/api/summarize?apiKey=ba63c1dc1fae4c04bddc32c6ebae1a4b&size=20&keywords=10&fragments=15&filename=1.txt"

    header = {'Content-Type': "application/octet-stream"}
    r = requests.post(api_url, headers = header, data = post_body)
    json_res = r.json()

    return json_res


################################################################################
#   FUNCTION NAME: control_f
#   INPUT:
#       · transcript_from_yt - downloaded transcript from youtube
#       · keyword - keyword to search on the transcript
#   OUTPUT:
#       · list of video timestamps where the keyword is mentioned
#   DESCRIPTION:
#       · It looks for all the keyword appeareances and stores its timestamps
#         in a list that it's returned
################################################################################
def control_f(transcript_from_yt, keyword):
    #converting everything to capital letters to avoid case sensitivity
    word = keyword.upper()
    word_coinc = []

    for dictionary in transcript_from_yt:
        if dictionary.get("text").upper().__contains__(word):
            word_coinc.append(dictionary.get("start"))

    return word_coinc

def summarize_from_url(video_id):
    lista = access_youtube_transcript(video_id)
    lista2 = transcript_to_text(lista)
    summarize = summ_bot_call(lista2)
    return summarize[0].get("summary")

def get_keywords_from_uril(video_id):
    lista = access_youtube_transcript(video_id)
    lista2 = transcript_to_text(lista)
    summarize = summ_bot_call(lista2)
    return summarize[0].get("summary")[1].get("keywords")