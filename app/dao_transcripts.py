import pymongo
from pprint import pprint
import pandas as pd
import numpy as np
import datetime
import app.mongo.Transcript


def insert_transcript(transcript, connection):
	client = pymongo.MongoClient(connection)
	db = client.taotai
	collection = db['Transcript']

	transcript_dict = transcript.to_dict()

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

def insert_transcripts(transcripts,connection):
	client = pymongo.MongoClient(connection)
	db = client.taotai
	collection = db['Transcript']

	for x in transcripts:
		transcript_dict = x.to_dict
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

def query_transcript(query,connection):
	#Queries must have the following format:
	#Query = {key1: value1,key2: value2...}
	client = pymongo.MongoClient(connection)
	db = client.taotai
	collection = db['Transcript']

	try:
		doc = collection.find(query)
	except:
		pprint('Error: No data was retrieved')

	return doc

def query_random_transcript(connection):
	client = pymongo.MongoClient(connection)
	db = client.taotai
	collection = db['Transcript']

	try:
		doc = collection.find_one()
	except:
		pprint('Error: No data was retrieved')

	return doc

def delete_one_transcript(query,connection):
	client = pymongo.MongoClient(connection)
	db = client.taotai
	collection = db['Transcript']

	try:
		doc = collection.delete_one(query)
	except:
		pprint('Error: Not possible to delete document')

def delete_many_transcripts(query,connection):
	#To delete all documents from the collection just input an empty query( {} )
	client = pymongo.MongoClient(connection)
	db = client.taotai
	collection = db['Transcript']

	try:
		doc = collection.delete_many(query)
	except:
		pprint('Error: Not possible to delete document')

	pprint('All transcripts were deleted')

def update_one_transcript(query,newvalues,connection):
	#Queries and newvalues must be a dictionary
	client = pymongo.MongoClient(connection)
	db = client.taotai
	collection = db['Transcript']

	try:
		result = collection.udpate_one(query,newvalues)
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
		result = collection.udpate_one(query,newvalues)

def update_one_transcript(query,newvalues,connection):
	#Queries and newvalues must be a dictionary
	client = pymongo.MongoClient(connection)
	db = client.taotai
	collection = db['Transcript']

	try:
		result = collection.udpate_many(query,newvalues)
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
		result = collection.udpate_many(query,newvalues)


