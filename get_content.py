
# coding: utf-8

# In[1]:

import requests


# In[2]:

def get_content(url):
    rq = requests.get(url)
    content = rq.content.decode()
    rq.close()
    return content

