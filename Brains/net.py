# -*- coding: utf-8 -*-


# Personal Assistant Reliable Intelligent System
# By Tanguy De Bels


from Senses.mouth import speak
from Senses.ears import listen
from Utilities import vars

import os
import webbrowser
import urllib

def url(msg):
	message = listen()
	message = message.replace(" ", "")
	webbrowser.get(vars.chrome).open(u'http://www.' + message)

def fb(msg):
	webbrowser.get(vars.chrome).open(u'http://www.facebook.com')

def net_search(to_search):
	netSearch = urllib.quote_plus(to_search.encode(encoding='utf8', errors='replace'))
	webbrowser.get(vars.chrome).open(u'https://www.google.be/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=' + netSearch)

