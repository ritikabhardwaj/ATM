import sqlite3
import math

def checK(ck):
     conn=sqlite3.connect("AccountInfo.db")
     cmd="select * from details where Card_No="+str(ck)
     cursor=conn.execute(cmd)
     profile=None
     for row in cursor:
          profile=row
     conn.close
     return profile

def gcd(a, b):
     while(b > 0):
          c = a % b
          a = b
          b = c
     return a
           
p=97
q=107
n=p*q
phi=(p-1)*(q-1)
for e in range(2,phi): 
    if gcd(e,phi)== 1: 
        break
f=2*e+1
g=n-1

for i in range(1,10): 
    x = 1 + i*phi
    if x % e == 0: 
        d = int(x/e) 
        break

def encrypt(msg):
     c=(msg**e)%(n)
     return c

def decrypt(c):
     y=(c**d)%(n)
     return y

def update(cardNo,pin):
     conn=sqlite3.connect("AccountInfo.db")
     cmd="select * from details where Card_No='"+str(cardNo)+"'"
     cursor=conn.execute(cmd)
     ifRecordExist=0
     for row in cursor:
          ifRecordExist=1
     if(ifRecordExist==1):
          cmd="update details SET Pin='"+str(pin)+"' where Card_No= '"+str(cardNo)+"'"
     conn.execute(cmd)    
     conn.commit()
     conn.close()
     
def updateB(cardNo,balance):
     conn=sqlite3.connect("AccountInfo.db")
     cmd="select * from details where Card_No="+str(cardNo)
     cursor=conn.execute(cmd)
     ifRecordExist=0
     for row in cursor:
          ifRecordExist=1
     if(ifRecordExist==1):
          cmd="update details SET Balance="+str(balance)+" where Card_No="+str(cardNo)
     conn.execute(cmd)    
     conn.commit()
     conn.close()

def server(cardNo,pin_user):
     pin_user=decrypt(pin_user)
     profile=checK(cardNo)
     if(profile!=None):
          pin=profile[5]
          Pin=int(pin)
          balance=int(profile[4])
          if(Pin == 0):
               pin=str(input('\nEnter a new pin: '))
               if(len(pin)!=4):
                    print('\nPin must have 4 digits. Pls Re-enter: ')
                    pin=str(input('Enter the Pin: '))
               print('Pin Created Successfully')
               pin=hash(str(pin))
               update(cardNo,pin)
          else:
               pin_user=str(pin_user)
               pin_user=hash(pin_user)
               pin_user=int(pin_user)
          
               if(Pin==pin_user):
                    if(balance>=Amt):
                        balance=balance-Amt
                        print ('\nTRANSACTION SUCCESS')
                        print ('Available Balance is ', balance)
                        updateB(cardNo,balance)
                    else:
                        print('\nYOU DONT HAVE SUFFICIENT BALANCE')
               else:
                    print('**Pin entered is INCORRECT**')
     else:
            print ('\n**ENTERED CARD NUMBER IS INVALID**')
     

def server2(cardNo,pin_user):
     pin_user=decrypt(pin_user)
     profile=checK(cardNo)
     if(profile!=None):
          pin=profile[5]
          balance=profile[4]
          if(pin == 0):
               pin=str(input('\nEnter a new pin: '))
               if(len(pin)!=4):
                    print('\nPin must have 4 digits. Pls Re-enter: ')
                    pin=str(input('Enter the Pin: '))
               print('Pin Created Successfully')
               pin=hash(str(pin))
               update(cardNo,pin)
          else:
               pin_user=str(pin_user)
               pin_user=hash(pin_user)
               if(pin==pin_user):
                    print('Available Balance : ',balance)
               else:
                    print('\n**Pin entered is INCORRECT**')
     if(profile==None):
          print ('\n**ENTERED CARD NUMBER IS INVALID**')
               
def server3(cardNo,pin_user):
     pin_user=decrypt(pin_user)
     profile=checK(cardNo)
     if(profile!=None):
          pin=profile[5]
          if(pin==0):
               pin=str(input('\nEnter a new pin: '))
               if(len(pin)!=4):
                    print('\nPin must have 4 digits. Pls Re-enter: ')
                    pin=str(input('Enter the Pin: '))
               print('Pin Created Successfully')
               pin=hash(str(pin))
               update(cardNo,pin)
          else:
               pin_user=hash(str(pin_user))
               if(pin==pin_user):
                    newpin=str(input('Enter the new Pin: '))
                    if(len(newpin)!=4):
                        print('\nPin must have 4 digits. Pls Re-enter: ')
                        newpin=str(input('Enter the Pin: '))
                    print('\n**Pin changed Successfully**')
                    pin=hash(newpin)
                    update(cardNo,pin)
               else:
                    print ('\n**Pin entered is incorrect**')
     if(profile==None):
          print ('\n**ENTERED CARD NUMBER IS INVALID**')
          
          
print ('\n------------------------Welcome---------------------------\n')
print('Please choose among the following options:')
a=int(input('\n1. Withdrawl \n2. Check Balance \n3. Create or Change Pin \n4. Exit\n\nEnter your choice: '))
while(a!=4):
     if(a==1):
          cardNo=str(input('Enter the Card No.: '))
          pin_user=int(input('Enter the pin: '))
          pin_user=int(encrypt(pin_user))
          Amt=int(input("\nEnter amt to be removed: "))
          server(cardNo,pin_user)
          
     if(a==2):
          cardNo=str(input('Enter the Card No.: '))
          pin_user=int(input('Enter the pin: '))
          pin_user=int(encrypt(pin_user))
          server2(cardNo,pin_user)

     if(a==3):
          cardNo=str(input('Enter the Card No.: '))
          pin_user=int(input('Enter the pin: '))
          pin_user=int(encrypt(pin_user))
          server3(cardNo,pin_user)
     
     z=int(input('\nDo you want to continue:\n1. Yes\t2.No \nEnter your Choice: '))
     if(z==1):
          a=int(input('\n1. Withdrawl \n2. Check Balance \n3. Create or Change Pin \n4. Exit\n\nEnter your choice: '))
     if(z==2):
          break
if(a==4 or z==2):
     print ("Good Bye")
     exit
