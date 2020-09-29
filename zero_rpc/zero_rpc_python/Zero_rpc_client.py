#!/usr/bin/env python
# coding: utf-8

# # Install zerorcp if not installed

# In[1]:


#!pip install zerorpc


# # Import necessary libraries

# In[2]:


import zerorpc
import time
import random


# # Receive 1 message

# In[3]:


c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")
print(f'At {time.time()} client sent a message.\n{c.hello(time.time())}\n')


# # Receive 10 messages

# In[4]:


for i in range(10):
    c = zerorpc.Client()
    c.connect("tcp://127.0.0.1:4242")
    print(f'{i+1})At {time.time()} client sent a message.\n{c.hello(time.time())}\n')


# For further types of messages streams, go to [zerorpc](http://www.zerorpc.io/)

# In[ ]:




