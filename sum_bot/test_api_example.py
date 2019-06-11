import requests

# Text for processing in UTF-8 encoding
text_for_processing = u"Planet has only until 2030 to stem catastrophic climate change, experts warn."
# Create bytes representation of the text
post_body = bytes(text_for_processing.encode('utf-8'))

# API URL
# You can change 'summarize' to different endpoints: sentiment, keywords, etc.
api_url = "https://www.summarizebot.com/api/summarize?apiKey=ba63c1dc1fae4c04bddc32c6ebae1a4b&size=20&keywords=10&fragments=15&filename=1.txt"
# HTTP header
header = {'Content-Type': "application/octet-stream"}
r = requests.post(api_url, headers = header, data = post_body)
json_res = r.json()
print(json_res)
