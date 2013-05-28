futurenao
=========

client side tools for robot cloud services

OK so this code is for CLI mode right now, we will have to port it to choreagraph.

To install, simply SSH to your nao,  

mkdir /orbital            (This is the base folder for the python cloud files) <br>
mkdir /orbital/images     (this you need if you want to run the demo)

then you need to get this code into the orbital folder.   I haven't installed git on NAO yet so from your favorite place
download the code from github here git clone .......  

then transfer it to /oorbital

edit the OrbitalConnector.py and change the username and password to your account info 

then run it!

python OrbitalConnector.py  it should then take a picture and upload it to the cloud.

*Note that you will need a cloud storage account so contact me for one.  You must be part of the Aldebaran developer program
or actively involved in research or development with NAO or ROMEO to get an account.

more updates soming soon.

Neil



