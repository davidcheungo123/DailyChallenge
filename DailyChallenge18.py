#!/usr/bin/env python
# coding: utf-8

# In[15]:


def checkifpalindromes(inputList):
    list2 = inputList.copy()
    list2.reverse()
    
    if inputList == list2:
        return True
    else:
        return False
    
    
def stringtify(inputList):
    finalStr = ""
    for i in inputList:
        finalStr += str(i)
    
    return finalStr


def palindromes(inputNum):
    inputNum = str(inputNum)
    inputNum = list(inputNum)
    
    NumList = []
    for num in inputNum:
        NumList.append(int(num))
    
    finalList = []
    for i in range(len(NumList)):
        for j in range(i,len(NumList)+1):
            if checkifpalindromes(NumList[i:j]) and len(NumList[i:j]) >=2:
                finalList.append(stringtify(NumList[i:j]))
            else:
                continue
                
    
                
    
                
    return finalList

print(palindromes(34322122))
            
            


# In[ ]:




