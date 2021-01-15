#!/usr/bin/env python
# coding: utf-8

# In[8]:


##For Daily Python Challenge 1
import string

def clean_string(stringInput):
    punctuation = string.punctuation
    
    for i in stringInput:
        if i in punctuation or i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            stringInput = stringInput.replace(i, "")
    return stringInput


print(clean_string("initinitinitABCDEFGHIJ!@#$%finalfinal"))


# In[ ]:




