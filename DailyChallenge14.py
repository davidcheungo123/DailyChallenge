#!/usr/bin/env python
# coding: utf-8

# In[13]:


def addList(listInput):
    
    list1 = listInput[:int(len(listInput)/2)]
    list2 = listInput[int(len(listInput)/2):]
    
    finalList = []
    
    for item1, item2 in zip(list1, list2):
        finalList.append(item1 + item2)
    
    if len(list2) > len(list1):
        finalList.append(list2[-1])
    
    return finalList

print(addList([1, 2, 3, 4, 5, 6, 7]))
print(addList([1,2,3,4,5,6]))


# In[ ]:




