from Hotel import *
h = HotelManu()

print("Welcome My Hotel")
while True:
    print("-------------------------------------------------")
    print("1...Add custoer's")
    print("2...Display Manu ")
    print("3...Display details ")
    print("-------------------------------------------------")
    ch2 = int(input("Enter your choice : "))
    if ch2 == 1:
        h.getcustomer()
    
    
    
    elif ch2 == 2:
            h.Manu()
        
        
    elif ch2 == 3:
        h.display()
        