
# coding: utf-8

# In[1]:

import re


# In[2]:

from itertools import product, chain


# In[3]:

def split_nbo_alts(p):
    ps = p.split()
    return [ps[0]]+[x[1:-1] for x in ps[1:]]


# In[4]:

def extract(text):
    r = "([a-zA-Z']+ \([a-zA-Z']+\), |[a-zA-Z']+, ){4}([a-zA-Z']+ \([a-zA-Z']+\)|[a-zA-Z']+)"
    # "asd, asd (asdf), asd'f, as, a"
    nbo = [m.group().split(', ') for m in re.finditer(r, text)]
    nbo_alts = [[split_nbo_alts(p) for p in ps] for ps in nbo]
    nbo_variants_all = [list(x) for x in chain.from_iterable(product(*alts) for alts in nbo_alts)]
    return list(filter(lambda x: 'and' not in x, nbo_variants_all))


# In[5]:

def result():
    blather = open('nonbinary_org.txt', encoding="utf8").read()
    # http://nonbinary.org/wiki/Pronouns (English section)
    return extract(blather)


# In[6]:

if __name__ == '__main__':
    printme = result()
    for r in printme:
        print(r)

