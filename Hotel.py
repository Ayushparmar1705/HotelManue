class HotelManu:
    def getcustomer(self):
        fn = input("Enter the first name : ")
        ln = input("Enter the last name : ")
        billnumber = int(input("Enter the bill number : "))
        
        
    def display(self):
        print("First name : ",self.fn)
        print("Last name : ",self.ln)
        print("Bill number ",self.billnumber)
            
            
    
    def Manu(self):
        sum = 0
        while(True):
            print("------------------------------------------------------------------")
            print("\n1...Water                    10R")
            print("\n2...Coffy                    20R")
            print("\n3...Pav-Bhagi                100R ")
            print("\n4...Pizza                    100R")
            print("\n5...Cold Drinks               40R")
            print("------------------------------------------------------------------")
            ch = int(input("Enter Your Choice : "))
            if ch == 1:
                sum = sum + 10
                print("Selected Water")
                print("Water Price : ",sum)
                print("Do you want too continue?" )
                option = int(input("continue press (1) otherwise press (0)"))
             
                
                
                if option == 1:
                    continue
                
                else:
                    print("Total Bill is : ",sum)
                    print("Please welcome next time ........")
                    break
                    
            elif ch == 2:
                print("Selected Coffy")
                sum = sum + 20
                print("Price Coffy ",sum)
                
                
                print("Do you want too continue?" )
                option = int(input("continue press (1) otherwise press (0)"))
                
                
                if option == 1:
                    continue
                
                else:
                    print("Your Total Bill : ",sum)
                    print("Please welcome next time ........")
                    break
                    
            
            elif ch == 3:
                print("Selected Pav-Bahgi ")
                sum = sum + 100
                print("Price Pav-Bhagi ",sum)
                
                
                print("Do you want too continue?" )
                option = int(input("continue press (1) otherwise press (0)"))
                
                
                if option == 1:
                    continue
                
                else:
                    print("Total Bill is : ",sum)
                    print("Please welcome next time ........")
                    break
                    
            elif ch == 4:
                print("Selected Pizza ")
                sum = sum + 100
                print("Price Pizza ",sum)
                
                
                print("Do you want too continue?" )
                option = int(input("continue press (1) otherwise press (0)"))
                
                if option == 1:
                    continue
                
                else:
                    print("Total Bill is : ",sum)
                    print("Please welcome next time ........")
                    break
                    
            elif ch == 5:
                print("Selected Cold Drinks ")
                sum = sum + 40
                print("Price Cold Drinks ",sum)
                print("Do you want too continue?" )
                option = int(input("continue press (1) otherwise press (0)"))
                
                
                if option == 1:
                    continue
                
                else:
                    print("Total Bill is : ",sum)
                    print("Please welcome next time ........")
                    break
