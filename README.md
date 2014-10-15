Reply Crawler
====

Crawl Program for Reply Tweets


Features
----
Python 3+ with some standard imports.

Using:
* https://github.com/sixohsix/twitter


Specifications
----
This crawler picks up reply pair from Twitter.
However, targets are only LANG='ja', and without URL, Hashtag, some em parentheses.

The reply pair acquires only that correspondence of 'in_reply_to_status_id' is clear.

Run
----
Palease regist your application to get CONSUMER KEY, CONSUMER SECRET
* https://dev.twitter.com/apps
You have change 'CONSUMER NAME', 'CONSUMER KEY', and 'CONSUMER SECRET' in main.py

  $ ./main.py

First, you have to access to the twitter login page.
