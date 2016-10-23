
# coding: utf-8

# In[1]:

import json


# In[2]:

from collections import OrderedDict


# In[3]:

def make_obj(pronoun):
    r = OrderedDict()
    r['subject']= pronoun[0]
    r['object']= pronoun[1]
    r['dependentPossessive']= pronoun[2]
    r['independentPossessive']= pronoun[3]
    r['reflexive']= pronoun[4]
    return r


# In[4]:

def make_json(pronouns, fn='thirdPersonPronouns.json'):
    pronouns = set(tuple(p) for p in pronouns)
    pronouns = [make_obj(p) for p in sorted(pronouns)]
    py_obj = {'description': 'Third person personal pronouns with case',
              'thirdPersonPronouns': pronouns}
    return json.dump(py_obj, open(fn, 'w'),indent=2)


# In[5]:

from from_nonbinary_org import result as result1
from from_pronoun_is import result as result2
from from_aanbtc import result as result3


# In[6]:

if __name__ == '__main__':
    make_json(result1+result2+result3)


# In[38]:

#print(make_json(result1+result2+result3))

