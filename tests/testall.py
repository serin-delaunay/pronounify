
# coding: utf-8

# In[6]:

from import_utils import add_relative_path
add_relative_path('..')


# In[17]:

import unittest
import json
from make_json import make_json #ipython
#from .make_json import make_json #python


# In[19]:

def correct_format(text):
    obj = json.loads(text)


# In[26]:

class json_tests(unittest.TestCase):
    def validate_format(self, obj):
        self.assertEqual(set(obj.keys()), {'description','thirdPersonPronouns'})
        self.assertEqual(obj['description'], 'Third person personal pronouns with case')
        self.assertIsInstance(obj['thirdPersonPronouns'], list)
        for x in obj['thirdPersonPronouns']:
            self.assertIsInstance(x, dict)
            self.assertEqual(set(x.keys()),
                             {'subject', 'object',
                              'dependentPossessive',
                              'independentPossessive',
                              'reflexive'})
            for y in x.values():
                self.assertIsInstance(y, str)
    def test_accepts_empty(self):
        empty = make_json([])
        obj = json.loads(empty)
        self.validate_format(obj)
    def validate_entry(self, pronouns, obj):
        self.assertEqual(pronouns[0], obj['subject'])
        self.assertEqual(pronouns[1], obj['object'])
        self.assertEqual(pronouns[2], obj['dependentPossessive'])
        self.assertEqual(pronouns[3], obj['independentPossessive'])
        self.assertEqual(pronouns[4], obj['reflexive'])
    def accepts_single(self, pronouns):
        single = make_json([pronouns])
        obj = json.loads(single)
        self.validate_format(obj)
        self.validate_entry(pronouns, obj['thirdPersonPronouns'][0])
    def test_accepts_single(self):
        self.accepts_single(('they', 'them', 'their', 'theirs', 'themself'))
        self.accepts_single(('moo', 'quack', 'Carmilla Karnstein', 'a'*2048,
                             '¬!"£$%^&*()_+`1234567890-=QWERTYUIOP{}qwertyuiop[]'
                             'ASDFGHJKL:@~asdghjkl;\'#|ZXCVBNM<>?\\zxcvbnm,./'))
    def test_accepts_multiple(self):
        multiple = make_json([['a','b','c','d','e'],['f','g','h','i','j']])
        obj = json.loads(multiple)
        self.validate_format(obj)
        self.validate_entry(['a','b','c','d','e'],obj['thirdPersonPronouns'][0])
        self.validate_entry(['f','g','h','i','j'],obj['thirdPersonPronouns'][1])
    def test_removes_dupes(self):
        multiple = make_json([['a','b','c','d','e'],
                              ['f','g','h','i','j'],
                              ['a','b','c','d','e']])
        obj = json.loads(multiple)
        self.validate_format(obj)
        self.assertEqual(len(obj['thirdPersonPronouns']), 2)
        self.validate_entry(['a','b','c','d','e'],obj['thirdPersonPronouns'][0])
        self.validate_entry(['f','g','h','i','j'],obj['thirdPersonPronouns'][1])
        


# In[ ]:



