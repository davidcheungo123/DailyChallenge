#!/usr/bin/env python
# coding: utf-8

# In[1]:


def returnInt(inputList):
    numStr = 0
    numInt =0
    for element in inputList:
        if isinstance(element, str):
            numStr += int(element)
        elif isinstance(element, int):
            numInt += element
        else:
            continue
    
    return numStr - numInt


returnInt([1, '2', 3, '4', 5])

            
            


# In[ ]:




