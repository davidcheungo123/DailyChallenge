#!/usr/bin/env python
# coding: utf-8

# In[1]:


def elementFormat(inputStr):
    formatList = inputStr.split(":")
    
    return "(" + formatList[1] + "," + formatList[0] + ")"

def changeFormat(inputStr):
    formatList = inputStr.split(";")
    finalStr = ""
    for element in formatList:
        finalStr += elementFormat(element)
        
    return finalStr

changeFormat("Alfred:Black;Carey:Drake;Elena:Ferguson;Georgina:Harrison")
        


# In[ ]:




