
# coding: utf-8

# In[1]:

def extract(text):
    return [s.split() for s in text.split('\n')]


# In[2]:

def result():
    source = open('pronoun_is.txt').read()
    # https://github.com/witch-house/pronoun.is/blob/develop/resources/pronouns.tab
    return extract(source)


# In[3]:

if __name__ == '__main__':
    printme = result()
    for r in printme:
        print(r)

