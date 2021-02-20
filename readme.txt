API RateLimiter
=================

How to use it:

	Go to the mock server(http://127.0.0.1:8000/) on your browser
	Resigter a User(dev/org) to generate a token
	To simulate the API request/response process 
		 -On PostMan's headers panel set key to Authorization
		 -Insert the generated token separated by a space such as'Token b8sioahf934902h09244u0'
		 -Press Send for your JSON response to be displayed.
	Login to the adminpanel to alter the ratelimit for an API+User combination,if non-default values are desired.
		 User: Team10
		 Password : BLUEOPTIMA
	

Features
--------
	Server side rate-limiting solution



Installation
------------
	 For linux OS(Ubuntu 18.04.2 LTS):
	 Unzip the provided archive to your prefered location
	 Steps to configure running environment
		 - On your terminal run
			 $ cd (File_Location)/
			 $ python3 -m venv any_name
			 $ source any_name/bin/activate
			 (any_name)$ pip3 install -r requirements.txt
			 (any_name)$ python3 manage.py migrate
			 (any_name)$ python3 manage.py runserver

	 For MAC OS(Mojave):
	 Unzip the provided archive to your prefered location
	 Steps to configure running environment
		 - On your terminal run
			 $ cd (File_Location)/ 
			 $ sudo pip install virtualenv
			 $ virtualenv any_name 
			 $ cd any_name/
			 $ source bin/activate
			 (any_name)$ cd ..
			 (any_name)$ pip3 install -r requirements.txt
			 (any_name)$ python3 manage.py migrate
			 (any_name)$ python3 manage.py runserver


Dependencies
------------
	python3, postman, pip3 , pip, virtualenv along with listings in requirements.txt
	Download Postman from https://www.getpostman.com/downloads/
