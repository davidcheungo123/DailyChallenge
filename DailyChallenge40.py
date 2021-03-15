#!/usr/bin/env python
# coding: utf-8

# In[20]:


def transpose_matrix(inputList):
    ans = []
    row_counts = len(inputList)
    col_counts = len(inputList[0])
            
    for i in range(col_counts):
        ans.append([])
        for j in range(row_counts):
            ans[i].append(inputList[j][i])
            
    return ans
    


# In[21]:


transpose_matrix([ [1, 1, 1], [2, 2, 2], [3, 3, 3] ])


# In[22]:


transpose_matrix([ [5, 5], [6, 7], [9, 1] ])


# In[ ]:




