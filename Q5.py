a = int(input("Enter 1st Item Price:"))
b = int(input("Enter 2nd Item Price:"))
c = int(input("Enter 3rd Item Price:"))
d = int(input("Enter 4th Item Price:"))
e = int(input("Enter 5th Item Price:"))
f = int(input("Enter 6th Item Price:"))
g = int(input("Enter 7th Item Price:"))
h = int(input("Enter 8th Item Price:"))
i = int(input("Enter 9th Item Price:"))
j = int(input("Enter 10th Item Price:"))
Total = a+b+c+d+e+f+g+h+i+j
print("TOTAL AMOUNT:",Total) 
if int(Total)>2000:
    Discount = Total*0.2
    final = Total-Discount
    print("DISCOUNT:",Discount, "\nFINAL AMOUNT:",final)
else:
    print("No Discount")


