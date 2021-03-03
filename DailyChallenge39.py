#!/usr/bin/env python
# coding: utf-8

# In[43]:


import math
import itertools as it
def checkprimes(x):
    counter = 0
    for i in range(1,x+1):
        if x % i ==0:
            counter +=1
        else:
            continue
    if counter == 2:
        return True
    else:
        return False

def semiprime(inputInt):
    for i,j in it.product(range(2, inputInt), repeat=2):
        if inputInt % (i * j) ==0:
            if checkprimes(i) and checkprimes(j) and i != j:
                return "Squarefree Semiprime"
            elif checkprimes(i) and checkprimes(j) and i ==j:
                return "Semiprime"
            else:
                continue
        else:
            continue
    return "Neither"


# In[44]:


semiprime(49)


# In[45]:


semiprime(15)


# In[46]:


semiprime(97)


# In[ ]:





# In[ ]:




