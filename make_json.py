
# coding: utf-8

# In[1]:

import json
from bad_pronouns import bad_pronouns


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

def make_json(pronouns, fn=None):
    pronouns = set(tuple(p) for p in pronouns)
    pronouns = [make_obj(p) for p in sorted(pronouns)]
    py_obj = OrderedDict([
            ('description', 'Third person personal pronouns with case'),
            ('thirdPersonPronouns', pronouns)])
    if fn is None:
        return json.dumps(py_obj, indent=2)
    else:
        json.dump(py_obj, open(fn, 'w', encoding='utf8'),
                  indent=2, ensure_ascii=False)


# In[5]:

def check_pronoun(ps):
    weird = False
    if any(p.endswith('elf') or p.endswith('elves') for p in ps[:-1]):
        weird = True
    if not (ps[4].endswith('elf') or ps[4].endswith('elves')):
        weird = True
    if weird:
        print('weird pronoun set: {0}'.format(ps))


# In[6]:

def check_pronouns(pronouns):
    for p in pronouns:
        check_pronoun(p)


# In[7]:

from from_nonbinary_org import result as result1
from from_pronoun_is import result as result2
from from_tumblr_com import result as result3


# In[8]:

if __name__ == '__main__':
    print('getting pronouns')
    all_pronouns = result1()+result2()+result3()
    print('got {0} pronouns'.format(len(all_pronouns)))
    print('making json')
    check_pronouns(all_pronouns)
    all_pronouns = filter(lambda x: x not in bad_pronouns,
                          all_pronouns)
    make_json(all_pronouns, 'thirdPersonPronouns.json')
    print('done')
    #print(make_json(all_pronouns)) # let's not

