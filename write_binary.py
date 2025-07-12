#!/usr/bin/env python
# coding: utf-8

# In[1]:


with open("sample_binary.bin","wb") as file:
    data=b'\x48\x65\x6c\x6c\x6F'
    file.write(data)


# In[ ]:




