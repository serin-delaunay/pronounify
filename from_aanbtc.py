
# coding: utf-8

# In[1]:

import re


# In[2]:

def extract(text):
    r = "([a-zA-Z'*]+/){4}[a-zA-Z'*]+"
    # "asd/as*/a*d/*sd/dsa"
    pronouns = [m.group().split(', ') for m in re.finditer(r, text)]
    return [ps[0].split('/') for ps in pronouns]


# In[3]:

def result():
    all_pronouns = open('aanbtc.txt').read()
    # http://askanonbinary.tumblr.com/pronouns
    #all_pronouns = general + animal + nature + creature + royal + misc
    return extract(all_pronouns)


# In[4]:

if __name__ == '__main__':
    printme = result()
    for r in printme:
        print(r)

