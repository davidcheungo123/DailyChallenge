#!/usr/bin/env python
# coding: utf-8

# In[6]:


def phoneNumber(listInput):
    
    if len(listInput) != 11:
        return "Wrong format is inputed"
    elif 8 not in listInput or 5 not in listInput or 2 not in listInput:
        return "Wrong format is inputed"
    else:
        strOutput = "+852 "
        listInput.remove(8)
        listInput.remove(5)
        listInput.remove(2)
        
        while len(listInput) != 0:
            for num in listInput:
                if len(strOutput) == 5:
                    if num == 2 or num == 3 or num == 5 or num ==6 or num == 7 or num ==9:
                        strOutput += str(num)
                        listInput.remove(num)
                    else:
                        continue
            if len(strOutput) > 5:
                for num in listInput:
                    strOutput += str(num)
                    listInput.remove(num)
            else:
                return "Invalid format"
                    
        return strOutput
        
phoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1])
        


# In[ ]:




