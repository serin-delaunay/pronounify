
# coding: utf-8

# In[1]:

import re
from get_content import get_content


# In[2]:

from bs4 import BeautifulSoup


# In[3]:

def extract(text):
    r = "([a-zA-Z'*]+/){4}[a-zA-Z'*]+"
    # "asd/as*/a*d/*sd/dsa"
    pronouns = [m.group().split(', ') for m in re.finditer(r, text)]
    return [ps[0].split('/') for ps in pronouns]


# In[4]:

def result():
    targets = ['http://destroythecistem.tumblr.com/pronouns',
               'http://askanonbinary.tumblr.com/general',
               #'http://askanonbinary.tumblr.com/non-english',
               'http://askanonbinary.tumblr.com/animal',
               'http://askanonbinary.tumblr.com/nature',
               'http://askanonbinary.tumblr.com/creature',
               'http://askanonbinary.tumblr.com/royal',
               'http://askanonbinary.tumblr.com/ungrouped'
              ]
    def all_texts():
        for target in targets:
            content_html = get_content(target)
            soup = BeautifulSoup(content_html, 'lxml')
            for script in soup(['script', 'style']):
                script.extract()
            yield soup.get_text()
    all_pronouns = '\n'.join(all_texts())
    return extract(all_pronouns)


# In[5]:

if __name__ == '__main__':
    printme = result()
    for r in printme:
        print(r)

