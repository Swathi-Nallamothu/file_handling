#!/usr/bin/env python
# coding: utf-8

# In[25]:


with open("file1.txt",'w') as f:
    f.write("swathi nallamothu")
with open("file1.txt",'r+') as f: #arises past data 
    data=f.read()
    print("previous:",data)
    new_data=data.replace("nallamothu","chinnarao")
    f.seek(0)# upto the index 
    f.write(new_data)
    f.truncate()# it will continues the updated value with the exited from seek() upto the index 
with open("file1.txt",'r') as f:
    print("latest:",f.read())


# In[ ]:





# In[ ]:




