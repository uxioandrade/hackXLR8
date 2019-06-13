################################################################################
#   Project: FastForward
#   File: interface_summ_yt_transcr.py
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
import re
import requests
import numpy as np
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
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
    counter = 0
    np.random.seed(42)
    for frag in transcript_list:
        text += " " + frag.get("text")
        if counter>=3:
            choice = np.random.choice(2,1)[0]
            if choice:
                counter = 0
                text += ".\n"
        counter += 1
    text += "."
    return text


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


def _summary_caps(summary_str):
    summary = list(summary_str)
    length = len(summary)
    i = 0
    while(i<length):
        if summary[i] == '.':
            while(i<length):
                i += 1
                if i == length:
                    break
                if summary[i].isalpha():
                    summary[i] = summary[i].upper()
                    break
        i+=1
    return "".join(summary)

################################################################################
#   FUNCTION NAME: summ_transcript_keywords
#   INPUT:
#       · transcript_list - dictionary of youtube transcripts
#       · word_counter (optional) - number of words of the summary (default: 100)
#       · number_keywords (optional) - number of keywords to search (default: 4)
#   OUTPUT:
#       · summarize and the list of found keywords
#   DESCRIPTION:
#       · It uses several machine learning algorithms in order to summarize a
#         given transcript and detect the keywords of the summary
################################################################################
def summ_transcript_keywords(transcript_list , word_counter = 100 , number_keywords = 4):

    lista = transcript_to_text(transcript_list)

    summary = summarize(lista , word_count = word_counter).capitalize()
    re.sub(r"(?:^|(?:[.!?'\n']\s+))(.)",lambda m: m.group(0).upper(), summary)
    keywords_list = keywords(lista , words = number_keywords , lemmatize=True)

    return _summary_caps(summary), keywords_list


def summarize_from_url(url=None):
    transcript = access_youtube_transcript(url)

    return summ_transcript_keywords(transcript)


# Testing
if __name__ == "__main__":
    videoId_example = "https://www.youtube.com/watch?v=U51MSK6nSQE"
    lst = access_youtube_transcript(videoId_example)
    print("SUMMARY:")
    print(summ_transcript_keywords(lst)[0])
    print("KEYWORDS:")
    print(summ_transcript_keywords(lst)[1])
    print("LIST OF KEYWORD(0) APPEARENCES:")
    print(control_f(lst, summ_transcript_keywords(lst)[1][0]))
