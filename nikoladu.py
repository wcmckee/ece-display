
# coding: utf-8

# Nikoladu
# 
# This script opens a json file of jobs at Ministry Of Education. It creates a rst file for each job - along with a meta file. This is then turned into a static blogs. 
# The title of each blog post is the ID of the job. I used this as it is unique. It ignores the first 3 characters (edu) and just focus on the number.
# The post content was just the job title, but I have updated it to include helpful skills to have. 
# Location and category of job is added as tags to the post. 

# In[ ]:




# In[33]:

#import nikola

import requests
import json
import getpass
import pandas
import os


# In[ ]:




# In[34]:

myusr = getpass.getuser()


# In[35]:

with open('/home/{}/moejobs/index.json'.format(myusr), 'r') as opedu:
          dicminj = json.loads(opedu.read())


# In[ ]:




# In[36]:

#opedu = open('/home/{}/moejobs/index.json'.format(myusr), 'rb', 'utf-8')


# In[ ]:




# In[37]:

#minjob = opedu.read()


# In[38]:

#dicminj = json.loads(minjob)


# In[39]:

ldic = len(dicminj)


# In[40]:

#print(dicminj)


# In[41]:

catlis = list()

loclis = list()
datlis = list()
jobti = list()


# In[ ]:




# In[42]:

numdic = dict()


# In[ ]:




# In[43]:

#catedi


# In[ ]:




# In[44]:

#for hel in helpth:
    #print(hel[0] + '/n')


# In[ ]:




# In[ ]:




# In[ ]:




# In[45]:

testlay = list()


# In[ ]:




# In[ ]:




# In[ ]:




# In[46]:

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
    jorefd = jobref.replace('/', '-')
    print (jorefd)
    
    with open('/home/{}/minstryofedu/posts/{}.meta'.format(myusr, jorefd), 'w') as moemeta:
        moemeta.write(jorefd + '\n' + jorefd + '\n' + str(pdate) + ' ' + str('09:00:00') + '\n' + catedi + ', ' + locdi)
    #opmetf = open('/home/{}/minstryofedu/posts/{}.meta'.format(myusr, jorefd), 'w')
    #opmetf.write(jorefd + '\n' + jorefd + '\n' + str(pdate) + ' ' + str('09:00:00') + '\n' + catedi + ', ' + locdi)
    #opmetf.close()
    #print(helpth)
    for hel in helpth:
        print(hel[0] + '/n')
        testlay.append(hel[0])
        with open('/home/{}/minstryofedu/posts/{}.rst'.format(myusr, jorefd), 'w') as moerst:
            moerst.write(titdi)
    #oprstfi = open('/home/{}/minstryofedu/posts/{}.rst'.format(myusr, jorefd), 'w')
    #oprstfi.write(titdi)
    #oprstfi.close()



    dicjob.update({'Category' : catedi, 'Date Advertised' : str(pdate), 'Job Title' : titdi,
    'Location' : locdi, 'Job Reference' : jobref, 'reqs' : helpth})
    
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




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[47]:

#json.dumps(numdic)


# In[48]:

with open('/home/{}/minstryofedu/output/index.json'.format(myusr), 'w') as moerst:
    moerst.write(json.dumps(numdic))


# In[49]:

testlay


# In[50]:

os.chdir('/home/{}/minstryofedu/'.format(myusr))


# In[51]:

os.system('nikola build')


# In[52]:

os.system('aws s3 sync /home/{}/minstryofedu/output/ s3://moejobs'.format(myusr))


# In[ ]:



