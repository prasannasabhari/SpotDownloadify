import csv
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from pathlib import Path
import yt_dlp as youtube_dl
import requests
import pandas as pd
import os
from youtubesearchpython import VideosSearch

def search_for_url_vids(name_songs):
    videosSearch = VideosSearch(name_songs, limit = 1)
    result = videosSearch.result()
    link = result["result"][0]["link"]
    print(link)
    return link

def run(link):
    video_url = link
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    SAVE_PATH = str(os.path.join(Path.home(), "Downloads/songs"))
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':"{}/{}".format(SAVE_PATH,filename), 
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    print(filename)
    print("Download complete... {}".format(filename))

def __main__():
	data = pd.read_csv(r'songs.csv')
	songs = data['song names'].tolist()
	print("Found ", len(songs), " songs!")
	for song in songs:
		print(song)
		run(search_for_url_vids(song))

__main__()