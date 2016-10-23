
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


# In[23]:

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
    #def validate_entry(self, obj):
    #    pass
    def accepts_single(self, pronouns):
        single = make_json([pronouns])
        obj = json.loads(single)
        self.validate_format(obj)
        self.assertEqual(pronouns[0], obj['thirdPersonPronouns'][0]['subject'])
        self.assertEqual(pronouns[1], obj['thirdPersonPronouns'][0]['object'])
        self.assertEqual(pronouns[2], obj['thirdPersonPronouns'][0]['dependentPossessive'])
        self.assertEqual(pronouns[3], obj['thirdPersonPronouns'][0]['independentPossessive'])
        self.assertEqual(pronouns[4], obj['thirdPersonPronouns'][0]['reflexive'])
    def test_accepts_single(self):
        self.accepts_single(('they', 'them', 'their', 'theirs', 'themself'))
        self.accepts_single(('moo', 'quack', 'Carmilla Karnstein', 'a'*2048,
                             '¬!"£$%^&*()_+`1234567890-=QWERTYUIOP{}qwertyuiop[]'
                             'ASDFGHJKL:@~asdghjkl;\'#|ZXCVBNM<>?\\zxcvbnm,./'))
    #def test_accepts_multiple(self):
    #    pass


# In[ ]:



