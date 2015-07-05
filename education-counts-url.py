
# coding: utf-8

# In[60]:

import bs4
import requests
import dominate
from dominate.tags import *
import os
import shutil
import json
from urlparse import urlparse
from bs4 import BeautifulSoup


# In[61]:

#eceall = requests.get('')


# In[62]:

opind = open('/media/removable/WILLIAMS30G/www.educationcounts.govt.nz/index.html', 'r')


# In[63]:

optfz = opind.read()


# In[64]:

edcountz = bs4.BeautifulSoup(optfz)


# In[65]:

afind = edcountz.findAll('a')


# In[66]:

gidict = dict()


# In[67]:

for afi in afind:
    gied = afi.text
    gifz = gied.replace(' ', '-')
    giflow = gifz.lower()
    gidict.update({giflow[:12] : afi.attrs['href']})
    
    gihrd = urlparse(afi.attrs['href'])
    
    


# In[68]:

doc = dominate.document(title='educount')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with doc:
    #with div(id='header').add(ol()):
        #for i in ['home', 'about', 'contact']:
            #li(a(i.title(), href='/%s.html' % i))

    with div(cls='row'):
        h1('education-counts-url')
        for afi in afind:
            if 'https://' in afi.attrs['href']:
                gied = afi.text
                gifz = gied.replace(' ', '-')
                giflow = gifz.lower()
                a(dominate.tags.li(giflow[:12]), href = (afi.attrs['href']))
                #print afi.attrs['href']
            #p(edu.txt)
            #dominate.tags.p(edu.attrs['href'])
            #a(dominate.tags.p(edu.text), href=dominate.tags.a(edu.attrs['href']))
            
            #print edu.text

#print doc


# In[69]:

docre = doc.render()
#s = docre.decode('ascii', 'ignore')
yourstring = docre.encode('ascii', 'ignore').decode('ascii')
indfil = ('/media/removable/WILLIAMS30G/education-counts-url/index.json')
mkind = open(indfil, 'w')
mkind.write(yourstring)
mkind.close()


# In[70]:

dicon = json.dumps(gidict)


# In[71]:

opeducon = open('/media/removable/WILLIAMS30G/education-counts-url/index.json', 'w')

opeducon.write(dicon)

opeducon.close()


# In[72]:

rdeducon = open('/media/removable/WILLIAMS30G/education-counts-url/index.json', 'r')

rdqa = rdeducon.read()


# In[73]:

loadic = json.loads(rdqa)

