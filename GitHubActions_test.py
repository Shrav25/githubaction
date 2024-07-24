#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pytest
from GitHubActions import multiply


# In[ ]:


def test_multiply():
    assert multiply(1,1) == 1
    assert multiply(10,10) == 100
    assert multiply(12,10) == 120
    assert multiply(12,12) == 111
    
if __name__ == "__GitHubActions__":
    GitHubActions_test.GitHubActions()

