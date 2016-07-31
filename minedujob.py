
# coding: utf-8

# <h3>minedujob</h3>
# 
# Python script to fetch jobs from Ministry Of Education and convert it into a json object. Fix format problems around the xml.  
# 
# 

# In[ ]:




# TODO
# 
# done - Parse description tag for the keys and values hidden within that. 
# done - Extract email from description, if email look up persons phone number and attach it.
# 
# Location - look on digitalnz for cc by images. Search location and aerial photos of the area that could be used in the job ad.
# title - 
# 
# scrape url.
# 
# done - cycle over all job listings and create json object with them all instead of just a random choice.
# 
# Short the url
# 
# Fix arrow to convert to the time given rather than time now.
# 
# Merge data in from DigitalNZ.
# 
# What other apis could i merge in?
# 
# Fix the li that doesn't get included in description text (p) and make sure it is included.
# 
# 

# In[1]:

import requests
#import untangle
import xmltodict
import json
#import random
import bs4
import os
#import dominate
#from dominate.tags import *
#from pydnz import Dnz
#import arrow
#import bs4
#import pyshorteners
#import tweepy
import getpass


# In[2]:

myusr = getpass.getuser()


# In[3]:

#dnz = Dnz('keyhere')


# In[4]:

jobreq = requests.get('https://jobs.govt.nz/jobtools/job_rss?o1=16563&k2=7E204B6518FF9F28&source=JobRSS&medium=JobRSS', verify=False)


# In[5]:

#jobreq = requests.get('https://jobs.minedu.govt.nz/jobtools/job_rss?o1=17584&k2=A52B3674BC046465&source=JobRSS&medium=JobRSS', verify=False)


# In[6]:

jobtxta = jobreq.text


# In[7]:

#obj = untangle.parse(jobtxta)


# In[8]:

jobtxta


# In[ ]:




# In[9]:

#obj


# In[10]:

dicjobz = xmltodict.parse(jobtxta)


# In[11]:

ranldicj = len(dicjobz['rss']['channel']['item'])


# In[12]:

#ranldicj


# In[13]:

#randicz = random.randint(0, ranldicj)


# In[14]:

#randicz


# In[15]:

wrapdict = dict()


# In[16]:

moejdir = ('/home/{}/moejobs/'.format(myusr))


# In[17]:

moejdir


# In[ ]:




# In[18]:

def ospacheck():
    if os.path.isdir(moejdir) == True:
        print ('its true')
    else:
        print ('its false')
        os.mkdir(moejdir)


# In[19]:

ospacheck()


# In[21]:

#dicrtq


# In[23]:

bfina


# In[25]:

dicrs


# In[ ]:




# In[22]:

for dic in range(ranldicj):
    dicrs = dicjobz['rss']['channel']['item'][dic]
    dicrts = dicrs['title']
    dicrtq = dicrs
    #artim = arrow.now(dicrtq['pubDate'])
    #jobclose = artim.replace(weeks=+2)
    #jclodat = jobclose.date()
    msjobdic = dict()
    #msjobdic.update({#'date-advertised' : str(artim.date()), 
                #'time-advertised' : str(artim.time()),
                #'title' : dicrts,
                #'date-closed' : str(jclodat)})
    requlink = dicrtq['link']
    reqlinkq = requests.get(requlink)
    bsoup = bs4.BeautifulSoup(reqlinkq.text)
    bfina = bsoup.findAll('a')
    
    for bfin in bfina:
        if ('@') in bfin.text:
            #print bfin.text
            msjobdic.update({('email') : str(bfin.text)})
            
    for bfin in bfina:
        if ('href') in bfin.text:
            #print bfin.text
            msjobdic.update({('href') : str(bfin.text)})
    for bfiny in bfina:
        if '.docx' in bfiny.text:
            msjobdic.update({'doc' : bfiny.text})
    msjobdic.update({'link' : dicrtq['link']})
    msjobdic.update({'jsonlen' : (str(dic))})
    bsdescr = bs4.BeautifulSoup(dicrtq['description'])
    txtspli = [line.text.split(": ") for line in bsdescr.findAll('li')[0:8]]
    docitems = [line.text.split(": ") for line in bsdescr.findAll('li')[9:]]
    findict = dict()
    findict.update({'lidocend' : docitems})
    totlen = len(txtspli)
    for tes in range(totlen):
        findict.update({txtspli[tes][0] : txtspli[tes][1]})
    findict.update({txtspli[0][0] : txtspli[0][1]})
    msjobz = findict.copy()
    msjobz.update(msjobdic)
    
    wrapdict.update({dic : msjobz})
    jsmsdob = json.dumps(wrapdict)
    #opeind = open('/home/wcmckee/minedujob/' + str(dic) + '.json', 'w')
    with open('/home/{}/moejobs/index.json'.format(myusr), 'w') as moejsn:
        moejsn.write(jsmsdob)
    #opind = open('/home/{}/moejobs/index.json'.format(myusr), 'w')
    #opind.write(jsmsdob)
    #api.update_status(dicrts)
    #opeind.close()
    
    


