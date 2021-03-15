#!/usr/bin/env python
# coding: utf-8

# In[29]:


import string
def helperFunction(strlen , replaceStr):
    return replaceStr * strlen
    

def censor_string(sentence, censorList, replaceStr):
    clear = ""
    for ele in sentence:
        if ele not in string.punctuation:
            clear += ele
    clearInput = clear
    inputList = clearInput.split()
    ans = ""
    for index, ele in enumerate(inputList):
        if index != len(inputList) -1:
            if ele in censorList:
                ans += helperFunction(len(ele), replaceStr)
            else:
                ans += ele
            ans += " "
        else:
            if ele in censorList:
                ans += helperFunction(len(ele), replaceStr)
            else:
                ans += ele     
    ans += sentence[-1]
    return ans
        


# In[30]:


censor_string("Today is a Wednesday!", ["Today", "a"], "-")


# In[31]:


censor_string("The cow jumped over the moon.", ["cow", "over"], "*")


# In[32]:


censor_string("Why did the chicken cross the road?", ["did", "chicken", "road"], "*")


# In[ ]:





# In[ ]:




