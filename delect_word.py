#!/usr/bin/env python
# coding: utf-8

# In[ ]:


with open("ex1.txt","r") as f:
    lines=f.readlines()
with open("ex1.txt","w") as f:
    for line in lines:
        if line.strip() !="two":
            f.write(line)

