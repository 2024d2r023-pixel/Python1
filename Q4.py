a = input("Enter English Marks:")
b = input("Enter Maths Marks:")
c = input("Enter Science Marks:")
d = input("Enter Hindi Marks:")
e = input("Enter SST Marks:")
Total = int(a)+int(b)+int(c)+int(d)+int(e)
Per = (Total/500*100)
print("TOTAL:",Total , "\nPERCENTAGE:",Per)
if int(Per) >= 50:
    print("Pass")
else:
    print("Fail")