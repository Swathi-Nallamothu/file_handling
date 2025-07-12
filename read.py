#!/usr/bin/env python
# coding: utf-8

# In[6]:


file=open("sample.txt","r")
data=file.read()#read data from the existed file
print(data)


# In[8]:


file=open("sample.txt","r")
data=file.readline() # prints 1st line of the file
print(data)


# In[ ]:


file=open("sample.txt","r")
for line in file:
    print(line.strip())
data=file.


# In[ ]:




