#! /usr/bin/env python

import naoqi
import time
import sys
from naoqi import ALProxy

def say(text):
                tts = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)
                tts.say(text)

def stream(source):
		aup = ALProxy("ALAudioPlayer", "127.0.0.1", 9559)
		fileId = aup.post.playWebStream(source,.8,0.0)
