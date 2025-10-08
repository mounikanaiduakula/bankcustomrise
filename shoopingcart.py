cart = []

products = [
    {"id": 1, "name": "Laptop", "price": 800},
    {"id": 2, "name": "Phone", "price": 500},
    {"id": 3, "name": "Headphones", "price": 100},
    {"id": 4, "name": "Keyboard", "price": 50},
    {"id": 5, "name": "Mouse", "price": 30}
]

def view_products():
    for p in products:
        print(p["id"], p["name"], "$", p["price"])

def add_to_cart():
    pid = int(input("Enter Product ID: "))
    qty = int(input("Enter Quantity: "))

    for p in products:
        if p["id"] == pid:
            for item in cart:
                if item["id"] == pid:
                    item["quantity"] += qty
                    print("Updated", p["name"])
                    return
            cart.append({"id": pid, "name": p["name"], "price": p["price"], "quantity": qty})
            print("Added", p["name"])
            return
    print("Product not found")

def view_cart():
    total = 0
    for item in cart:
        sub = item["price"] * item["quantity"]
        total += sub
        print(item["id"], item["name"], "$", item["price"], "x", item["quantity"], "=", sub)
    print("Total:", total)

def update_cart():
    pid = int(input("Enter Product ID: "))
    qty = int(input("Enter new quantity: "))
    for item in cart:
        if item["id"] == pid:
            item["quantity"] = qty
            print("Updated", item["name"])
            return
    print("Item not in cart")

def remove_from_cart():
    pid = int(input("Enter Product ID: "))
    for item in cart:
        if item["id"] == pid:
            cart.remove(item)
            print("Removed", item["name"])
            return
    print("Item not in cart")

def checkout():
    view_cart()
    print("Thank you for shopping!")
    cart.clear()

while True:
    print("1.View Products")
    print("2.Add")
    print("3.View cart")  
    print("4.Update")
    print("5.Remove")
    print("6.Checkout") 
    print("7.Exit")   
    choice = input("Choose: ")
    if choice == "1":
        view_products()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        view_cart()
    elif choice == "4":
        update_cart()
    elif choice == "5":
        remove_from_cart()
    elif choice == "6":
        checkout()
    elif choice == "7":
        break
