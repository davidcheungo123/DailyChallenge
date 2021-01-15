#!/usr/bin/env python
# coding: utf-8

# In[19]:


def sum_cubes(n):
    print([i for i in range(n) if i == round(i** (1/3))**3])
    return sum([i for i in range(n) if i == round(i** (1/3))**3])

print(sum_cubes(100))


# In[ ]:





# In[ ]:




