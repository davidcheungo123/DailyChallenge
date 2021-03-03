#!/usr/bin/env python
# coding: utf-8

# In[1]:


def number_of_swaps(inputList):
    counter = 0
    
    for i in range(len(inputList)-1):
        for j in range(i+1, len(inputList)):
            if inputList[i] > inputList[j]:
                inputList[i] , inputList[j] = inputList[j], inputList[i]
                counter +=1
                
    return counter


# In[2]:


number_of_swaps([5, 4, 3])


# In[3]:


number_of_swaps([1, 3, 4, 5])


# In[4]:


number_of_swaps([5, 4, 3, 2])


# In[ ]:




