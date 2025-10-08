class savingsaccount:
   def init(self,account_holder,pin,balance):
      self.account_holder=account_holder
      self.pin=pin 
      self.balance=balance
      self.is_active=True
   def check_balance(self,pin):
      if not self.is_active:
         print("account inactive")
      elif pin!=self.pin:
         print("invalid pin")
      else:
         print(f"current balance:rupees{self.balance}")
def withdraw(self,amount,pin):
      if not self.is_active:
         print("account inactive")
      elif pin!=self.pin:
         print("invalid pin")
      elif amount>self.balance:
         print("incorrect funds")
      else:
         self.balance-=amount
         print(f"{amount} withdrawn successfully.newbalance :{self.balance}")
def business_account(self,business_name,balance):
      self.business_name=business_name
      self.balance=balance
      self.is_active=True
def check_balance(self):
      if self.is_active:
         print(f"bussiness balance:{self.balance}")
      else:
         print("business account is inactive")
if __name__ == "main":
    savings = savingsaccount("mouni", 10000, "1234")
    business = business_account("ABC Traders", 25000)
    print("--- Balance Check ---")
    savings.check_balance("1234")  
    savings.check_balance("0000")