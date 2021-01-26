#!/usr/bin/env python
# coding: utf-8

# In[2]:


def sumThree(n):
    return sum(i for i in range(n+1) if i %3 ==0)

print(sumThree(10))


# In[ ]:




