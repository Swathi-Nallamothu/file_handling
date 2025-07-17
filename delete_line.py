#!/usr/bin/env python
# coding: utf-8

# In[8]:


idel=input("enter exact line")
with open("ex1.txt","r") as f:
    lines=f.readlines()
with open("ex1.txt","w") as f:
    for line in lines:
        if line.strip() != idel.strip():
            f.write(line)


# In[ ]:




