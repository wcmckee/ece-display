
# coding: utf-8

# parseduxml 
# 
# script to parse rss xml feed from http://www.education.govt.nz/
# 
# Had problems parsing the html so i decided to add a try and pass if exception. It fixes it but does this mean it's going to save less data?
# 
# Saving it as json. I'll make another script to build the nikola site from the json object it creates. 
# 
# Missing author. Why not just make moe the author?
# 
# No post tags. Would be nice to tag things. eg: schools, subject matter, areas etc.

# In[ ]:




# In[41]:

import requests
import xmltodict
import json


# In[22]:

reqedu = requests.get('http://www.education.govt.nz/rss.xml')


# In[23]:

diedu = xmltodict.parse(reqedu.text)


# In[24]:

ledi = len(diedu['rss']['channel']['item'])


# In[33]:

nodict = dict()


# Remove all - in title. Change space to - Why is this only working on the last element.

# In[26]:

nospap= list()


# In[27]:

siteloc = '/home/wcmckee/minrss/posts/'


# In[39]:

for isz in range(0, ledi):
    try:
        postdict = dict()
        #diet = (diedu['rss']['channel']['item'][isz]['title'])
        repsi = (diedu['rss']['channel']['item'][isz]['title'].replace('–', ''))
        
        nospac = repsi.replace(' ', '-')
        postdict.update({'title' : repsi})
        
        #oprst = open(siteloc + diet + '.rst', 'w')
        #oprst.write(diet)
        deitz = (diedu['rss']['channel']['item'][isz]['description'])
        postdict.update({'description' : deitz})
        pubd = (diedu['rss']['channel']['item'][isz]['pubDate'])
        links = (diedu['rss']['channel']['item'][isz]['link'])
        postdict.update({'publish' : pubd, 'link' : links})
    
        
        pocopy = postdict.copy()
        
        nodict.update({isz : pocopy})
        #opmets = open(siteloc + deitz + '.meta', 'w')
        #opmets.write()
        #print(deitz)
        #oprst.close()
        #opmets

    except Exception:
        pass


# In[46]:

jsdic = json.dumps(nodict)


# In[48]:

wrimd = open('/home/wcmckee/minrss/moenews.json', 'w')


# In[49]:

wrimd.write(jsdic)


# In[50]:

wrimd.close()

