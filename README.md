# CITS3403-Project: Soccer Polls
##### ## By Hasitha (21146645) and Samuel (22539107)

## Web Application Purpose

The context that we have based our web application on is Soccer Polls, and the polls on our site can consist of any topic related to Soccer players. We expect users who love Soccer and love debating about different Soccer topics to use our web application. Example polls could include:

1. Who do you think the best soccer player in the world is?
2. Who do you think the best soccer player of all time is?

Users can then vote for the player that they think is the best (with respect to the question they are answering above). Therefore, the social choice mechanism that we have used is very simple. A user wishing to vote on a poll can either select a predefined (by the poll creator) or previously used entry/answer or add a new entry to the poll when no more than eight entries already exist. This means that a user votes for one and only one entry/answer. 

## Setup

1. Install python
2. Install the following python packages:

	- pip install flask
	- pip install python-dotenv
	- pip install  flask-wtf
	- pip install  flask-sqlalchemy
	- pip install flask-migrate
	- pip install  flask-login

3. In terminal `set FLASK_APP=project.py` or for Mac `export FLASK_APP=project.py`

4. To prepopulate database run `python prepop.py`

5. `flask run` to run the website locally

6. Navigate to localhost:5000 or 127.0.0.1:5000

## Logins

A few users logins have been created for convenience

##### Admins

username:`Hasi` pw:`Hasitest1`
username:`Sam` pw:`Samtest1`
username:`Tim` pw:`Timtest1`

##### Users

username:`Tom` pw:`Tomtest1`
username:`Michael` pw:`Michaeltest1`
