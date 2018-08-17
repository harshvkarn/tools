import urllib2
import argparse
import os
import time
import re
from slackclient import SlackClient

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='URL of site to check', required=True)
args = parser.parse_args()

#Notify: That call slack's API
def notify(status):
	msg = "UUurrrggghh! \n "+ args.url + " is in *trouble*! :cry: \n :warning: *Error:* :warning: \n " + "`" + str(status) + "`" 
	sc.api_call(
	  "chat.postMessage",
	  channel="#health-status",
	  text=msg,
	  username="NetBee",
	  icon_url="http://www.pngmart.com/files/1/Cartoon-Bee-PNG.png"
	)

# status = 200
while True:
	try:
		status = urllib2.urlopen(args.url).getcode()
		if status != 200:
			notify(status)
		time.sleep(10)
	except Exception as e:
		print ("Error",e)
		notify(e)
		time.sleep(10)

