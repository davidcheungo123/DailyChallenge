#!/usr/bin/env python
# coding: utf-8

# In[8]:


def difference(numInput):
    numInput = str(numInput)
    strList = list(numInput)
    maximun = ""
    minimum = ""
    
    maxStrList = sorted(strList, key=lambda x: int(x), reverse=True)
    minStrList = sorted(strList, key=lambda x: int(x))
    
    for strDigit1, strDigit2 in zip(maxStrList, minStrList):
        maximun += strDigit1
        minimum += strDigit2
        
    difference = int(maximun) - int(minimum)
    
    return difference
        
    
    
print(difference(123456789))
print(difference(20))


# In[ ]:




