#!/usr/bin/env python
# coding: utf-8

# In[1]:


##This is for daily challenge 2

def lose_weight(gender, weight, duration):
    if gender.upper() not in ["M", "F"]:
        return "You inputed a wrong gender"
    if weight <= 0 or type(weight) != int:
        return "You inputed a wrong weight"
    if duration <= 0 or type(duration) != int:
        return "You inputed a wrong duration"
    
    if gender.upper() == "M":
        return weight*(1-0.015)**duration
    else:
        return weight*(1-0.012)**duration
    
print(lose_weight("M", 70, 3))


# In[ ]:




