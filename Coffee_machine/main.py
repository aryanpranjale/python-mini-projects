# ask for what kind of coffee the user wants (latte, black coffee, etc), with hidden menu
# hidden menu -> report, or off 
# if report is entered, it shows the amount of ingredient left, amount each type of coffee sold, 
# and money till now
# quarter = $0.25
# dime = $0.10
# nickel = $0.05
# penny = $0.01
import data
def money_total():
    money_data = data.money
    quarter_t= (money_data["quarter"]*0.25) 
    dime_t= money_data["dime"]* 0.10
    nickel_t = money_data["nickel"]*0.05
    penny_t = money_data["penny"]*0.01

    total_money = quarter_t + dime_t +nickel_t+ penny_t
    total_money= round(total_money,2)
    return total_money
def take_money(cost_of_coffee):
    
    paid_money = 0
    print(f"The amount to pay -> {cost_of_coffee}")
    while True:
        try:
            quarters = int(input("How many quarters?:\n"))*0.25
            dime = int(input("How many dimes?:\n"))*0.10
            nickel = int(input("How many nickels?:\n"))*0.05
            penny = int(input("How many pennys?:\n"))*0.01
            coin_quantity= [quarters,dime,nickel,penny]
            if any(quantity <0 for quantity in coin_quantity):
                print("Enter positive coin quantity input")
            else:
                money_taken = round(quarters + dime + nickel + penny , 2)
                paid_money += money_taken
                money_difference= paid_money - cost_of_coffee
                if money_difference < 0:
                    print(f"Add more {money_difference*-1:.2f} to recive the coffee")
                    
                    
                elif money_difference>0:
                    print(f"You paid extra, here is your ${money_difference:.2f}")
                    paid_money = cost_of_coffee
                    return paid_money
                else:
                    return paid_money 
        except ValueError:
            print("Enter only numbers! and try again!")
        
def coffee_pick():
    selection = True
    while selection:
        print("Welcome! What would you like to have?")
        print('''   :Coffee Options:  
        1. Espresso     -> $ 1.50
        2. Latte        -> $ 2.50
        3. Cappuccino   -> $ 3.00
        ''')

        selected_coffee = input("Enter the number or Name of the coffee:\n").strip().title()
        coffee_dic= next(
            (coffee for coffee in data.coffee_types 
             if selected_coffee in coffee["name"]  ) ,
             None
              )
        
        if coffee_dic == None:
            if selected_coffee== "Off":
                return False
            elif selected_coffee == "Report":
                report_data= data.report
                money_made= money_total()
                print(f'''
                Milk: {report_data["milk"]}ml 
                Water: {report_data["water"]} ml
                Sugar: {report_data["sugar"]}g
                Latte sold: {report_data["Latte"]}
                Cappuccino sold:{report_data["Cappuccino"]}
                Espresso sold:{report_data["Espresso"]}
                Money made: {report_data["total_money"]}''')

            else: 
                print("Try entering \n1 for espresso \n2 for latte \n3 for cappuccino")
        else:
            return coffee_dic

def coffee_machine():
    mach_running= True
    
    while mach_running:   
        stop = 0
        selected_coffee= coffee_pick()
        if selected_coffee == False:
            mach_running= False
        else:
            ingredient = ["milk","water","sugar"]
            report_update = data.report 
            for key in selected_coffee :
                if key in ingredient :
                    if report_update[key]-selected_coffee[key] <0:
                        print(f"There isnt enough {key}")
                        stop = 1
                        break  
            if stop == 0 :
                askmoney = take_money(selected_coffee["price"])
                for key in ingredient:
                    report_update[key] -= selected_coffee[key]
                
                report_update["total_money"] += askmoney
                report_update[selected_coffee["name"][0]] += 1
            
    
coffee_machine()
