#!/usr/bin/env python
# coding: utf-8

# In[1]:


def countLowercase(inputStr):
    alphaList = list(inputStr)
    
    D = {}
    
    for alpha in alphaList:
        if alpha.islower():
            if alpha not in D:
                D[alpha] =1

            else:
                D[alpha] +=1
        else:
            continue
            
    return D

countLowercase("apple")


# In[ ]:




