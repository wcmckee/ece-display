
# coding: utf-8

# In[51]:

import json
import bs4
#import github
#from github import Github
#import git
#import tweepy
#import random
import dominate
from dominate.tags import * 


# <h3>Read Min Job</h3>
# 
# Python script to read the json file generated from minedujob.
# 
# The key 'lidocend' is good things to have for the job. It is a series of ['blahbhal'],

# In[52]:

opwse = open('/home/wcmckee/minedujob/index.json', 'r')


# In[53]:

jsloaop = json.loads(opwse.read())


# In[54]:

lejsp = len(jsloaop)


# In[55]:

#ranlej = random.randint(0, lejsp)


# In[56]:

#jsloaop


# In[57]:

#listed = list()


# In[58]:

#for jsran in range(lejsp):
    #print jsloaop.values()[jsran]['lidocend']
    #listed.append(jsloaop.values()[jsran]['lidocend'])


# In[59]:

#for lis in listed:
    #print lis
    #for li in lis:
        #print li
        #for wq in li:
            #print wq


# In[60]:

#for jsran in range(lejsp):
    #print jsloaop.values()[jsran]['Category']
    
    #for jsl in jsloaop.values()[jsran]['lidocend']:
        #print jsl
        #for jl in jsl:
            #print jl


# In[61]:

#print (jsloaop[0])


# In[62]:

doc = dominate.document(title='Ministry of Education Jobs')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type ='text/javascript', src='script.js')
    #str(str2)
    
    with div():
        attr(cls='header')
        h1('Ministry of Education Jobs')
        #p(img('imgs/getsdrawn-bw.png', src='imgs/getsdrawn-bw.png'))
        #p(img('imgs/15/01/02/ReptileLover82-reference.png', src= 'imgs/15/01/02/ReptileLover82-reference.png'))
        #h1('Updated ', strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        #p(panz)
        #p(bodycom)
    
    

with doc:
    with div(id='body'):
        for jsran in range(lejsp):
            h3(jsloaop.values()[jsran]['Job Title'])
            p(jsloaop.values()[jsran]['Category'])
            p(jsloaop.values()[jsran]['Job Type'])
            for jsl in jsloaop.values()[jsran]['lidocend']:
        #print jsl
                for jl in jsl:
                    p(jl)
    
        
        
        #for rdz in reliz:
            #h1(rdz.title)
            #a(rdz.url)
            #p(img(rdz, src='%s' % rdz))
            #print rdz
            #p(img(rdz, src = rdz))
            #p(rdz)


                
            #print rdz.url
            #if '.jpg' in rdz.url:
            #    img(rdz.urlz)
            #else:
            #    a(rdz.urlz)
            #h1(str(rdz.author))
            
            #li(img(i.lower(), src='%s' % i))

    with div():
        attr(cls='body')
        p('GetsDrawn is open source')
        a('https://github.com/getsdrawn/getsdrawndotcom')
        a('https://reddit.com/r/redditgetsdrawn')

#print doc


# In[63]:

docre = doc.render()
#s = docre.decode('ascii', 'ignore')
yourstring = docre.encode('ascii', 'ignore').decode('ascii')
indfil = ('/home/wcmckee/minedujob/index.html')
mkind = open(indfil, 'w')
mkind.write(yourstring)
mkind.close()


# In[8]:

#noranch = jsloaop[0]


# In[20]:

#for les in range(0, lejsp):
    #print les
    #randa = jsloaop[str(les)]
    #print randa['title']
    
    #print randa['Category']
    #print randa['Location']
    
    #print randa['Date Advertised']
    #print randa['time-advertised']

