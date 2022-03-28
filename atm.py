import logging
List = ["1.Check Balance ","2. Withdraw Cash","3.Desposit Cash","4.Quit"]
import time
for i in List:
  print (i)

x = int(input ("Enter a choice:"))
while x != 4:
  x
  if x == 1:
    
    print ("Proceeding.........")
    time.sleep(3)
    print ("You have  20000 in your account.")
  elif x == 2:
    print ("PLEASE WAIT .......")
    time.sleep (3)
    withdraw = int(input ("Type the amount to withdraw:"))
    if withdraw > 20000:
      print ("You only have 20000 ")
      logging.warn("Sorry you don't have enough money")
      
    else:
      print ("withdrawing the cash")
    print (f"Now you have {20000 - withdraw} in your bank account")
  elif x == 3:
    print ("PLEASE Wait......")
    time.sleep(3)
    print("Add CASH")
    print ("PLEASE Wait......")
    print ("Amount Desposited successfully")
    print ("Want to add more cash")
    y1 = input ("Add MORE CASH......:")
    if y1 == "y" or "yes":
      print ("Adding more cash")


  elif x== 4:
    print ("Thankyou for Wisting ")
  else:
    print ("something went wrong ! ")

  y = input ("Do you want more transaction:")
  if y == "y" or "yes":
    print ("wait for while")
    time.sleep(3)
    x = int(input ("Enter a choice:"))
  else:
    break
