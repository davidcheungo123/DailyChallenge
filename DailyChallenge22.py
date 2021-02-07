#!/usr/bin/env python
# coding: utf-8

# In[4]:


def decimalDigits(inputStr):
    finalStr = ""
    for element in inputStr:
        finalStr += bin(int(element))[2:]
        
    return int(finalStr)

decimalDigits("2973")


# In[ ]:




