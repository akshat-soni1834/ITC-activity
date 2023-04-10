Room=int(input("1.Deluxe, 2.Non-AC:- "))
Days=int(input("Enter the number of days you have stayed:- "))  
Food=float(input("Enter the total amount you paid for food:- "))
if Room == 1:
    charge= 7500 * Days
    tax=0.18*Food
else:
    charge = 4500*Days
    tax=0.05*Food
tip=0.1*Food
total= charge+tip+tax+Food
print(f"Tip amount {tip} rupees")
print(f"Food amount breaks CGST: {0.5*tax}  SGST: {0.5*tax} rupees")
print(f"Grand Total: {total} rupees")