
# coding: utf-8

# In[1]:

from get_content import get_content


# In[2]:

def extract(text):
    return [s.split() for s in text.split('\n') if len(s)>0]


# In[3]:

def result():
    target = 'https://raw.githubusercontent.com/witch-house/pronoun.is/develop/resources/pronouns.tab'
    source = get_content(target)
    return extract(source)


# In[4]:

if __name__ == '__main__':
    printme = result()
    for r in printme:
        print(r)

