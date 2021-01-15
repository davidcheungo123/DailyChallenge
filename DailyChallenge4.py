#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math

#at least one pair

def calculate_probability(n):
    return 1- (math.factorial(365) / math.factorial(365-n)) / (365)**n



#another possbile solution:
def calculate_probability1(n):
    
    return 1 - (364/365)**(n*(n-1)/2)

print(calculate_probability(5))
print(calculate_probability1(5))


# In[ ]:




