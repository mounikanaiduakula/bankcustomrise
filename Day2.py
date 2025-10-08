import mysql.connector

db_connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Mounika756",
    database="SBIBankDatabase"
)
cursorobj=db_connection.cursor()

def signup():
    name=input("enter your name:--").strip().lower()
    password=input("enter your password here:--").strip().lower()
    userole=input("enter a role here (customer/admin):--").strip().lower()
    cursorobj.execute("insert into users (user_name,user_password,user_role) values (%s,%s,%s)",(name,password,userole))
    db_connection.commit
    cursorobj.execute("select * from users where user_name=%s",(name,))

    data=cursorobj.fetchone()
    user_id,un,up,upurole=data
    print(user_id,"id")

    acc_type=input("enter ac/type (savings/current):-- ")
    cursorobj.execute("insert into accounts (user_id,acc_type,acc_bal) values (%s,%s,%s)",(user_id,acc_type,5000))
    db_connection.commit()

print("---SBI BANK PROJECT")
print("1.signup")
print("2.logup")
print("3.exit")

choose=input("enter your option:--")
if choose == "1":
    signup()

