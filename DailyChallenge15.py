#!/usr/bin/env python
# coding: utf-8

# In[3]:


def alterList(list1, list2):
    finalList = []
    for item1, item2 in zip(list1, list2):
        finalList.append(item1)
        finalList.append(item2)
    
    finalList.extend(list1[len(list2):])
    finalList.extend(list2[len(list1):])
    
    return finalList


print(alterList([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e']))
print(alterList([1, 2, 3],['a', 'b', 'c', 'd', 'e'] ))
print(alterList([1, 2, 3, 4, 5], ['a', 'b'] ))


# In[ ]:




