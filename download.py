# Include Libarires
# from pytube import YouTube
import pafy
import sys
import re
import os
import helpers


def downloadSong(link):
    try:
        yt = pafy.new(link)
        print("Downloading: " + yt.title)
        yt.getbestaudio().download(filepath='video', quiet=False)
        ext = yt.getbestaudio().extension
        helpers.convertVideo(yt.title, ext)
        print("Done!\n")
    except OSError:
        print('Video not found!')


def figure(input):
    if 'www.youtube.com/' in input:
        # Determine if playlist or video
        if 'playlist' in input:
            # playlist
            helpers.PlaylistSort(input)

        else:
            # not playlist
            downloadSong(input)

    else:
        with open(input, 'r') as file:
            for item in file:
                figure(item)


if len(sys.argv) < 2:
    print("You need to provide a link or file")
    exit()

else:
    
    if os.path.exists('./misc') == False:
        os.mkdir('./misc')
        
    if os.path.exists('./audio') == False:
        os.mkdir('./audio')

    if os.path.exists('./video') == False:
        os.mkdir('./video')

    try:
        figure(sys.argv[1])
    except KeyboardInterrupt:
        print('\nUser Aborted Operation')
    
    print('Cleaning Up...')
    #Begin Cleanup Process