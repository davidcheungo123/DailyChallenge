#!/usr/bin/env python
# coding: utf-8

# In[5]:


def return_Tuple(inputList):
    tu = (inputList[1],inputList[2],inputList[3])
    
    return (round(sum(tu)/3,2) , min(inputList))

print(return_Tuple([6.4, 11.4, 7.6, 10.5, 8.1]))


# In[ ]:




