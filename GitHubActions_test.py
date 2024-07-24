#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pytest
from main import multiply


# In[ ]:


def test_multiply():
    assert multiply(1,1) == 1
    assert multiply(10,10) == 100
    assert multiply(12,10) == 120
    
if __name__ == "__main__":
    GitHubActions_test.main()

