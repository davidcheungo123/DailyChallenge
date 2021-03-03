#!/usr/bin/env python
# coding: utf-8

# In[12]:


import math
def checkPrime(x):
    if x >1:
        for i in range(2, x):
            if x % i ==0:
                return False
        return True
    else:
        return False

def filter_primes(inputList):
    ansList = []
    for ele in inputList:
        if checkPrime(ele):
            ansList.append(ele)
    return ansList


# In[13]:


filter_primes([7, 9, 3, 9, 10, 11, 27])


# In[14]:


filter_primes([10007, 1009, 1007, 27, 147, 77, 1001, 70]) 


# In[15]:


filter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]) 


# In[ ]:




