
# coding: utf-8

# In[3]:

def extract(text):
    return [s.split() for s in text.split('\n') if len(s)>0]


# In[4]:

def get_content(url):
    rq = requests.get(url)
    content = rq.content.decode()
    rq.close()
    return content


# In[5]:

def result():
    target = 'https://raw.githubusercontent.com/witch-house/pronoun.is/develop/resources/pronouns.tab'
    source = get_content(target)
    return extract(source)


# In[6]:

if __name__ == '__main__':
    printme = result()
    for r in printme:
        print(r)

