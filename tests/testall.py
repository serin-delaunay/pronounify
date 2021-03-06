
# coding: utf-8

# In[1]:

from import_utils import add_relative_path
add_relative_path('..')


# In[2]:

import unittest


# In[3]:

import json
from make_json import make_json #ipython
#from .make_json import make_json #python

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
    def test_fail_missing(self):
        with self.assertRaises(Exception):
            make_json([['a','b','c','d']])
        with self.assertRaises(Exception):
            make_json([[]])


# In[4]:

import from_pronoun_is
class pronoun_is_tests(unittest.TestCase):
    def test_parsing(self):
        self.assertEqual(
            from_pronoun_is.extract(
                """ze	hir	hir	hirs	hirself
ze	zir	zir	zirs	zirself"""),
            [['ze','hir','hir','hirs','hirself'],
             ['ze','zir','zir','zirs','zirself']])
    def test_results(self):
        r = from_pronoun_is.result()
        self.assertGreater(len(r), 10)
        for x in r:
            self.assertEqual(len(x),5)
            for p in x:
                self.assertIsInstance(p, str)


# In[5]:

import from_nonbinary_org
class nonbinary_org_tests(unittest.TestCase):
    def test_parsing_basic(self):
        self.assertEqual(
            from_nonbinary_org.extract(
                'I, me, my, mine, myself'),
            [['I','me','my','mine','myself']])
        self.assertEqual(
            from_nonbinary_org.extract(
                'I, me, my, mine, myself. blah blah '
                'she, her, her, hers, herself miaouw '),
            [['I','me','my','mine','myself'],
             ['she','her','her','hers','herself']])
    def test_parsing_alternatives(self):
        self.assertEqual(
            from_nonbinary_org.extract(
                'a, b, c, d (e), f'),
            [['a','b','c','d','f'],
             ['a','b','c','e','f']])
        self.assertEqual(
            from_nonbinary_org.extract(
                'a, b, c, d, e (f)'),
            [['a','b','c','d','e'],
             ['a','b','c','d','f']])
        self.assertEqual(
            from_nonbinary_org.extract(
                'a, b (g), c, d, e (f)'),
            [['a','b','c','d','e'],
             ['a','b','c','d','f'],
             ['a','g','c','d','e'],
             ['a','g','c','d','f']])
    def test_results(self):
        r = from_nonbinary_org.result()
        self.assertGreater(len(r), 20)
        for x in r:
            self.assertEqual(len(x),5)
            for p in x:
                self.assertIsInstance(p, str)


# In[6]:

import from_tumblr_com
class tumblr_com_tests(unittest.TestCase):
    def test_parsing(self):
        self.assertEqual(
            from_tumblr_com.extract(
                'a/b/c/d/e f/g/h/i/j'),
            [['a','b','c','d','e'],
             ['f','g','h','i','j']])
    def test_results(self):
        r = from_tumblr_com.result()
        self.assertGreater(len(r), 5)
        for x in r:
            try:
                self.assertEqual(len(x),5)
            except AssertionError:
                print("offending pronoun set:{0}".format(x))
                raise
            for p in x:
                self.assertIsInstance(p, str)
        

