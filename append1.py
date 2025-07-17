#!/usr/bin/env python
# coding: utf-8

# In[ ]:


with open("ex1.txt","a+") as f:
    f.write("three \n")
    f.seek(0)
    data=f.read()
    print("current_data:",data)

