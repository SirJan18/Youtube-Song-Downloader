import os
import eyed3
import sys
import time
import helpers
import logging


# TODO: Write Metadata

def writeName(name, title):
    try:
        file = eyed3.load('./audio/' + name + ".mp3")
        file.tag.title = title
        file.tag.save()

    except OSError as e:
        #print("There was a problem while writing metadata. Check the logs")
        logging.log(logging.INFO, "Name Error: " + str(e))


def writeArtist(name, artist):
    try:
        file = eyed3.load('./audio/' + name + ".mp3")
        file.tag.artist = artist
        file.tag.save()

    except OSError as e:
        #print("There was a problem while writing metadata. Check the logs")
        logging.log(logging.INFO, "Artist Error: " + str(e))


def writeAlbum(name, album):
    try:
        file = eyed3.load('./audio/' + name + ".mp3")
        file.tag.album = album
        file.tag.save()

    except OSError as e:
        #print("There was a problem while writing metadata. Check the logs")
        logging.log(logging.INFO, "Album Error: " + str(e))


def writeMeta(name):
    try:
        if name.index(" - ") != ValueError:
            broken = name.split(' - ')
            writeArtist(name, broken[0])
            writeName(name, broken[1])
            # TODO: Search metadata-db

        else:
            writeName(name, name)

    except ValueError as e:
        #print("There was a problem writing data")
        logging.log(logging.INFO, "Album Error: " + str(e))


logging.basicConfig(filename='./misc/log.log', level=logging.INFO)
eyed3.log.setLevel("ERROR")
#writeMeta(sys.argv[1])
