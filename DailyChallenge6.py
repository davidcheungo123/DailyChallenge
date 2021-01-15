#!/usr/bin/env python
# coding: utf-8

# In[5]:


def middle(stringInput):
    
    if len(stringInput) %2 == 0:
        return stringInput[(int(len(stringInput)/2) -1)] + stringInput[int(len(stringInput)/2)]
    
    else:
        return stringInput[int(len(stringInput)/2)]
    
print(middle("aRRc"))
print(middle("abc"))
print(middle("aaBBcc"))


# In[ ]:




