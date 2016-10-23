
# coding: utf-8

# In[1]:

import re
from get_content import get_content, get_html_plaintext


# In[2]:

def extract(text):
    r = "([a-zA-Z'*]+/){4}[a-zA-Z'*]+"
    # "asd/as*/a*d/*sd/dsa"
    pronouns = [m.group().split(', ') for m in re.finditer(r, text)]
    return [ps[0].split('/') for ps in pronouns]


# In[3]:

def result():
    targets = [#'http://destroythecistem.tumblr.com/pronouns',
               'http://pronoun-provider.tumblr.com/pronouns',
               #'http://askanonbinary.tumblr.com/general',
               #'http://askanonbinary.tumblr.com/non-english',
               'http://askanonbinary.tumblr.com/animal',
               #'http://askanonbinary.tumblr.com/nature',
               #'http://askanonbinary.tumblr.com/creature',
               #'http://askanonbinary.tumblr.com/royal',
               #'http://askanonbinary.tumblr.com/ungrouped'
              ]
    print("getting html from {0} urls".format(len(targets)))
    all_pronouns = '\n'.join(get_html_plaintext(get_content(target))
                             for target in targets)
    print("html contained {0} plaintext chars".format(len(all_pronouns)))
    return extract(all_pronouns)


# In[4]:

if __name__ == '__main__':
    printme = result()
    for r in printme:
        print(r)

