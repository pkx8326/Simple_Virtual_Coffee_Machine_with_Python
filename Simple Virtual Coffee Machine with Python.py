#!/usr/bin/env python
# coding: utf-8

# In[1]:


import app_data
from take_coin import take_coin


# In[8]:


value = 0 #the monetary value supplied by a customer

print(f'''Hello! This is a virtual coin-operated coffee machine!
we offer {app_data.coffee[0]['type']} for ${app_data.coffee[0]['cost']},
{app_data.coffee[1]['type']} for ${app_data.coffee[1]['cost']}, and
{app_data.coffee[2]['type']} for ${app_data.coffee[2]['cost']}.\n''')

order_again = "y"
while order_again in ["Y", "y"]:
    order_again = ""
    command_type = ''

    
    while True:
        try:
            while command_type not in ['0','1','2','3']:
                command_type = input(f'''What would you like? 
type "1" for {app_data.coffee[0]['type']}, "2" for {app_data.coffee[1]['type']}, and "3" for {app_data.coffee[2]['type']},
or type "0" for the machine\'s status report: ''')
        except ValueError:
            print("Please input only valid integer between 0 - 3.")
        else:
            if command_type == '0':
                print(f"The machine now has {app_data.resources['water']} ml of water, {app_data.resources['coffee']} g of coffee, {app_data.resources['milk']} ml of milk, and ${app_data.resources['coin_value']} worth of coins.")
                command_type = ''      
            else:
                print(f"You ordered a shot of {app_data.coffee[int(command_type)-1]['type']} for ${app_data.coffee[int(command_type)-1]['cost']}.")
                #Check the resources
                if app_data.resources['coffee'] < app_data.coffee[int(command_type)-1]['coffee']:
                    print("Sorry, we don't have enough coffee ❌")
                    break
                elif app_data.resources['water'] < app_data.coffee[int(command_type)-1]['water']:
                    print("Sorry, we don't have enough water ❌") 
                    break
                elif app_data.resources['milk'] < app_data.coffee[int(command_type)-1]['milk']:
                    print("Sorry, we don't have enough milk ❌")
                    break
                else:
                    value = take_coin()
                    while value < app_data.coffee[int(command_type)-1]['cost']:
                        print(f"You don't have enough funds. ${value} is returned. Please insert coin again:")
                        value = take_coin()
                        
                    if value > app_data.coffee[int(command_type)-1]['cost']:
                        print(f"Here is your change of ${round(value - app_data.coffee[int(command_type)-1]['cost'],2)}")
                        print(f"Enjoy your hot {app_data.coffee[int(command_type)-1]['type']} ☕")
                        app_data.resources['water'] = app_data.resources['water'] - app_data.coffee[int(command_type)-1]['water']
                        app_data.resources['coffee'] = app_data.resources['coffee'] - app_data.coffee[int(command_type)-1]['coffee']
                        app_data.resources['milk'] = app_data.resources['milk'] - app_data.coffee[int(command_type)-1]['milk']
                        app_data.resources['coin_value'] += app_data.coffee[int(command_type)-1]['cost']
                        command_type = ''
                        break
                    else:
                        print(f"Enjoy your hot {app_data.coffee[int(command_type)-1]['type']} ☕")
                        app_data.resources['water'] = app_data.resources['water'] - app_data.coffee[int(command_type)-1]['water']
                        app_data.resources['coffee'] = app_data.resources['coffee'] - app_data.coffee[int(command_type)-1]['coffee']
                        app_data.resources['milk'] = app_data.resources['milk'] - app_data.coffee[int(command_type)-1]['milk']
                        app_data.resources['coin_value'] += app_data.coffee[int(command_type)-1]['cost']
                        command_type = ''
                        break
    
    while order_again not in["Y", "y", "N", "n"]:
        order_again = input("Order another drink? Y/N: ")
        if order_again in ["N","n"]:
            print("Thank you for enjoying our coffee 💖")
            print(f"The machine now has {app_data.resources['water']} ml of water, {app_data.resources['coffee']} g of coffee, {app_data.resources['milk']} ml of milk, and ${app_data.resources['coin_value']} worth of coins.")

