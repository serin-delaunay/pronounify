
# coding: utf-8

# In[1]:

import requests
from bs4 import BeautifulSoup


# In[2]:

def get_content(url):
    rq = requests.get(url)
    content = rq.content.decode()
    rq.close()
    return content


# In[3]:

def get_html_plaintext(content_html):
        soup = BeautifulSoup(content_html, 'lxml')
        for script in soup(['script', 'style']):
            script.extract()
        return soup.get_text()

