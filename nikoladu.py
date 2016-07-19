
# coding: utf-8

# Nikoladu
# 
# This script opens a json file of jobs at Ministry Of Education. It creates a rst file for each job - along with a meta file. This is then turned into a static blogs. 
# The title of each blog post is the ID of the job. I used this as it is unique. It ignores the first 3 characters (edu) and just focus on the number.
# The post content was just the job title, but I have updated it to include helpful skills to have. 
# Location and category of job is added as tags to the post. 

# In[ ]:




# In[1]:

#import nikola

import requests
import json
import getpass
import pandas


# In[2]:

myusr = getpass.getuser()


# In[ ]:




# In[3]:

opedu = open('/home/{}/moejobs/index.json'.format(myusr), 'r')


# In[4]:

minjob = opedu.read()


# In[5]:

dicminj = json.loads(minjob)


# In[6]:

ldic = len(dicminj)


# In[11]:

#print(dicminj)


# In[12]:

catlis = list()

loclis = list()
datlis = list()
jobti = list()


# In[ ]:




# In[13]:

numdic = dict()


# In[ ]:




# In[16]:

for ldi in range(ldic):
    dicjob = dict()
    catedi = (dicminj[str(ldi)]['Category'])
    locdi = (dicminj[str(ldi)]['Location'])
    datdi = (dicminj[str(ldi)]['Date Advertised'])
    pandatz = pandas.to_datetime(datdi)
    pdate = pandatz.date()
    titdi = (dicminj[str(ldi)]['Job Title'])
    helpth = (dicminj[str(ldi)]['lidocend'])
    
    jobref = (dicminj[str(ldi)]['Job Reference'])
    jorefd = jobref[4:]
    print (jorefd)
    
    with open('/home/{}/minstryofedu/posts/{}.meta'.format(myusr, jorefd), 'w') as moemeta:
        moemeta.write(jorefd + '\n' + jorefd + '\n' + str(pdate) + ' ' + str('09:00:00') + '\n' + catedi + ', ' + locdi)
    #opmetf = open('/home/{}/minstryofedu/posts/{}.meta'.format(myusr, jorefd), 'w')
    #opmetf.write(jorefd + '\n' + jorefd + '\n' + str(pdate) + ' ' + str('09:00:00') + '\n' + catedi + ', ' + locdi)
    #opmetf.close()
    
    with open('/home/{}/minstryofedu/posts/{}.rst'.format(myusr, jorefd), 'w') as moerst:
        moerst.write(titdi)
    #oprstfi = open('/home/{}/minstryofedu/posts/{}.rst'.format(myusr, jorefd), 'w')
    #oprstfi.write(titdi)
    #oprstfi.close()



    dicjob.update({'Category' : catedi, 'Date Advertised' : str(pdate), 'Job Title' : titdi,
    'Location' : locdi, 'Job Reference' : jobref})
    
    numdic.update({ldi : dicjob})
    #numdic.update({ldi : dicjob})
    
    loclis.append(locdi)
    datlis.append(datdi)
    jobti.append(titdi)
    
    nedicf = dicjob.copy()
    nedicf.update(nedicf)
    
    numdic.update({ldi : nedicf})
    
    #if 'education' in catedi:
    #    print (catedi)

        


# In[ ]:



