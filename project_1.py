Holder_names=['vikas','harsha','yaswanth']
acc_Pin=['1122','1133','1144']
acc_balance=[100000,70000,80000]
deposit=0
withdraw=0
balance=0
add_1=1
add_2=3
i=0

while True:  
        print('-_-'*20,'\n') 
        print('******* WELCOME TO PEOPLES BANK ********\n')
        print('       1.CREATE A NEW ACCOUNT ')
        print('       2.WITHDRAW AMOUNT')
        print('       3.DEPOSIT AMOUNT')
        print('       4.BALANCE ENQUERY ')
        print('--     5.EXIT \n')
        print('-_-'*20,'\n')

        user_option=int(input('PLESE ENTER YOUR OPTION : '))
        if user_option==1:
                print('YOU SELECTED CREATE OPTION')
                num_of_cust=eval(input('HOW MANY ACCOUNTS YOU WANT TO CREATE : '))
                i+=num_of_cust
                if i>3:
                        print('\n SORRY YOU ENTERED MORE THAN 3  CUSTOMERS')
                        i-=num_of_cust
                else :
                        # The while loop will run according to the no:of customers.
                        while add_1 <= i:
                                name=input('PLESE ENTER YOUR FULL NAME : ')
                                Holder_names.append(name)
                                def create_pin(acc_Pin):
                                    pin=str(input('PLEASE CREATE YOUR 4 DIGIT PIN : '))
                                    if len(pin) == 4:
                                       acc_Pin.append(pin)
                                    else:
                                        print('YOUR PIN SO TOO LONG OR TOO LOW')
                                        create_pin(acc_Pin)
                                create_pin(acc_Pin) 
                                balance =0       
                                deposit=eval(input('PLEASE DEPOSITE YOUR AMOUNT : '))
                                balance = deposit+balance
                                acc_balance.append(balance)
                                add_2 = len(Holder_names)
                                print('\nNAME :', end=" ")
                                print(f'{Holder_names}')
                                print('PIN :',end=" ")
                                print(f'{acc_Pin}')
                                print('BALANCE :',end=" ")
                                print(f'{acc_balance}','-/RS')
                                add_1 = add_1 + 1
                                add_2 = add_2 + 1
                                print('\n YOUR DETAILS ARE ADDED TO OUR BANK')
                                print('**** YOUR ACCOUNT IS CREATED SUCCESSFULLY ****\n')
                                print('HEAR YOU CAN CHECK YOUR NAME IN THE LIST\n')
                                print(Holder_names)
                                print("\n")
                                print('NOTE : PLEASE REMEMBER THE PASSWORD')
                                print('='*20)
                        main_menu=input('PRESS ANY KEY TO GO BACK TO HOME :')         
                        
        elif user_option == 2:
                print('YOU SELECTED WITHDRAWAL OPTION')
                j=0
                while j<1:
                      k=-1 
                      name = input("PLEASE ENTER YOUR FULL NAME: ")
                      pin = str(input('PLEASE ENTER YOUR PERSONAL PIN: ')) 
                      while k < len(Holder_names) -1:
                            k = k+1
                            if name == Holder_names[k]:
                               if pin == acc_Pin[k]:
                                    j=j+1
                                    print("YOUR CURRENT BALANCE IS:", end=" ")
                                    print(acc_balance[k], end=" ")
                                    print("/-RS\n")
                                    balance = (acc_balance[k])
                                    withdraw = eval(input("ENTER YOUR WITHDRAWAL AMOUNT: "))
                                    if withdraw > balance:
                                          deposit = eval(input("YOUR CURRENT BALANCE IS LOWER THAN WITHDRAWAL PLEASE DEPOSIT AMOUNT AND WITHDRAW: "))
                                          balance = balance+deposit
                                          print("YOUR CURRENT BALANCE IS: ",balance, end=" ")
                                          print("-/RS\n")
                                          balance = balance-withdraw
                                          print("\n")
                                          print("----------WITHDRAWAL SUCCESSFULL----------")
                                          acc_balance[k]=balance
                                          print("YOUR NEW BALANCE IS: ",balance, end=" ")
                                          print("-/RS\n\n")
                                    else:
                                         balance = balance-withdraw   
                                         print("\n")
                                         print("----------WITHDRAWAL SUCCESSFULL----------")
                                         acc_balance[k]=balance
                                         print("YOUR NEW BALANCE IS: ",balance, end=" ")
                                         print("-/RS\n\n")  
                main_menu=input('PRESS ANY KEY TO GO BACK TO HOME :') 
                
        elif user_option == 3:
                print('YOU SELECTED DEPOSIT OPTION')
                n=0
                while n<1:
                      k=-1 
                      name = input("PLEASE ENTER YOUR FULL NAME: ")
                      pin = str(input('PLEASE ENTER YOUR PERSONAL PIN: ')) 
                      while k < len(Holder_names) -1:
                            k = k+1
                            if name == Holder_names[k]:
                               if pin == acc_Pin[k]:
                                    n=n+1
                                    print("YOUR CURRENT BALANCE IS:", end=" ")
                                    print(acc_balance[k], end=" ")
                                    print("/-RS\n")
                                    balance = (acc_balance[k])
                                    deposit = eval(input("PLEASE ENTER YOUR DEPOSIT AMOUNT: "))
                                    balance = balance+deposit
                                    acc_balance[k]=balance
                                    print("\n")
                                    print("----------DEPOSIT SUCCESSFULL----------")
                                    print("YOUR NEW BALANCE IS: ",balance, end=" ")
                                    print("-/RS\n\n")
                if n < 1:
                      print("YOUR NAME AND PIN DOESN'T MATCH!\n")
                      break            
                main_menu=input('PRESS ANY KEY TO GO BACK TO HOME :') 
                                    
        elif user_option == 4:
               print('YOU SELECTED BALANCE ENQUERY OPTION')
               k=0
               print("CUSTOMER NAME LIST AND BALANCE LIST BELOW: ")
               print("\n")
               while k<=len(Holder_names)-1:
                 print("ACCOUNT HOLDER =", Holder_names[k])
                 print("ACCOUNT BALANCE =", acc_balance[k], end=" ")
                 print("-/RS")
                 print("\n")
                 k=k+1
               main_menu=input('PRESS ANY KEY TO GO BACK TO HOME :')             
         

        elif user_option == 5:
            print('YOU SELECTED EXIT OPTION')
            print("\n")
            print("**************** THANKS FOR CHOOSING OUR BANKS ****************")  
            print("\n")                      
            print("*********************** VISIT AGAIN ****************")    
            break
        else:
             print("INVALID OPTION PLEASE TRY AGAIN")      
             main_menu=input('PRESS ANY KEY TO GO BACK TO HOME :')                         
        
                                