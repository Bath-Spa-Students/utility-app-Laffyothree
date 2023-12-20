import time
import sys

crdts = 0  # Where user's inserted credits/cash will get stored.
stock = 5  # Item stocks variables.
stock1 = 4
stock2 = 3
stock3 = 2
stock4 = 1

def print_slow(str):  # Adding typewriter effect on the text.
        for char in str:
            time.sleep(.08)
            sys.stdout.write(char)
            sys.stdout.flush()

print_slow ("\n\033[1mHELLO THERE!\033[0m")  # Adding bold effect on the text to make it more readeable.
time.sleep(.5)  # A time transition between text printing.
print_slow ("\n\033[1mWELCOME TO LA's VENDING MACHINE :)\033[0m")  # A "welcome" message for the user :)


vm_items = {  # A nested dictionary storing each item's name, code, price, and stocks.
  "Snacks" : {  # Items are organized into different categories.
    "Name" : "Cheetos Crunchy Cheese Flavour",
    "Code" : "A01",
    "Price": 7.00,
    "Stock": 5,

    "Name1" : "Lay's Classic Potato Chips",
    "Code1" : "A02",
    "Price1": 7.00,
    "Stock1": 4,

    "Name2" : "Pringles Chips",
    "Code2" : "A03",
    "Price2": 7.00,
    "Stock2": 3,
  },

  "Drinks" : {
    "Name" : "Diet Coke",
    "Code" : "B01",
    "Price": 5.00,
    "Stock": 2,

    "Name1" : "Diet Mountain Dew",
    "Code1" : "B02",
    "Price1": 5.00,
    "Stock1": 1,

    "Name2" : "Diet Pepsi",
    "Code2" : "B03",
    "Price2": 5.00,
    "Stock2": 2,
  },

  "Sweets" : {
    "Name" : "Hershey's Chocolate Bar",
    "Code" : "C01",
    "Price": 6.00,
    "Stock": 3,

    "Name1" : "M&Ms Milk Chocolate",
    "Code1" : "C02",
    "Price1": 6.00,
    "Stock1": 4,

    "Name2" : "Snickers Bar",
    "Code2" : "C03",
    "Price2": 6.00,
    "Stock2": 5, 
  }
}

time.sleep(.05)
def display_list():
    for item, item_info in vm_items.items():  # For loop to properly showcase item names, codes, prices, and stocks.
        print ("\n--------------------------------------------------------------")
        print ("\nCategory: " + item)
        print (f"""\n\tItem Name: {item_info['Name']}           
            Price: ${item_info['Price']}
             Code: {item_info['Code']}
            Stock: {item_info['Stock']}""")
        print (f"""\n\tItem Name: {item_info['Name1']}           
            Price: ${item_info['Price1']}
             Code: {item_info['Code1']}
            Stock: {item_info['Stock1']}""")
        print (f"""\n\tItem Name: {item_info['Name2']}           
            Price: ${item_info['Price2']}
             Code: {item_info['Code2']}
            Stock: {item_info['Stock2']}""")
       
display_list()
print ("\n--------------------------------------------------------------")

time.sleep(3)
crdts1 = float(input("\nInsert banknotes or coins: $"))  # User input for them to insert any amount of credits/cash.
crdts += crdts1 


def purchasing_process(value):  # Tracking amount of user money that has been spent.
     global crdts  # Giving use of the variable "crdts" beyond the current scope.
     if float(crdts) >= value:
          crdts -= value

def item_stock(num):  # Tracking the number of stocks after every purchase.
     global stock  # Giving use of the variable "stock" beyond the current scope.
     if float(stock) >= num:
        stock -= num
        print ("There are only " + str(stock) + " stock/s left for this item.")

def item_stock1(num1):
     global stock1
     if float(stock1) >= num1:
        stock1 -= num1
        print ("There are only " + str(stock1) + " stock/s left for this item.")

def item_stock2(num2):
     global stock2
     if float(stock2) >= num2:
        stock2 -= num2
        print ("There are only " + str(stock2) + " stock/s left for this item.")

def item_stock3(num3):
     global stock3
     if float(stock3) >= num3:
        stock3 -= num3
        print ("There are only " + str(stock3) + " stock/s left for this item.")

def item_stock4(num4):
     global stock4
     if float(stock4) >= num4:
        stock4 -= num4
        print ("There are only " + str(stock4) + " stock/s left for this item.")


def buying_process():  # The main process of the vending machine program.
    global crdts
    activate_selection = True
    while activate_selection: # While loop to allow users to select and purcahse items.
        print_slow (f"\n\033[1mYour available credit/s is ${str(crdts)} \033[0m")  # Displays the user's remaining balance.
        time.sleep(.8)  
        item_selection = input("\nEnter the code of the item you desire to purchase: ")

        if item_selection == 'A01':
            if stock < 1:  # Informs the user when the item variable reaches zero.
                print ("\nThis item is now currently out of stock.")

            elif crdts == 0 or crdts <= 7.00:  # Informs the user that they don't have sufficient balance.
                print_slow ("\n\033[1mYour credit balance is not enough, item selection did not proceed.\033[0m") 
                time.sleep(.8)
                adding_credits = input("\nWould you like to add more banknotes or coins? Put proceed to continue or any key to cancel: ") 
                 # ^ An option for the user to insert additional credit when the balance is not enough.

                if adding_credits == 'proceed':
                    crdts2 = float(input("\nInsert banknotes or coins: $"))
                    crdts += crdts2
        
            else:
                print_slow ("\n\033[1mOne Cheetos Crunchy Cheese Flavour has been dispensed.\033[0m")  # Informs the user that the product/s has been dispensed.
                print ("\nCheetos Crunchy Cheese Flavour and Diet Pepsi is a dope combo!")  # Offering suggestions for the user to try.
                purchasing_process(7.00)  # Deducts the price of the item to the user's balance.
                str(item_stock (1))  # Updates the item stock after every purchase that's been made.

        elif item_selection == 'A02':
            if stock1 < 1:
                print ("\nThis item is now currently out of stock.")

            elif crdts == 0 or crdts <= 7.00:
                print_slow ("\n\033[1mYour credit balance is not enough, item selection did not proceed.\033[0m")
                time.sleep(.8)
                adding_credits = input("\nWould you like to add more banknotes or coins? Put proceed to continue or any key to cancel: ")

                if adding_credits == 'proceed':
                    crdts2 = float(input("\nInsert banknotes or coins: $"))
                    crdts += crdts2
        
            else:
                print_slow ("\n\033[1mOne Lay's Classic Potato Chips has been dispensed.\033[0m")
                print ("\nLay's Classic Potato Chips and Diet Mountain Dew is a dope combo!")
                purchasing_process(7.00)
                str(item_stock1 (1))

        elif item_selection == 'A03':
            if stock2 < 1:
                print ("\nThis item is now currently out of stock.")

            elif crdts == 0 or crdts <= 7.00:
                print_slow ("\n\033[1mYour credit balance is not enough, item selection did not proceed.\033[0m")
                time.sleep(.8)
                adding_credits = input("\nWould you like to add more banknotes or coins? Put proceed to continue or any key to cancel: ")

                if adding_credits == 'proceed':
                    crdts2 = float(input("\nInsert banknotes or coins: $"))
                    crdts += crdts2
        
            else:
                print_slow ("\n\033[1mOne Pringles Chips has been dispensed.\033[0m")
                print ("\nPringles Chips and Diet Coke is a dope combo!")
                purchasing_process(7.00)
                str(item_stock2 (1))


        elif item_selection == 'B01':
            if stock3 < 1:
                print ("\nThis item is now currently out of stock.")

            elif crdts == 0 or crdts <= 5.00:
                print_slow ("\n\033[1mYour credit balance is not enough, item selection did not proceed.\033[0m")
                time.sleep(.8)
                adding_credits = input("\nWould you like to add more banknotes or coins? Put proceed to continue or any key to cancel: ")

                if adding_credits == 'proceed':
                      crdts2 = float(input("\nInsert banknotes or coins: $"))
                      crdts += crdts2
        
            else:
                print_slow ("\n\033[1mOne Diet Coke has been dispensed.\033[0m")
                print ("\nDiet Coke and Snickers Bar is a dope combo!")
                purchasing_process(5.00)
                str(item_stock3 (1))

        elif item_selection == 'B02':
            if stock4 < 1:
                print ("\nThis item is now currently out of stock.")

            elif crdts == 0 or crdts <= 5.00:
                print_slow ("\n\033[1mYour credit balance is not enough, item selection did not proceed.\033[0m")
                time.sleep(.8)
                adding_credits = input("\nWould you like to add more banknotes or coins? Put proceed to continue or any key to cancel: ")

                if adding_credits == 'proceed':
                    crdts2 = float(input("\nInsert banknotes or coins: $"))
                    crdts += crdts2
        
            else:
                print_slow ("\n\033[1mOne Diet Mountain Dew has been dispensed.\033[0m")
                print ("\nDiet Mountain Dew and M&M's Milk Chocolate is a dope combo!")
                purchasing_process(5.00)
                str(item_stock4 (1))
    
        elif item_selection == 'B03':
            if stock3 < 1:
                print ("\nThis item is now currently out of stock.")

            elif crdts == 0 or crdts <= 5.00:
                print_slow ("\n\033[1mYour credit balance is not enough, item selection did not proceed.\033[0m")
                time.sleep(.8)
                adding_credits = input("\nWould you like to add more banknotes or coins? Put proceed to continue or any key to cancel: ")

                if adding_credits == 'proceed':
                    crdts2 = float(input("\nInsert banknotes or coins: $"))
                    crdts += crdts2
        
            else:
                print_slow ("\n\033[1mOne Diet Pepsi has been dispensed.\033[0m")
                print ("\nDiet Pepsi and Hershey's Chocolate Bar is a dope combo!")
                purchasing_process(5.00)
                str(item_stock3 (1))

    
        elif item_selection == 'C01':
            if stock2 < 1:
                print ("\nThis item is now currently out of stock.")

            elif crdts == 0 or crdts <= 6.00:
                print_slow ("\n\033[1mYour credit balance is not enough, item selection did not proceed.\033[0m")
                time.sleep(.8)
                adding_credits = input("\nWould you like to add more banknotes or coins? Put proceed to continue or any key to cancel: ")

                if adding_credits == 'proceed':
                    crdts2 = float(input("\nInsert banknotes or coins: $"))
                    crdts += crdts2
        
            else:
                print_slow ("\n\033[1mOne Hershey's Chocolate Bar has been dispensed.\033[0m")
                print ("\nHershey's Chocolate Bar and Diet Pepsi is a dope combo!")
                purchasing_process(6.00)
                str(item_stock2 (1))

        elif item_selection == 'C02':
            if stock1 < 1:
                print ("\nThis item is now currently out of stock.")

            elif crdts == 0 or crdts <= 6.00:
                print_slow ("\n\033[1mYour credit balance is not enough, item selection did not proceed.\033[0m")
                time.sleep(.8)
                adding_credits = input("\nWould you like to add more banknotes or coins? Put proceed to continue or any key to cancel: ")

                if adding_credits == 'proceed':
                    crdts2 = float(input("\nInsert banknotes or coins: $"))
                    crdts += crdts2
        
            else:
                print_slow ("\n\033[1mOne M&M's Milk Chocolate has been dispensed.\033[0m")
                print ("\nM&M's Milk Chocolate and Diet Mountain Dew is a dope combo!")
                purchasing_process(6.00)
                str(item_stock1 (1))
    
        elif item_selection == 'C03':
            if stock < 1:
                print ("\nThis item is now currently out of stock.")

            elif crdts == 0 or crdts <= 6.00:
                print_slow ("\n\033[1mYour credit balance is not enough, item selection did not proceed.\033[0m")
                time.sleep(.8)
                adding_credits = input("\nWould you like to add more banknotes or coins? Put proceed to continue or any key to cancel: ")

                if adding_credits == 'proceed':
                    crdts2 = float(input("\nInsert banknotes or coins: $"))
                    crdts += crdts2
        
            else:
                print_slow ("\n\033[1mOne Snickers Bar has been dispensed.\033[0m")
                print ("\nSnickers Bar and Diet Coke is a dope combo!")
                purchasing_process(6.00)
                str(item_stock (1))

        else:
            print ("Ivalid item code.")  # Displayed when invalid code has been entered.

        time.sleep(.8)
        loop = input("\nWould you like to purchase another items? Type yes to proceed or done to quit: ")  # An option for the user if they want to purchase more product/s.

        if loop == 'done':  # To finish the purchase and end the program.
            activate_selection = False
            print_slow (f"\n\033[1mThe total of your change is ${float(crdts)} \033[0m")
            print_slow ("\nThank you for purchasing from \033[1mLA's VENDING MACHINE :)\033[0m")
            print_slow ("\n\033[1mENJOY YOUR SNACKS!\033[0m")  # Appreciation message for the user :)
            print ("\n")

buying_process()
