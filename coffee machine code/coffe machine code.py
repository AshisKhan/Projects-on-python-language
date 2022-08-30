MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    
}
profit=0
def resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
           print("sorry ingredients are not available")
           return False
        return True

def process_coins():
    print("please insert coins")
    rupees=int(input("quarters:  "))*0.25
    rupees+=int(input("dimes:  "))*0.10
    rupees+=int(input("nickel:  "))*0.05
    rupees+=int(input("pennis:  "))*0.01
    return rupees

def check_transaction_sucessful(money,drink_cost):
    if money>=drink_cost:
        change=money-drink_cost
        print("transaction is sucessfulland enjoy with your cofee")
        print(f"your change is {change}")
        global profit
        profit+=drink_cost
        return True
    else:
        print("sorry!!, that is not enough money")
        return False

def make_coffe(order_ingredients,drink_name):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on=True
while is_on:
    choice=input("do you want to close the machine then press off and to continue press on")
    
    if choice=="off":
        is_on=False
    elif choice=="on":
         print("available qingredients are")
         print(f"Water: {resources['water']}ml")
         print(f"Milk: {resources['milk']}ml")
         print(f"Coffee: {resources['coffee']}g")
         print(f"Money: ${profit}")
         coffe=input("what do you like?? (espresso/latte/cappuccino)")
         if resource_sufficient(MENU[coffe]["ingredients"]):
             payment=process_coins()
             if check_transaction_sucessful(payment,MENU[coffe]["cost"]):
                 make_coffe(MENU[coffe]["ingredients"],coffe)
            
        
            
            
    
    