
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

# In[379]:




# In[379]:




# In[379]:




# In[380]:

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
import bs4
#import pyshorteners
#import tweepy


# In[380]:




# In[380]:




# In[381]:

#dnz = Dnz('keyhere')


# In[382]:

jobreq = requests.get('https://jobs.minedu.govt.nz/jobtools/job_rss?o1=17584&k2=A52B3674BC046465&source=JobRSS&medium=JobRSS')


# In[383]:

jobtxta = jobreq.text


# In[384]:

#obj = untangle.parse(jobtxta)


# In[385]:

#obj


# In[386]:

dicjobz = xmltodict.parse(jobtxta)


# In[387]:

ranldicj = len(dicjobz['rss']['channel']['item'])


# In[388]:

#ranldicj


# In[389]:

#randicz = random.randint(0, ranldicj)


# In[390]:

#randicz


# In[391]:

wrapdict = dict()


# In[394]:

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
    opind = open('/home/wcmckee/minedujob/index.json', 'w')
    opind.write(jsmsdob)
    #api.update_status(dicrts)
    #opeind.close()
    
    


# In[395]:

opind.close()


# In[ ]:




# In[ ]:

#opeind.close()


# In[300]:

#dicrs = dicjobz['rss']['channel']['item'][0]


# In[301]:

#dicrts = dicrs['title']
#dicrtq = dicrs


# In[182]:

#artim = arrow.now(dicrtq['pubDate'])


# In[183]:

#jobclose = artim.replace(weeks=+2)


# In[184]:

#jclodat = jobclose.date()


# In[184]:




# In[185]:

#msjobdic = dict()


# In[186]:

#msjobdic.update({'date-advertised' : str(artim.date()), 
#                'time-advertised' : str(artim.time()),
#                'title' : dicrts,
#                'date-closed' : str(jclodat)})


# In[187]:

#msjobdic


# In[188]:

#requlink = dicrtq['link']


# In[189]:

#reqlinkq = requests.get(requlink)


# In[190]:

#bsoup = bs4.BeautifulSoup(reqlinkq.text)


# In[191]:

#bfina = bsoup.findAll('a')


# In[192]:

#msjobdic.update({'date advertised' : str(artim.date()), 
#                'time advertised' : str(artim.time()),
#                'title' : dicrts,
#                '})
#for bfin in bfina:
#    if ('@') in bfin.text:
#        #print bfin.text
#        msjobdic.update({('email') : str(bfin.text)})
        


# In[193]:

#for bfiny in bfina:
#    if '.docx' in bfiny.text:
#        print bfiny.text


# In[194]:

#Search for this file and render text.
#if jpg/gif render.


# In[195]:

#for bfin in bfina:
#    if ('href') in bfin.text:
        #print bfin.text
#        msjobdic.update({('href') : str(bfin.text)})


# In[196]:

#msjob


# In[197]:

#msjobdic.update({'randnum' : randicz})


# In[198]:

#for bfiny in bfina:
#    if '.docx' in bfiny.text:
#        msjobdic.update({'doc' : bfiny.text})


# In[199]:

#msjobdic


# In[200]:

#msjobdic.update({'link' : dicrtq['link']})


# In[201]:

#msjobdic


# In[202]:

#msjobdic.update({'doc' : b


# In[203]:

#bsdescr = bs4.BeautifulSoup(dicrtq['description'])


# In[204]:

#for iza in bsdescr.findAll('li')[0:8]:
#    print iza


# In[205]:

#lili = list()


# In[206]:

#txtspli = [line.text.split(": ") for line in bsdescr.findAll('li')[0:8]]


# In[207]:

#findict = dict()


# In[208]:

#totlen = len(txtspli)


# In[209]:

#for tes in range(totlen):
#    findict.update({txtspli[tes][0] : txtspli[tes][1]})
    


# In[210]:

#findict.update({txtspli[0][0] : txtspli[0][1]})


# In[211]:

#msjobz = findict.copy()
#msjobz.update(msjobdic)


# In[212]:

#for bsdz in bsdescr.findAll('li'):
#    (k,v) = bsdz.text.split(": ")
#    print bsdz.text
#    print(k,v)
#    lili.append(bsdz.text)


# In[213]:

#txtlis = list()


# In[213]:




# In[214]:

#bsp = bsdescr.findAll('p')


# In[215]:

#for bs in bsp:
    #print bs.text
    #txtlis.append(bs.text)
    #numchc = [int(s) for s in bs.text.split() if s.isdigit()]
    #It's skipping items in the li since thats not a p :( 
    #There are other details in the description that I 
    #would like to extract - like closing date. 
    #Why not for closing date just take the date it was 
    #advertised and + 2 weeks?
    


# In[216]:

#dicrts


# In[217]:

#debsnz =  dnz.search(dicrs)


# In[218]:

#randrecord = len(debsnz.records)


# In[219]:

#ranitdz = random.randint(0, randrecord)


# In[220]:

#ranitdz


# In[221]:

#randicz


# In[222]:

#debsnz.records


# In[223]:

#debrecintz = debsnz.records[ranitdz]


# In[224]:

#kederz = debrecintz.keys()


# In[225]:

#print debrecintz['category']
#print debrecintz['usage']


# In[226]:

#for ked in kederz:
#    print ked
#    print debrecintz[ked]
    #print ked
    #print ked
    #print debrecintz['category']


# In[227]:

#print debrecintz['id']


# In[228]:

#getiddnz = ('http://api.digitalnz.org/v3/records/' + str(debrecintz['id']) + '.json?api_key=Ph2LDuyiJmJcQm1S5myy')


# In[229]:

#getiddnz


# In[230]:

#reqidnz = requests.get(getiddnz)


# In[231]:

#json.dumps(reqidnz)


# In[232]:

#mylirq = list()


# In[233]:

#for reqi in reqidnz:
    #print reqi
    #print reqi.upper()
    #reqi


# In[234]:

#my_dict.pop("key", None)


# In[235]:

#dicrq = len(dicjobz['rss']['channel']['item'])


# In[236]:

#dicrq


# In[237]:

#Return a random job.


# In[238]:

#ranjoz = random.randint(0, dicrq)

#dicrsch = dicjobz['rss']['channel']['item']


# In[239]:

#print dicrsch[ranjoz]['link']


# In[240]:

#print dicrsch[ranjoz]['title']


# In[241]:

#jobtype
#location
#date advertised
#jobreference
#jobtitle
#should be keys
#Currently they are inside description key
#Create new json file that fixes this.


# In[242]:

#for dezsr in  dicrsch[ranjoz]['description']:
##    if 'JobType' in dezs#r:
# #       print dezsr


# In[243]:

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

        


# In[244]:

#print doc

#docre = doc.render()
#s = docre.decode('ascii', 'ignore')
#yourstring = docre.encode('ascii', 'ignore').decode('ascii')
#indfil = ('/home/wcmckee/minedujob/index.html')
#mkind = open(indfil, 'w')
#mkind.write(yourstring)
#mkind.close()


# In[261]:

#jsmsdob = json.dumps(msjobdic)


# In[262]:

#opeind = open('/home/wcmckee/minedujob/minedujobs.json', 'w')


# In[263]:

#opeind.write(jsmsdob)


# In[264]:

#opeind.close()


# In[248]:




# In[ ]:



