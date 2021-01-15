#!/usr/bin/env python
# coding: utf-8

# In[1]:


def divisions(n, divisor):
    
    number_of_times = len([ divisor**i for i in range(1, n) if divisor**i <= n and n % divisor**i == 0])
    
    return number_of_times

print(divisions(12,3))


# In[ ]:




