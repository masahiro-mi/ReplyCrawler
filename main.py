#-*- encoding: utf-8 -*-

from twitter import *
import os,sys,time

#NG words
check_chara = ('http', '#', '\\', '【','】')

#Retry MAX
retry_max = 10
#Retry time
retry_time = 10

CONSUMER_NAME = 'YOUR APPLICATION NAME'
CONSUMER_KEY =  'YOUR CONSUMER KEY'
CONSUMER_SECRET = 'YOUR CONSUMER SECRET'

TWITTER_CREDS = os.path.expanduser('.credentials')
if not os.path.exists(TWITTER_CREDS):
  oauth_dance(CONSUMER_NAME, CONSUMER_KEY, CONSUMER_SECRET, TWITTER_CREDS)
oauth_token, oauth_secret = read_token_file(TWITTER_CREDS)

# token
stream = TwitterStream(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))
twitter = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

def show(_status):
  #print('IN:\n'+str(_status), file=sys.stderr)
  for r in range(retry_max):
    if 'lang' in _status and _status['lang'] == 'ja' and 'in_reply_to_status_id' in _status and not _status['in_reply_to_status_id'] is None and 'text' in _status and check(_status['text']):
      try:
        status=twitter.statuses.show(id=_status['in_reply_to_status_id'])
      except:
        #print('! Error\tRetry to read in_reply_tweet - '+str(r), file=sys.stderr)
        time.sleep(retry_time)
        continue
      #print('OUT:\n'+str(status), file=sys.stderr)
      if 'lang' in _status and _status['lang'] == 'ja' and 'text' in status and check(status['text']):
        print(str(status['id'])+'\t'+trim(status['text'])+'\t'+str(_status['id'])+'\t'+trim(_status['text']))
        if 'in_reply_to_status_id' in status and not status['in_reply_to_status_id'] is None:
          show(status)
        break
      else:
        #print('! Info\tin_reply_tweet is not acceptable', file=sys.stderr)
        break
    else:
      break

def trim(text):
  return text.replace('\r','-br-').replace('\n','-br-')

def check(text):
  for char in check_chara:
    if char in text:
      return False
  return True

def main():
  while 1:
    statuses = stream.statuses.sample()
    for status in statuses:
      show(status)

if __name__ == '__main__':
 main()