# In[ ]:

#opind.close()


# In[ ]:




# In[ ]:

#opeind.close()


# In[ ]:

#dicrs = dicjobz['rss']['channel']['item'][0]


# In[ ]:

#dicrts = dicrs['title']
#dicrtq = dicrs


# In[ ]:

#artim = arrow.now(dicrtq['pubDate'])


# In[ ]:

#jobclose = artim.replace(weeks=+2)


# In[ ]:

#jclodat = jobclose.date()


# In[ ]:




# In[ ]:

#msjobdic = dict()


# In[ ]:

#msjobdic.update({'date-advertised' : str(artim.date()), 
#                'time-advertised' : str(artim.time()),
#                'title' : dicrts,
#                'date-closed' : str(jclodat)})


# In[ ]:

#msjobdic


# In[ ]:

#requlink = dicrtq['link']


# In[ ]:

#reqlinkq = requests.get(requlink)


# In[ ]:

#bsoup = bs4.BeautifulSoup(reqlinkq.text)


# In[ ]:

#bfina = bsoup.findAll('a')


# In[ ]:

#msjobdic.update({'date advertised' : str(artim.date()), 
#                'time advertised' : str(artim.time()),
#                'title' : dicrts,
#                '})
#for bfin in bfina:
#    if ('@') in bfin.text:
#        #print bfin.text
#        msjobdic.update({('email') : str(bfin.text)})
        


# In[ ]:

#for bfiny in bfina:
#    if '.docx' in bfiny.text:
#        print bfiny.text


# In[ ]:

#Search for this file and render text.
#if jpg/gif render.


# In[ ]:

#for bfin in bfina:
#    if ('href') in bfin.text:
        #print bfin.text
#        msjobdic.update({('href') : str(bfin.text)})


# In[ ]:

#msjob


# In[ ]:

#msjobdic.update({'randnum' : randicz})


# In[ ]:

#for bfiny in bfina:
#    if '.docx' in bfiny.text:
#        msjobdic.update({'doc' : bfiny.text})


# In[ ]:

#msjobdic


# In[ ]:

#msjobdic.update({'link' : dicrtq['link']})


# In[ ]:

#msjobdic


# In[ ]:

#msjobdic.update({'doc' : b


# In[ ]:

#bsdescr = bs4.BeautifulSoup(dicrtq['description'])


# In[ ]:

#for iza in bsdescr.findAll('li')[0:8]:
#    print iza


# In[ ]:

#lili = list()


# In[ ]:

#txtspli = [line.text.split(": ") for line in bsdescr.findAll('li')[0:8]]


# In[ ]:

#findict = dict()


# In[ ]:

#totlen = len(txtspli)


# In[ ]:

#for tes in range(totlen):
#    findict.update({txtspli[tes][0] : txtspli[tes][1]})
    


# In[ ]:

#findict.update({txtspli[0][0] : txtspli[0][1]})


# In[ ]:

#msjobz = findict.copy()
#msjobz.update(msjobdic)


# In[ ]:

#for bsdz in bsdescr.findAll('li'):
#    (k,v) = bsdz.text.split(": ")
#    print bsdz.text
#    print(k,v)
#    lili.append(bsdz.text)


# In[ ]:

#txtlis = list()


# In[ ]:




# In[ ]:

#bsp = bsdescr.findAll('p')


# In[ ]:

#for bs in bsp:
    #print bs.text
    #txtlis.append(bs.text)
    #numchc = [int(s) for s in bs.text.split() if s.isdigit()]
    #It's skipping items in the li since thats not a p :( 
    #There are other details in the description that I 
    #would like to extract - like closing date. 
    #Why not for closing date just take the date it was 
    #advertised and + 2 weeks?
    


# In[ ]:

#dicrts


# In[ ]:

#debsnz =  dnz.search(dicrs)


# In[ ]:

#randrecord = len(debsnz.records)


# In[ ]:

#ranitdz = random.randint(0, randrecord)


# In[ ]:

#ranitdz


# In[ ]:

#randicz


# In[ ]:

#debsnz.records


# In[ ]:

#debrecintz = debsnz.records[ranitdz]


# In[ ]:

#kederz = debrecintz.keys()


# In[ ]:

#print debrecintz['category']
#print debrecintz['usage']


# In[ ]:

#for ked in kederz:
#    print ked
#    print debrecintz[ked]
    #print ked
    #print ked
    #print debrecintz['category']


# In[ ]:

#print debrecintz['id']


# In[ ]:

#getiddnz = ('http://api.digitalnz.org/v3/records/' + str(debrecintz['id']) + '.json?api_key=Ph2LDuyiJmJcQm1S5myy')


# In[ ]:

#getiddnz


# In[ ]:

#reqidnz = requests.get(getiddnz)


# In[ ]:

#json.dumps(reqidnz)


# In[ ]:

#mylirq = list()


# In[ ]:

#for reqi in reqidnz:
    #print reqi
    #print reqi.upper()
    #reqi


# In[ ]:

#my_dict.pop("key", None)


# In[ ]:

#dicrq = len(dicjobz['rss']['channel']['item'])


# In[ ]:

#dicrq


# In[ ]:

#Return a random job.


# In[ ]:

#ranjoz = random.randint(0, dicrq)

#dicrsch = dicjobz['rss']['channel']['item']


# In[ ]:

#print dicrsch[ranjoz]['link']


# In[ ]:

#print dicrsch[ranjoz]['title']


# In[ ]:

#jobtype
#location
#date advertised
#jobreference
#jobtitle
#should be keys
#Currently they are inside description key
#Create new json file that fixes this.


# In[ ]:

#for dezsr in  dicrsch[ranjoz]['description']:
##    if 'JobType' in dezs#r:
# #       print dezsr


# In[ ]:

#docstart.title = ('ministry-of-education-jobs')
#doc = dominate.document(title='ministry-of-education-jobs')

#with doc.head:
#    link(rel='stylesheet', href='style.css')
#    script(type='text/javascript', src='script.js')

#with doc:
    #with div(id='header').add(ol()):
        #for i in ['home', 'about', 'contact']:
            #li(a(i.title(), href='/%s.html' % i))

#    with div(cls='row'):
#        h1('education-counts-jobs')
#        h2(dicrsch[ranjoz]['title'])
#        p(dicrs)
        #p(dicrsch[ranjoz]['description'])
#        p(a(dicrs, href= dicrsch[ranjoz]['link']))
        
        #for ked in kederz:
        #print ked
        #    p((kederz[ked]))
        #print ked
        #print ked

        


# In[ ]:

#print doc

#docre = doc.render()
#s = docre.decode('ascii', 'ignore')
#yourstring = docre.encode('ascii', 'ignore').decode('ascii')
#indfil = ('/home/wcmckee/minedujob/index.html')
#mkind = open(indfil, 'w')
#mkind.write(yourstring)
#mkind.close()


# In[ ]:

#jsmsdob = json.dumps(msjobdic)


# In[ ]:

#opeind = open('/home/wcmckee/minedujob/minedujobs.json', 'w')


# In[ ]:

#opeind.write(jsmsdob)


# In[ ]:

#opeind.close()


# In[ ]:




# In[ ]:



