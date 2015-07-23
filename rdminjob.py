
# coding: utf-8

# In[21]:

import json
import bs4
#import github
#from github import Github
#import git
#import tweepy
#import random
import dominate
from dominate.tags import * 
#import pydnz


# <h3>Read Min Job</h3>
# 
# Python script to read the json file generated from minedujob.
# 
# The key 'lidocend' is good things to have for the job. It is a series of ['blahbhal'],

# In[4]:

opwse = open('/home/wcmckee/github/wcmckee.com/output/minedujobs/index.json', 'r')


# In[5]:

jsloaop = json.loads(opwse.read())


# In[6]:

lejsp = len(jsloaop)


# In[20]:

#rdjsop = 'ysgF_WqSpx1vofqAx7qG'


# In[23]:

#dnz = pydnz.Dnz(rdjsop)


# In[24]:

#dnz.search


# In[ ]:




# In[7]:

#ranlej = random.randint(0, lejsp)


# In[8]:

jsloaop


# In[9]:

#listed = list()


# In[10]:

#for jsran in range(lejsp):
    #print jsloaop.values()[jsran]['lidocend']
    #listed.append(jsloaop.values()[jsran]['lidocend'])


# In[11]:

#for lis in listed:
    #print lis
    #for li in lis:
        #print li
        #for wq in li:
            #print wq


# In[12]:

#for jsran in range(lejsp):
    #print jsloaop.values()[jsran]['Category']
    
    #for jsl in jsloaop.values()[jsran]['lidocend']:
        #print jsl
        #for jl in jsl:
            #print jl


# In[35]:

#print (jsloaop[0])


# In[39]:

#import random


# In[40]:

#randitez = random.randint(0,100)


# In[48]:

doc = dominate.document(title='Ministry of Education Jobs')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type ='text/javascript', src='script.js')
    #str(str2)
    
    with div():
        attr(cls='header')
        h1('Ministry of Education Jobs')
        p(img('logo.png', src='logo.png'))

        #p(img('imgs/getsdrawn-bw.png', src='imgs/getsdrawn-bw.png'))
        #p(img('imgs/15/01/02/ReptileLover82-reference.png', src= 'imgs/15/01/02/ReptileLover82-reference.png'))
        #h1('Updated ', strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        #p(panz)
        #p(bodycom)
    
    

with doc:
    with div(id='body'):
        for jsran in range(lejsp):
            h2(a((jsloaop.values()[jsran]['Job Title']), href=jsloaop.values()[jsran]['link']))
            #h3(jsloaop.values()[jsran]['Job Title'])
            h3(jsloaop.values()[jsran]['Category'])
            p(jsloaop.values()[jsran]['Job Type'])
            p(jsloaop.values()[jsran]['Date Advertised'])
            p(jsloaop.values()[jsran]['Job Reference'])
            p(jsloaop.values()[jsran]['Location'])
            
            #locdnz = dnz.search(jsloaop.values()[jsran]['Location'])
            #randitez = random.randint(0,5)
            #p(locdnz.records[0]['description'])
            #print locdnz.records
            #try:
            #    p(a('email', href= 'mailto:' + jsloaop.values()[jsran]['email']))
            #except NameError:
            #    skip
            #if 'email' in jsloaop.keys():
            #p(a('email', href= 'mailto:' + jsloaop.values()[jsran]['email']))
            #p(jsloaop.values()[jsran]['email'])

            for jsl in jsloaop.values()[jsran]['lidocend']:
        #print jsl
                for jl in jsl:
                    p(jl)
        #<a href="mailto:name@email.com">Link text</a>
        
        
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
        p('MinistryOfEducationJobs is open source')
        p(a('github - ece-display', href='https://github.com/wcmckee/ece-display'))
        p(a('wcmckee', href='http://wcmckee.com'))
        #a('https://github.com/wcmckee/ece-display')
        #a('http://wcmckee.com')

#print doc


# In[49]:

docre = doc.render()
#s = docre.decode('ascii', 'ignore')
yourstring = docre.encode('ascii', 'ignore').decode('ascii')
indfil = ('/home/wcmckee/github/wcmckee.com/output/minedujobs/index.html')
mkind = open(indfil, 'w')
mkind.write(yourstring)
mkind.close()


# In[41]:

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

