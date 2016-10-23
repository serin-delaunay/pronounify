
# coding: utf-8

# In[1]:

import os,sys


# In[2]:

def add_relative_path(rp):
    ap = os.path.abspath(rp)
    if ap not in sys.path:
        sys.path.insert(1,ap)

