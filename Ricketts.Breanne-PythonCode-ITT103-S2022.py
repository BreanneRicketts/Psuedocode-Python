#Author:Breanne Ricketts
#Date Created: May 2, 2022
#Course: ITT103
#Purpose: The purpose of this python code is provide the framework that guides the program's direction, whereas the goals and objectives outline how the purpose will be achieved.


Class_1c_rate = 0.06
Class_1d_rate = 0.07
Class_1e_rate = 0.10

Class_2c_rate = 0.04
Class_2d_rate = 0.06

Class_3_rate = 0.045

Salesperson_num= int(input("Input salesperson number"))
while Salesperson_num != 0:
    Salesperson_num= int(input("Input salesperson number"))
    Sales_amount=int(input("Input Sales amount"))
    Class=int(input("Input Class"))
    if Class == 1:
        if Sales_amount <= 1000:
            print ("Your commission rate is", Sales_amount * Class_1c_rate)
    if Class == 1:
        if Sales_amount > 1000 and Sales_amount < 2000:
            print("Your comission rate is",Sales_amount * Class_1c_rate)
    if Class == 1:
        if Sales_amount >= 2000:
            print ("Your comission rate is", Sales_amount * Class_1e_rate)
    elif Class == 2:
        if Sales_amount < 1000:
            print ("Your comission rate is", Sales_amount * Class_2c_rate)
    if Class == 2:
        if Sales_amount >= 1000:
            print ("Your comission rate is", Sales_amount * Class_2c_rate)
    elif Class == 3:
        print("Your commision rate is", Sales_amount * Class_3_rate)
    else:
        print("Error Message")

    i=input("Would you like to continue? ")
    if i =="no":
        break

"End"
