import pymongo
from pprint import pprint
import pandas as pd
import numpy as np
import datetime

client = pymongo.MongoClient("mongodb+srv://admin:vivavoxadmin@climargy-adg0v.mongodb.net/test?retryWrites=true")
db = client.taotai

collection = db['Transcript']
'''
tweet_dict = {'text': '@DaveMccrossen You make an interesting point! Probably remains killing people like nuclear waste!'}

tweet_dict['rts'] = 1
tweet_dict['likes'] = 0
tweet_dict['date'] = datetime.datetime(2019, 3, 24, 17, 47, 30)
tweet_dict['coordinates'] = [-73.856077, 40.848447]
tweet_dict['replies'] = 5
tweet_dict['followers'] = 300
'''
try:
	result = collection.insert_one(transcript_dict)
except pymongo.errors.InvalidDocument:
	n = {}
	for k,v in transcript_dict.items():
		if isinstance(k,str):
			for p in ['utf-8','iso-8859-1']:
				try:
					k = str(k)
				except (UnicodeEncodeError, UnicodeDecodeError):
					continue
		if isinstance(v,np.int64):
			v = int(v)
		if isinstance(v,str):
			for p in ['utf-8','iso-8859-1']:
				try:
					v = str(v)
				except(UnicodeDecodeError, UnicodeEncodeError):
					continue
		n[k] = v
	result = collection.insert_one(transcript_dict)

pprint('Insertion finished')