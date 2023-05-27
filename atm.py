print("WELCOME TO STATE BANK OF INDIA....")
print("Welcome to our bank...Please enter the required option from the list below...")
print("0:LOG-OUT      1:VIEW ACCOUNT BALANCE  2:WITHDRAW CASH")
print(" 3.change pin   4:DEPOSIT_CASH         5:RETURN CARD ")
op=input("select options like 0,1,2,3,4,5..")
if(op=='1'):
    print("login")
    Pin=input("please enter your 4 digit pin")
    pin=len(Pin)
    print("!!!!CAUTION DONT SHARE YOUR PIN WITH ANYONE...KEEP IT CONFIDENTIAL!!!!!!")
    if(Pin=="1234"):
      print("The account balance is 50000")
    if(Pin=="5678"):
      print("The account balance is 80000")  
if(op=='2'):
    print("Account Balance is 536686865")
elif(op=='3'):
    print("Withdraw Cash")
    print("Enter the amount you wish to withdraw...")
    amount=input("select the amount 500,1000,2000,10000")
    print("The transaction is being processed......")
    print("please withdraw your cash.....")
    if(amount=="10000"):
     print("the main account balance is 50000")
    else:
       print("the main account balance is 25000")
    amount2=(amount2)
elif(op=='4'):
    print("Deposit Cash")
    print("To deposit please enter the required fields:")
    acc_no=input("enter the acc_no")
    acc_holdername=input("enter the acc_holder name")
    pan_no=input("enter the pan_no")
    amount=input("enter the amount to be deposited")
    IFSC_CODE=input("enter the IFSC CODE")
    pin=input("enter the pin")
    print("THE AMOUNT HAS BEEN DEPOSITED SUCCESSFULLY")
elif(op=='5'):
    print("To change pin follow the steps:")
    for i in range(3):
        pin=input("Enter pin:")
        new_pin=input("enter the new pin")
        if((new_pin!=pin)):
            if(i<3):
                print("Invalid pin!,you have left with,2-i,attempts")
            else:
                print("Account is blocked!please contact admin!!!")
                userchoice='e'
        else:
                print("Successfully logged in")
                print("Thank you")
                break
    new_pin=input("confirm the changed_pin")
    print("the pin has been changed successfully")

     

    
