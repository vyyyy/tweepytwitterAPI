# tweepytwitterAPI

Use the tweepy API to stream tweets for a given filter.   

After cloning this repo, cd into the directory ($ cd tweepytwitterAPI) where the python script is contained.

Run this script at the commandline via the Terminal app on a Mac.  
For example, $ ./tweepytwitterAPI.py 'python tutorial'.  

If needed, to setup file permission on OSX/Linux:   
  1. $ cd ~  
  2. $ chmod +x tweepytwitterAPI.py
  
The expected output should be a stream of incoming live tweets containing 'python tutorial'.   

Dependency: tweepy API, http://docs.tweepy.org/en/v3.5.0/getting_started.html  
You'll also need your own keys for Twitter API authentication.   
