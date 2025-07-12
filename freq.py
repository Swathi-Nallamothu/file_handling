#!/usr/bin/env python
# coding: utf-8

# In[7]:


filename=input("enter the filename:")
with open(filename) as file:
    text=file.read()
    l=input("enter a char:")
    c=0
    for char in text:
        if char==l:
            c+=1
print(l,"appears",c,"times in the file")


# In[ ]:




