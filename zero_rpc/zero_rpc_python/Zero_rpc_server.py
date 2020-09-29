#!/usr/bin/env python
# coding: utf-8

# # Install zerorpc if not installed

# In[ ]:


#!pip install zerorpc


# # Import necessary libraries

# In[ ]:


import zerorpc
import time


# # Start the server

# In[ ]:


class HelloRPC(object):
    def hello(self, message):
        return f'Server received:{str(message)} from client and sent back at {str(time.time())} which takes {str(time.time() - message)}'

s = zerorpc.Server(HelloRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()


# Manipulation to the data can be the done received. Instead of printing the message, simply perform calculations on the data.
# 
# Restart the kernel if issues with closing
# 
# For further types of messages streams, go to [zerorpc](http://www.zerorpc.io/)

# In[ ]:




