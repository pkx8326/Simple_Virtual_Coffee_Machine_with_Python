# Simple_Virtual_Coffee_Machine_with_Python
This project demonstrates Python's modularity capability. This repository hosts a Python code for a simple virtual coffee machine. It is a coin-operated machine that can dispense espresso, latte, and cappuccino at different prices. 

The machine principle is simple:
1. The customer chooses between the three choices of the coffees.
2. The machine checks its resources to make sure that it has enough raw material to make that coffee. If there's not enough raw material, it tells the customer and the customer chooses a different choice or stop ordering.
3. If there's enough raw material to make the coffee, the machine asks for coins.
4. The customer insert coins.
5. The machine checks if there're enough coins for the cost of that coffee, if there's not enough coins, the machine return all the coins and the customer needs to insert them again.
6. If there're enough coins, the machine makes and gives the coffee to the customer. The machine also collect the coins given by the customers.
7. At the process of choosing a coffee, the customer can also choose to make the machine display its status, including all the raw materials left in the machine and the value of the coins it has collected so far.

The following picture shows how the program interacts with users:
![image](https://user-images.githubusercontent.com/65524471/154978845-83a15c4a-46dd-4b59-9d9e-6989d81cc5bc.png)
