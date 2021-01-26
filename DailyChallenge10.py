#!/usr/bin/env python
# coding: utf-8

# In[7]:


def binary(num):
    binary = bin(num)[2:]
    one_num = binary.count("1")
    
    indexing = []
    diff = []
    
    for iterator in range(one_num):
        indexing.append(binary.index("1"))
        binary = binary.replace("1", "", 1)
    
    for i in range(len(indexing)-1):
        diff.append(indexing[i+1]-indexing[i])
    
    if len(diff) >0:
        return max(diff)
    else:
        return 0
    
for num in [9,529,20,15]:
    print(f"The output of the input {num} is {binary(num)}")
    


# In[ ]:




