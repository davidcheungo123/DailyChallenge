#!/usr/bin/env python
# coding: utf-8

# In[1]:


def power_ranger(power, minInput, maxInput):
    counter = 0
    for i in range(minInput, maxInput +1):
        if int(i**(1/power)) == float(i**(1/power)):
            counter +=1
    return counter


# In[2]:


power_ranger(2, 49, 65) 


# In[3]:


power_ranger(3, 1, 27) 


# In[4]:


power_ranger(10, 1, 5)


# In[5]:


power_ranger(5, 31, 33) 


# In[6]:


power_ranger(4, 250, 1300)


# In[ ]:




