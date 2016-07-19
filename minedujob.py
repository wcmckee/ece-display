
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

jobreq = requests.get('https://jobs.minedu.govt.nz/jobtools/job_rss?o1=17584&k2=A52B3674BC046465&source=JobRSS&medium=JobRSS', verify=False)


# In[5]:

jobtxta = jobreq.text


# In[6]:

#obj = untangle.parse(jobtxta)


# In[7]:

#obj


# In[8]:

dicjobz = xmltodict.parse(jobtxta)


# In[9]:

ranldicj = len(dicjobz['rss']['channel']['item'])


# In[10]:

#ranldicj


# In[11]:

#randicz = random.randint(0, ranldicj)


# In[12]:

#randicz


# In[13]:

wrapdict = dict()


# In[19]:

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
    
    


# In[20]:

#opind.close()


# In[ ]:




# In[16]:

#opeind.close()


# In[23]:

#dicrs = dicjobz['rss']['channel']['item'][0]


# In[24]:

#dicrts = dicrs['title']
#dicrtq = dicrs


# In[25]:

#artim = arrow.now(dicrtq['pubDate'])


# In[26]:

#jobclose = artim.replace(weeks=+2)


# In[27]:

#jclodat = jobclose.date()


# In[ ]:




# In[28]:

#msjobdic = dict()


# In[29]:

#msjobdic.update({'date-advertised' : str(artim.date()), 
#                'time-advertised' : str(artim.time()),
#                'title' : dicrts,
#                'date-closed' : str(jclodat)})


# In[30]:

#msjobdic


# In[31]:

#requlink = dicrtq['link']


# In[32]:

#reqlinkq = requests.get(requlink)


# In[33]:

#bsoup = bs4.BeautifulSoup(reqlinkq.text)


# In[34]:

#bfina = bsoup.findAll('a')


# In[35]:

#msjobdic.update({'date advertised' : str(artim.date()), 
#                'time advertised' : str(artim.time()),
#                'title' : dicrts,
#                '})
#for bfin in bfina:
#    if ('@') in bfin.text:
#        #print bfin.text
#        msjobdic.update({('email') : str(bfin.text)})
        


# In[36]:

#for bfiny in bfina:
#    if '.docx' in bfiny.text:
#        print bfiny.text


# In[37]:

#Search for this file and render text.
#if jpg/gif render.


# In[38]:

#for bfin in bfina:
#    if ('href') in bfin.text:
        #print bfin.text
#        msjobdic.update({('href') : str(bfin.text)})


# In[39]:

#msjob


# In[40]:

#msjobdic.update({'randnum' : randicz})


# In[41]:

#for bfiny in bfina:
#    if '.docx' in bfiny.text:
#        msjobdic.update({'doc' : bfiny.text})


# In[42]:

#msjobdic


# In[43]:

#msjobdic.update({'link' : dicrtq['link']})


# In[44]:

#msjobdic


# In[45]:

#msjobdic.update({'doc' : b


# In[46]:

#bsdescr = bs4.BeautifulSoup(dicrtq['description'])


# In[47]:

#for iza in bsdescr.findAll('li')[0:8]:
#    print iza


# In[41]:

#lili = list()


# In[42]:

#txtspli = [line.text.split(": ") for line in bsdescr.findAll('li')[0:8]]


# In[43]:

#findict = dict()


# In[44]:

#totlen = len(txtspli)


# In[45]:

#for tes in range(totlen):
#    findict.update({txtspli[tes][0] : txtspli[tes][1]})
    


# In[46]:

#findict.update({txtspli[0][0] : txtspli[0][1]})


# In[47]:

#msjobz = findict.copy()
#msjobz.update(msjobdic)


# In[48]:

#for bsdz in bsdescr.findAll('li'):
#    (k,v) = bsdz.text.split(": ")
#    print bsdz.text
#    print(k,v)
#    lili.append(bsdz.text)


# In[49]:

#txtlis = list()


# In[49]:




# In[50]:

#bsp = bsdescr.findAll('p')


# In[51]:

#for bs in bsp:
    #print bs.text
    #txtlis.append(bs.text)
    #numchc = [int(s) for s in bs.text.split() if s.isdigit()]
    #It's skipping items in the li since thats not a p :( 
    #There are other details in the description that I 
    #would like to extract - like closing date. 
    #Why not for closing date just take the date it was 
    #advertised and + 2 weeks?
    


# In[52]:

#dicrts


# In[53]:

#debsnz =  dnz.search(dicrs)


# In[54]:

#randrecord = len(debsnz.records)


# In[55]:

#ranitdz = random.randint(0, randrecord)


# In[56]:

#ranitdz


# In[57]:

#randicz


# In[58]:

#debsnz.records


# In[59]:

#debrecintz = debsnz.records[ranitdz]


# In[60]:

#kederz = debrecintz.keys()


# In[61]:

#print debrecintz['category']
#print debrecintz['usage']


# In[62]:

#for ked in kederz:
#    print ked
#    print debrecintz[ked]
    #print ked
    #print ked
    #print debrecintz['category']


# In[63]:

#print debrecintz['id']


# In[64]:

#getiddnz = ('http://api.digitalnz.org/v3/records/' + str(debrecintz['id']) + '.json?api_key=Ph2LDuyiJmJcQm1S5myy')


# In[65]:

#getiddnz


# In[66]:

#reqidnz = requests.get(getiddnz)


# In[67]:

#json.dumps(reqidnz)


# In[68]:

#mylirq = list()


# In[69]:

#for reqi in reqidnz:
    #print reqi
    #print reqi.upper()
    #reqi


# In[70]:

#my_dict.pop("key", None)


# In[71]:

#dicrq = len(dicjobz['rss']['channel']['item'])


# In[72]:

#dicrq


# In[73]:

#Return a random job.


# In[74]:

#ranjoz = random.randint(0, dicrq)

#dicrsch = dicjobz['rss']['channel']['item']


# In[75]:

#print dicrsch[ranjoz]['link']


# In[76]:

#print dicrsch[ranjoz]['title']


# In[77]:

#jobtype
#location
#date advertised
#jobreference
#jobtitle
#should be keys
#Currently they are inside description key
#Create new json file that fixes this.


# In[78]:

#for dezsr in  dicrsch[ranjoz]['description']:
##    if 'JobType' in dezs#r:
# #       print dezsr


# In[79]:

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

        


# In[80]:

#print doc

#docre = doc.render()
#s = docre.decode('ascii', 'ignore')
#yourstring = docre.encode('ascii', 'ignore').decode('ascii')
#indfil = ('/home/wcmckee/minedujob/index.html')
#mkind = open(indfil, 'w')
#mkind.write(yourstring)
#mkind.close()


# In[81]:

#jsmsdob = json.dumps(msjobdic)


# In[82]:

#opeind = open('/home/wcmckee/minedujob/minedujobs.json', 'w')


# In[83]:

#opeind.write(jsmsdob)


# In[84]:

#opeind.close()


# In[84]:




# In[84]:



