
# coding: utf-8

# In[1]:

source = open('pronoun_is.txt').read()
# https://github.com/witch-house/pronoun.is/blob/develop/resources/pronouns.tab


# In[2]:

result = [s.split() for s in source.split('\n')]


# In[3]:

result

