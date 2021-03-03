#!/usr/bin/env python
# coding: utf-8

# In[7]:


import itertools as it

def checkIfPower(x):
    for num in x:
        if num % 3 !=  0 and num !=1:
            return False
    return True

def powerSum(numInput):
    numList = range(1, numInput +1)
    
    finalList = []
    
    for i in range(2, numInput+1):
        for j in it.combinations_with_replacement(numList, i):
            if sum(j) == numInput:
                finalList.append(j)
                
    ulList = []
                
    for iteralElement in finalList:
        if checkIfPower(iteralElement):
            ulList.append(iteralElement)
                
    return ulList
        
powerSum(6)
    


# In[ ]:




