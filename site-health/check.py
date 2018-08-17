# Copyright 2018 Harshvardhan Karn <harshvkarn54@gmail.com>

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License

import urllib2
import argparse
import os
import time
import re
import multiprocessing
from slackclient import SlackClient

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='URL of site to check', required=True)
parser.add_argument('-c', '--channel', help='Channel to post', required=True)
args = parser.parse_args()
channelName = '#'+args.channel
print channelName
#Notify: That call slack's API
def notify(status):
	msg = "<!channel>  \n UUurrrggghh! \n "+ args.url + " is in *trouble*! :cry: \n :warning: *Error:* :warning: \n " + "`" + str(status) + "`" 
	sc.api_call(
	  "chat.postMessage",
	  channel=channelName,
	  text=msg,
	  username="NetBee",
	  icon_url="http://www.pngmart.com/files/1/Cartoon-Bee-PNG.png"
	)

def mAlive():
	msg = "I am fine! Don't Worry! :relaxed:"
	sc.api_call(
	  "chat.postMessage",
	  channel=channelName,
	  text=msg,
	  username="NetBee-Status",
	  as_user="False",
	  icon_url="http://www.pngmart.com/files/1/Cartoon-Bee-PNG.png"
	)
def mainFunc():
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

if __name__ == '__main__':
	p = multiprocessing.Process(target=mainFunc, name="main")
	p.start()
	while True:
		mAlive()
		time.sleep(3600)