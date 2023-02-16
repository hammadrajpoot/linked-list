#!/usr/bin/env python
# coding: utf-8

# In[4]:


mylist = list(range(0,10))


# In[29]:


mylist


# In[30]:


mylist


# In[31]:


mylist.append(15)


# In[32]:


mylist


# In[33]:


mylist.insert(17,15)
mylist


# In[34]:


mylist.insert(7,789)
mylist


# In[35]:


mylist.pop()
mylist


# In[36]:


mylist.pop()
mylist


# In[37]:


mylist.remove(789)
mylist


# In[38]:


mylist


# In[43]:


mylist.remove(4)


# In[44]:


mylist


# In[45]:


from collections import deque


# In[46]:


ll = deque()


# In[47]:


ll


# In[48]:


ll.append(54)


# In[49]:


ll


# In[50]:


ll.insert(47,57)
ll


# In[51]:


ll.appendleft(45)
ll


# In[52]:


ll.pop()
ll


# In[53]:


ll.remove(54)
ll


# In[54]:


queue =deque()


# In[55]:


for i in range(0,10):
    queue.append(i)
    print(queue)


# In[58]:


for i in range(len(queue)):
    queue.popleft()
    print(queue)


# In[59]:


stack = deque()


# In[60]:


for i in range(0,10):
    stack.append(i)
    print(stack)


# In[61]:


for i in range(0,10):
    stack.appendleft(i)
    print(stack)


# In[62]:


for i in range(0,10):
    stack.popleft()
    print(stack)


# In[63]:


for i in range(len(stack)):
    stack.popleft()
    print(stack)


# In[ ]:




