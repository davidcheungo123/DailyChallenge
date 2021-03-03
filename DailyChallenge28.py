#!/usr/bin/env python
# coding: utf-8

# In[2]:


def check_almost(list1, list2):
    counter = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            counter +=1
    return counter

def recover(listInput):
    
    listInput_copy = listInput.copy()
    listInput_copy.reverse()
    
    listInput_copy = listInput[:len(listInput)//2] + listInput_copy[len(listInput)//2:]
        
    return listInput_copy

def almost_palindrome(inputStr):
    sList = list(inputStr)
    sList_correct = recover(sList)
    counter = check_almost(sList, sList_correct)
    if counter ==1:
        return True
    else:
        return False  


# In[3]:


almost_palindrome("abcdcbg")


# In[4]:


almost_palindrome("abccia")


# In[5]:


almost_palindrome("abcdaaa")


# In[6]:


almost_palindrome("1234312")


# In[ ]:




