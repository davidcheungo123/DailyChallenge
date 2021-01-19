#!/usr/bin/env python
# coding: utf-8

# In[2]:


def square(n,d):
    if type(d) != str:
        d= str(d)
    
    square = [i**2 for i in range(1,n+1)]
    chars = [str(i) for i in square]
    counter = 0
    for char in chars:
        if d in char:
            counter+=1
            
    return counter

square(5,1)


# In[ ]:




