#!/usr/bin/env python
# coding: utf-8

# In[5]:


def mostValue(strInput):
    D = {}
    for counter, strInput in enumerate(strInput):
        if strInput not in D:
            D[strInput] = [counter]
        else:
            D[strInput].append(counter)
    
    for key, valueList in D.items():
        D[key] = valueList[-1] - valueList[0]
        
    D = dict( sorted(D.items(), key=lambda x: x[0].lower()) )

    return max(D, key=D.get)

print(mostValue("abcdbcd"))


# In[ ]:




