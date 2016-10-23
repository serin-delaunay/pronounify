
# coding: utf-8

# In[1]:

import re


# In[2]:

from itertools import product, chain


# In[3]:

blather = ''.join(open('nonbinary_org.txt', encoding="utf8").readlines())
# http://nonbinary.org/wiki/Pronouns (English section)


# In[4]:

r = "([a-zA-Z']+ \([a-zA-Z']+\), |[a-zA-Z']+, ){4}([a-zA-Z']+ \([a-zA-Z']+\)|[a-zA-Z']+)"
nbo = [m.group().split(', ') for m in re.finditer(r, blather)]


# In[5]:

def split_nbo_alts(p):
    ps = p.split()
    return [ps[0]]+[x[1:-1] for x in ps[1:]]


# In[6]:

nbo_alts = [[split_nbo_alts(p) for p in ps] for ps in nbo]


# In[7]:

nbo_variants_all = [list(x) for x in chain.from_iterable(product(*alts) for alts in nbo_alts)]


# In[8]:

result = list(filter(lambda x: 'and' not in x, nbo_variants_all))


# In[9]:

result

