#!/usr/bin/env python
# coding: utf-8

# In[1]:


def uncensor(inputSentence, inputCensored):
    ans = ""
    for char in inputSentence:
        corrected = char
        if corrected == "*":
            corrected = inputCensored[0]
            inputCensored = inputCensored[1:]
        ans += corrected
    return ans


# In[2]:


uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo")


# In[3]:


uncensor("abcd", "")


# In[4]:


uncensor("*PP*RC*S*", "UEAE")


# In[ ]:




