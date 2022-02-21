#!/usr/bin/env python
# coding: utf-8

# In[1]:


def take_coin():
    fund = 0
    penny = 0
    dime = 0
    nickel = 0
    quarter = 0
    
    while True:
        try:
            penny = int(input("How many pennies would you like to insert?: "))
        except ValueError:
            print("Please input only an integer.")
        else:
            break
            
    while True:
        try:
            dime = int(input("How many dimes would you like to insert?: "))
        except ValueError:
            print("Please input only an integer.")
        else:
            break
    
    while True:
        try:
            nickel = int(input("How many nickel would you like to insert?: "))
        except ValueError:
            print("Please input only an integer.")
        else:
            break
            
    while True:        
        try:
            quarter = int(input("How many quarter would you like to insert?: "))
        except ValueError:
            print("Please input only an integer.")
        else:
            break
        
    fund = (penny*0.01)+(dime*0.1)+(nickel*0.05)+(quarter*0.25)
    return fund


# In[ ]:




