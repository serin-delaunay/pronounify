
# coding: utf-8

# In[1]:

import re


# In[2]:

from itertools import product, chain


# In[3]:

from get_content import get_content, get_html_b_h2


# In[4]:

def split_nbo_alts(p):
    ps = p.split()
    return [ps[0]]+[x[1:-1] for x in ps[1:]]


# In[5]:

def extract(text):
    r = "([a-zA-Z']+ \([a-zA-Z']+\), |[a-zA-Z']+, ){4}([a-zA-Z']+ \([a-zA-Z']+\)|[a-zA-Z']+)"
    # "asd, asd (asdf), asd'f, as, a"
    nbo = [m.group().split(', ') for m in re.finditer(r, text)]
    nbo_alts = [[split_nbo_alts(p) for p in ps] for ps in nbo]
    nbo_variants_all = [list(x) for x in chain.from_iterable(product(*alts) for alts in nbo_alts)]
    #return list(filter(lambda x: 'and' not in x, nbo_variants_all)) # the spurious 'and' isn't in bold
    return nbo_variants_all


# In[6]:

def result():
    target = 'http://nonbinary.org/wiki/Pronouns'
    start_marker = 'English neutral pronouns'
    end_marker = 'Esperanto neutral pronouns'
    blather = get_html_b_h2(get_content(target))
    blather = blather[blather.find(start_marker):blather.find(end_marker)]
    return extract(blather)


# In[7]:

if __name__ == '__main__':
    printme = result()
    for r in printme:
        print(r)

