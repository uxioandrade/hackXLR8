# Importing library to test
import interface_summ_yt_transcr


def is_link(url):
    if url.__contains__("="):
        return True
    return False

def without_subs_or_avail_languages(url, sub_prefix=None):
    try:
        access_youtube_transcript(link)
        return True
    except ValueError:
        return False

def transcript_to_text_dict_has_text(transcript_list):
    if transcript_to_text(transcript_list):
        return True
    else:
        return False



if __name__ == "__main__":
