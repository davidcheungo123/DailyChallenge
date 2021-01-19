#!/usr/bin/env python
# coding: utf-8

# In[9]:


def addSubtract(strInput, shift):
    #shift is 1 when add positive otherwise 0
    if shift == 1:
        num = int(strInput[0])
    else:
        num = -int(strInput[0])
    next_strInput = strInput[1:]
    if len(next_strInput) ==0:
        return num
    
    if next_strInput[0:4] == "plus":
        num += addSubtract(next_strInput[4:], 1)
    elif next_strInput[0:5] == "minus":
        num += addSubtract(next_strInput[5:], 0)
        
    return num
        
print(addSubtract("1plus2plus3minus4",1))
print(addSubtract("2minus6plus4plus7",1))


# In[ ]:




