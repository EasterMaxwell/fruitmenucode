print("WELCOME TO MAX SHOPPING MENU")
# THE BELOW BLOCK OF CODE WILL PRINT OUT THE LIST OF FRUITS IN TABULAR FORM
print('___paw - paw ____|____water melon___|___garden egg___')
print("___ apple _______|_______onion______|___beans seed___")
print("____pineapple___ |_______mango______|___melon seed___")
print("____banana___    |______grapes_____ |___cherry seed__")
print("THERE YOU HAVE IT!")
# TO GET USER INPUT
fruit_input = input("enter in any fruit in the above menu : ")
# A POOL OF CONTROL STATEMENT TO CHECK FOR A PARTICULAR FRUIT AND THEN PRINT IT'S PRICE
if fruit_input == "banana":
    print("the price of banana is : $200"
          " and you can find it in block 17")

elif fruit_input == "grapes":
    print("the price of grapes is : $204"
          " and you can find it in block 3")

elif fruit_input == "cherry seed":
    print("the price of cherry seed is : $500"
          " and you can it in block 7")

elif fruit_input == "pineapple":
    print("the price of pineapple is : $300"
          " and you can find it in block 22")

elif fruit_input == "mango":
    print("the price of mango is : $103"
          " and you can find it in block 36")

elif fruit_input == "melon seed":
    print("the price of melon seed is : $502"
          " and you can find it in block 80")

elif fruit_input == "garden egg":
    print("the price of garden egg is : $100"
          " and you can find it in block 28")

elif fruit_input == "apple":
    print("the price of apple is : $1000"
          " and you can find it in block 92")

elif fruit_input == "paw - paw":
    print("the price of paw - paw is : $570"
          " and you can find it in block 8")

elif fruit_input == "onion":
    print("the price of onion is : $149"
          " and you can find it in block 29")

elif fruit_input == "water melon":
    print('the price of water melon is : $242'
          ' and you can find it in block 16')

# AN ELSE STATEMENT TO PRINT 'INVALID FRUIT NAME' TO THE USER ANYTIME THEY
# ENTER  IN THE WRONG FRUIT
else:
    print('ERROR: invalid fruit name')
    print('please observe the menu one more time to get the correct fruit name')
