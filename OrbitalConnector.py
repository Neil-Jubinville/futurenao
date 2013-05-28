import os
import sys
import time
from naoqi import ALProxy
from speak import say
from vision import store
import json
import urllib2
import requests
import datetime

# Author Neil Jubinville


    
class OrbitalConnector:
	#make a http connection to the NAO data cloud 
	
	
	def __init__(self,u,p,s):
	    self.username=u;
	    self.password = p;
	    self.server = s;
	    self.authToken ="";
	    self.storageToken="";
	    self.storageUrl = "";
	    self.authenticated = "false";
	
	
	def connectAuth(self):
		print "Connecting to server:" +self.server + " using creds ( username:" +self.username+" , password:" +self.password+")";
		headers = {'X-Auth-User': self.username , 'X-Auth-Key': self.password }		
		res = requests.get(self.server ,headers=headers)
		print res.json;
		print res.headers;		
		
		if( res.status_code == requests.codes.ok):
		  say("I am successfully authenticated for cloud storage");
		  self.authenticated="true";
			  
		else:
		  say("I am unable to connect to the cloud storage.  I got a response code of " + str(res.status_code)); 
		
		#set the local headers
		self.authToken=res.headers["x-auth-token"];
		self.storageToken=res.headers["x-storage-token"];
		self.storageUrl=res.headers["x-storage-url"];
        
		if(self.authenticated):
		  say("Now that I am connected I will attempt to take and upload a picture.");
		
		
		#try to take the picture
		
		filename = 'image' + datetime.datetime.now().strftime("_%B_%d_%Y_%I%M%p");
		filetype ='jpg';
		store(filename,filetype);
		
		fullname = filename+'.'+filetype;
		
		myfile = open("/orbital/media/"+fullname,"rb");  
		data = myfile.read();
		#now prepare to upload it to the cloud.
		urlPath = self.storageUrl +'/media/pictures/'+fullname
		#headers = {'X-Auth-Token': self.authToken,  'X-Storage-Url': (self.storageUrl +'/media/pictures/myfile.jpg') ,'Content-Length': str(os.path.getsize('/orbital/media/image.jpg')) }	
		headers = {'X-Auth-Token': self.authToken }	
		
		
		res2 = requests.put(urlPath, data=data ,headers=headers);
		print res2.text;
		print res2.headers;
		say("OK I tried to upload.");
        
        
def main(args):
	myobj = OrbitalConnector("usernamehere","passwordhere","https://aquarius.orbitalsoftware.ca/auth/v1.0");
	print myobj.connectAuth();

if __name__ == '__main__':
    main(sys.argv)