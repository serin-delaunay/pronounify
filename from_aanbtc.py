
# coding: utf-8

# In[1]:

import re


# In[2]:

all_pronouns = ''.join(open('aanbtc.txt').readlines())
# http://askanonbinary.tumblr.com/pronouns


# In[3]:

#all_pronouns = general + animal + nature + creature + royal + misc


# In[4]:

r = "([a-zA-Z'*]+/){4}[a-zA-Z'*]+"
pronouns = [m.group().split(', ') for m in re.finditer(r, all_pronouns)]


# In[5]:

result = [ps[0].split('/') for ps in pronouns]


# In[6]:

result

