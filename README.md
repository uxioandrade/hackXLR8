FastForward: Video analytics
=================================

In today's world, a lot of information is presented in video format. 

However, watching videos takes time. Depending on the video, a lot of time. 

But what if you could access that information before hitting the play button? 

What if you could read a text summary, or jump straight to the interesting part?

## What does it do, exactly?

FastForward extracts information from speech in video files and generates a summary of the contents of the video, the key ideas presented within, as well as links to the most important parts. For this prototype, we are using YouTube videos. Just find one with subtitles and paste the URL in the text box on the site. Then, it will extract a summary of the video using TextRank (having done some NLP processing before), as well as some keywords and the moment they are mentioned in the video

## Quick install guide

Docker is the easiest way to get Fastforward up and running. Just do the following in the repository directory:

```sh
docker build -t fastforward:latest .
docker run -d -p 5000:5000 fastforward
```
