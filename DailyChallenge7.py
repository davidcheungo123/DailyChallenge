#!/usr/bin/env python
# coding: utf-8

# In[3]:


def oddOne(listInput):
    listSet = set(listInput)
    D = {}
    for item in listInput:
        if item not in D:
            D[item] = 1
        else:
            D[item] +=1
            
    return min(D, key=D.get)

oddOne([1,1,1,1,1,1,1,2])


# In[ ]:




