#!/usr/bin/env python
# coding: utf-8

# In[6]:


def splitFunction(strInput):
    s = ""
    strList = []
    for counter , string in enumerate(strInput):
        s += string
        if counter % 2 ==0 and counter + 1 == len(strInput):
            s+= "?"
        if len(s) == 2:
            strList.append(s)
            s = ""
            
    return strList

print(splitFunction("abcdef"))
print(splitFunction("abcdefg"))

        


# In[ ]:





# In[ ]:




