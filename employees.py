employees = []

# Add Employee
def add_employee():
    if len(employees) < 8:
        emp_id = input("Enter ID: ")
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        role = input("Enter Role: ")
        salary = float(input("Enter Salary: "))
        emp = {"ID": emp_id, "Name": name, "Department": dept, "Role": role, "Salary": salary}
        employees.append(emp)
        print("Employee added successfully!\n")
    else:
        print("Cannot add more than 8 employees.\n")

#View Employees
def view_employees():
    if len(employees) == 0:
        print("No employees found.\n")
    else:
        print("\n--- Employee List ---")
        for e in employees:
            print(f"ID: {e['ID']}, Name: {e['Name']}, Dept: {e['Department']}, Role: {e['Role']}, Salary: {e['Salary']}")
        print("----------------------\n")

#Search Employee
def search_employee():
    key = input("Enter Employee ID or Name to search: ")
    for e in employees:
        if e["ID"] == key or e["Name"].lower() == key.lower():
            print(f"ID: {e['ID']}, Name: {e['Name']}, Dept: {e['Department']}, Role: {e['Role']}, Salary: {e['Salary']}\n")
            return
    print("Employee not found.\n")

#  Update Employee
def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    for e in employees:
        if e["ID"] == emp_id:
            print("1. Update Department")
            print("2. Update Role")
            print("3. Update Salary")
            ch = input("Enter choice: ")
            if ch == "1":
                e["Department"] = input("Enter new Department: ")
            elif ch == "2":
                e["Role"] = input("Enter new Role: ")
            elif ch == "3":
                e["Salary"] = float(input("Enter new Salary: "))
            print("Employee updated successfully!\n")
            return
    print("Employee not found.\n")

# Delete Employee
def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    for e in employees:
        if e["ID"] == emp_id:
            employees.remove(e)
            print("Employee deleted successfully!\n")
            return
    print("Employee not found.\n")

while True:
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice.Try again.\n")
