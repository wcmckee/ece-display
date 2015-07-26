
# coding: utf-8

# Library Education Govt 
# 
# Script to deal with rss xml feed of library.education.govt.nz

# In[25]:

import requests
import json
import xmltodict
import bs4


# In[2]:

reqlib = requests.get('https://library.education.govt.nz/rss/highlights')


# In[3]:

reqlibt = reqlib.text


# In[4]:

libtd = xmltodict.parse(reqlibt)


# In[5]:

rslen = len(libtd['rss']['channel']['item'])


# In[6]:

#rslen


# In[7]:

wrapdict = dict()


# In[19]:

#print (libtd['rss']['channel']['item'][0])


# In[30]:

for libi in range(rslen):
    msjobdic = dict()

    #print (libtd['rss']['channel']['item'][libi]['title'])
    msjobdic.update({'title' : (libtd['rss']['channel']['item'][libi]['title'])})
    msjobdic.update({'link' : (libtd['rss']['channel']['item'][libi]['link'])})
    soupdes = bs4.BeautifulSoup(libtd['rss']['channel']['item'][libi]['description'])
    
    msjobdic.update({'description' : soupdes.text})
    msjobdic.update({'jsonlen' : libi})
    #findict = dict()
    
    #wrapdict.update({'title' : (libtd['rss']['channel']['item'][libi]['title'])})
    #totlen = len(libi)
    #for tes in range(totlen):
    #    wrapdict.update({'title' : txtspli[tes][1]})
    #findict.update({txtspli[0][0] : txtspli[0][1]})
    msjobz = msjobdic.copy()
    msjobz.update(msjobdic)
    
    wrapdict.update({libi : msjobz})
    #jsmsdob = json.dumps(wrapdict)
    
    
    #jslibi.update({rslen : msjobz})
    #jsmsdob = json.dumps(wrapdict)


# In[32]:

savjslib = json.dumps(wrapdict)


# In[35]:

savjfin = open('/home/wcmckee/github/wcmckee.com/output/moelib/index.json', 'w')
savjfin.write(savjslib)
savjfin.close()


# In[ ]:



