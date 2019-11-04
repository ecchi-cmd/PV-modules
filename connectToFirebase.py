#!/usr/bin/env python
# coding: utf-8

# In[3]:


from firebase import firebase
firebase= firebase.FirebaseApplication('https://projetpiste-46a47.firebaseio.com/', None)
result = firebase.get('/0', None)
print(result)

