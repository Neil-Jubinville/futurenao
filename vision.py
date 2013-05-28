import os
import sys
import time
from naoqi import ALProxy




def store(filename,imagetype):	
	 
  try:
	photoCaptureProxy = ALProxy("ALPhotoCapture", "127.0.0.1", 9559)
	photoCaptureProxy.setResolution(2)
	photoCaptureProxy.setPictureFormat(imagetype)  #jpg png etc..
	photoCaptureProxy.takePictures(1,"/orbital/media/", filename)

  except Exception, e:

  	print " *** Error: vision.py ,  when creating ALPhotoCapture proxy:"
  	print str(e)
  	


def main(args):
    print args
    store("testimage");

if __name__ == '__main__':
    main(sys.argv)