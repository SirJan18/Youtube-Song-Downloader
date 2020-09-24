import pafy
import sys
import os
import metadata.metadata as meta
import logging
from pydub import AudioSegment



def checkName(check):
    check = str(check)
    chars = ['/', '\\', ':', '?', '"', '<', '>', '|']
    for item in chars:
        check = check.replace(item, '_')
    return check



def convertVideos(input, folder, ext):
    #Check Name Remove any quotes, replace with /'
    try:
        name = checkName(input)
        print(f"Converting: {input}.{ext}")
        raw = AudioSegment.from_file(f'./video/{name}.{ext}')
        raw.export(f'./audio/{folder}/{name}.mp3', 'mp3')
        os.remove(f'./video/{name}.{ext}')
        #add metadata
        print("Writing metadata...")
        meta.writeMeta(input)
  
    except OSError as e:

        print("Error converting file. Check the Logs")
        logging.log(logging.INFO, "Converting: " + str(e))

def convertVideo(input, ext):
    #Check Name Remove any quotes, replace with /'
    try:  
        name = checkName(input)
        print(f'Converting: {name}.{ext}')
        raw = AudioSegment.from_file(f'./video/{input}.{ext}', ext)
        raw.export(f'./audio/{name}.mp3', 'mp3')
        os.remove('./video/'+name+'.mp4')
        #add metadata 
        print("Writing metadata...")
        meta.writeMeta(input)
    except OSError as e:

        print("Error converting file. Check the Logs")
        logging.log(logging.INFO, "Converting: " + str(e))


def PlaylistSort(link):
    #get videos from playlist
    playlist = pafy.get_playlist(link)
    #print(playlist['items'][1]['pafy'].getbest())\
    title = checkName(playlist['title'])
    print("Downloading " + title)
    if os.path.exists(f'./audio/{title}') == False:
        os.mkdir(f'./audio/{title}')
    print(str(len(playlist['items'])) + " Songs\n")
    for video in range(0, len(playlist['items'])):
        print(str(video+1) + " of " + str(len(playlist['items'])))
        print(playlist['items'][video]['pafy'].title)
        playlist['items'][video]['pafy'].getbestaudio().download(filepath='video', quiet=False)
        extension =  playlist['items'][video]['pafy'].getbestaudio().extension
        name = checkName(playlist['items'][video]['pafy'].title)
        
        try:
            convertVideos(name, title, extension)
        except OSError as e:
            print(f'There was an error downloading the song\n{e}')
        print("Done!\n")

#PlaylistSort(sys.argv[1])
logging.basicConfig(filename='./misc/log.log', level=logging.INFO)
