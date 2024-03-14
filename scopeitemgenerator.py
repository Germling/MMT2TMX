#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import openAI
import pandas
import sys
import re
import streamlit as st
import pandas as pd
import numpy as np
st.title('Scope Item Generator')


# In[2]:

#The function reads scope items from user input
def extract_scope_items_from_input():
    # Prompt the user for input
    content = input("Please enter the scope items; don't worry, I can do the formatting: ")
    
    # Define the regular expression pattern for a three-digit alphanumeric string
    pattern = r'\b(?![A-Z]{3})[A-Z0-9]{3}\b'
    
    # Find all matches of the pattern in the content
    matches = re.findall(pattern, content)
    
    # Use a set to get unique matches
    unique_matches = set(matches)
    
    # Convert the set to a sorted list
    sorted_unique_matches = sorted(list(unique_matches))
    
    return sorted_unique_matches

# Get unique scope items from user input
unique_scope_items = extract_scope_items_from_input()
print(unique_scope_items)


# In[7]:


def print_xml(unique_scope_items):
    for index, item in enumerate(unique_scope_items):
        xml_string = (f'<ph conkeyref="loio7b7f550aacf543fd93542078bb9ed368/{item}_id"/> '
                      f'(<ph conkeyref="loio7b7f550aacf543fd93542078bb9ed368/{item}_desc"/>)')
        # Check if the current item is the last one in the list
        if index == len(unique_scope_items) - 1:
            # If it's the last item, don't add a comma
            print(xml_string, end='')
        else:
            # If it's not the last item, add a comma after the string
            print(xml_string, end=', ')


# In[8]:


print_xml(unique_scope_items)


# In[ ]:
