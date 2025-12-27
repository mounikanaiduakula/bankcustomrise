import mysql.connector

db_connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Mounika756",
    database="SBIBankDatabase"
)
cursorObj=db_connection.cursor()

def managingRequests():
    allReqs=viewAllRequests()
    print(allReqs,'allReqs 13')

    inp=input("enter req_type to fetch pending,   rejected, approved") 
    inpReq=input("enter req_type to fetch loan,   atm_card,   check_book,   nte_banking") 

    for t in allReqs:
        name,r_type,bal,status=t
        print(t)
    if status == inp and r_type== inpReq:   
        userName=input("enter person anme :--- ")
        cursorObj.execute("select user_id from users where user_name=%s",(userName,))
        user_details=cursorObj.fetchone()
        user_id=user_details[0]
        if userName == t[0]:
            if bal > 500000: 
                staus_Updated="rejected"
                cursorObj.execute("update requests  set req_status=%s  where user_id=%s ",(staus_Updated,user_id))
                db_connection.commit()
                print("rejected cause , bid amount > limit amount")
            else:
                staus_Updated="approved"
                cursorObj.execute("update requests  set req_status=%s  where user_id=%s ",(staus_Updated,user_id))
                db_connection.commit()
                print("approved enjoy with friends and comlete loan then come again for loan")
def viewAllRequests():
    cursorObj.execute("""
    select users.user_name,requests.req_type,requests.req_bal,requests.req_status
    from users 
    left join requests 
    using (user_id) 
    """)
    allRequests=cursorObj.fetchall()
    print(allRequests)
    return allRequests


def deleteCustomer():
    deletPersonuser_id=int(input("enter user_id here to delete that customer :---   "))
    cursorObj.execute("delete from accounts where user_id =%s",(deletPersonuser_id,))    
    cursorObj.execute("delete from requests where user_id =%s",(deletPersonuser_id,))    
    cursorObj.execute("delete from users where user_id =%s",(deletPersonuser_id,))    
    db_connection.commit()
    print("deleted successfullyyy.....")

            
def  searchCustomer():
    id=int(input ("enter searching customer id :-- "))
    cursorObj.execute("select users.user_id,users.user_name,accounts.acc_bal,requests.req_type from users left join accounts using(user_id) left join requests using (user_id) where user_id = %s",(id,))


def requestRaise(user_id,req_mode): 
    qtAmt=int(input("enetr quoting amount for laon :----- "))
    cursorObj.execute("insert into requests(user_id, req_type, req_bal) values (%s,%s,%s)",(user_id,req_mode,qtAmt))
    db_connection.commit()

def deposit(user_id):
    depoAmt=int(input("enter depo amount :--   "))

    if depoAmt >0:
        cursorObj.execute("update accounts set acc_bal=acc_bal+%s where user_id = %s",(depoAmt,user_id))
        db_connection.commit()
        print("depo successfully.....")
    else:
        print("deposit amount should be >0 rupees but not -negative rupees")    
    


def check_Bal(user_id):
    cursorObj.execute("select * from accounts where user_id=%s",(user_id,))
    mainBal=cursorObj.fetchone()
    return mainBal

    
def withdraw(userid):
    amt=int(input("enter amount to draw :----     "))
    abc=check_Bal(userid)
    acId,userId,accType,Main_Amt=abc
    if amt>Main_Amt:
        print(f"you are trying to draw{ amt} but you are having only main bal {Main_Amt}")
    elif amt<=Main_Amt:
        cursorObj.execute("update accounts set acc_bal=acc_bal-%s where user_id = %s",(amt,userId))
        db_connection.commit()
        cursorObj.execute("select * from accounts where user_id=%s",(userid,))
        mainBal=cursorObj.fetchone()
        acId,userId,accType,Main_Amt=mainBal
        print(f"{amt } drwan successfully....",f"main bal {Main_Amt}")
def signup():
    name=input("enter your name :-- ").strip().lower()
    password=input("enter your password here :--  ").strip().lower()
    userRole=input("enter role here (customer / admin ):--- ").strip().lower()
    cursorObj.execute("insert into users (user_name,user_pswd,user_role) values (%s,%s,%s)",(name,password,userRole))
    db_connection.commit()
    cursorObj.execute("select * from users where user_name = %s",(name,))

    data=cursorObj.fetchone()
    user_id,un,up,uRole=data
    print(user_id,"id")
    
    acc_type=input("enter ac/type ( savings / current ):--  ")
    cursorObj.execute("insert into accounts (user_id,acc_type,acc_bal) values (%s,%s,%s) ",(user_id,acc_type,5000))
    db_connection.commit()
def login():
    name=input("enter name here :-- ")
    pswd=input("enter password here :--- ")
    role=input("enter role  ( customer/admin ) :--    ")
    cursorObj.execute("select * from users where user_name=%s",(name,))
    data=cursorObj.fetchone()
    user_id,userN,userP,userR=data
    print(userR,"role")
    if userR == "customer":
        print("---------customerMenu----------")
        print("---------1.withdraw----------")
        print("---------2.deposit----------")
        print("---------3.checkBal----------")
        print("--------4. requestRaise ----------")
        choose=input("enter one option here :----      ") 

        if choose == "1":
            withdraw(user_id)
        if choose == "3":
            print(check_Bal(user_id))  
        if choose == "2":
            deposit(user_id) 

        if choose == "4":
            print('1. Loan    2.atm_card     3.check_book    4.net_banking')
            req_Type=int(input("enter your choice here :--     ")) #1
            if req_Type == 1:
                req="loan"
                requestRaise(user_id,req)

            if req_Type == 2:
                req="atm_card"
                requestRaise(user_id,req)

            if req_Type == 3:
                req="check_book"
                requestRaise(user_id,req)

            if req_Type == 4:
                req="net_banking"
                requestRaise(user_id,req)            


    if userR == "admin" and userP==pswd:
        print("---------adminMenu----------")
        print("--------1.Deelte Customer-----------")
        print("---------2.search customer----------")
        print("---------3.view allRequests----------")
        print("---------4.view Accounts----------")
        print("---------5.managing requests----------")
        choose=input("enter option here :--     ")
        if choose == "2":
            searchCustomer()
        if choose == "1":
            deleteCustomer()  
        if choose == "3":
            viewAllRequests()
        if choose == "4":
            viewAllAccounts()  
        if choose == "5":
            managingRequests()         
    
     

print("--- SBI bank project-----")
print("1.signup")
print("2.login")
print("3.exit")

choose=input("enter your option :--    "  )

if choose == "1":
    signup()
if choose == "2":
    login()    