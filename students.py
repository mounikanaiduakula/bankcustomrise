students = []

def add_student():
    if len(students) >= 8:
        print("Limit reached")
    else:
        sid = input("ID: ")
        name = input("Name: ")
        course = input("Course (CS/ECE/IT/MECH/CIVIL): ").upper()
        if course in ["CS", "ECE", "IT", "MECH", "CIVIL"]:
            marks = int(input("Marks: "))
            students.append({"id": sid, "name": name, "course": course, "marks": marks})
            print("Student added successfully")
        else:
            print("Invalid course")

def view_students():
    if len(students) == 0:
        print("No students found")
    else:
        print("\nID\tName\tCourse\tMarks")
        print("-"*30)
        for s in students:
            print(s["id"], s["name"], s["course"], s["marks"])

def search_student():
    if len(students) == 0:
        print("No students to search")
    else:
        key = input("Enter ID or Name: ")
        for s in students:
            if s["id"] == key or s["name"].lower() == key.lower():
                print("\nStudent Found:")
                print("ID:", s["id"])
                print("Name:", s["name"])
                print("Course:", s["course"])
                print("Marks:", s["marks"])
                return
        print("Student not found")

def update_student():
    sid = input("Enter Student ID: ")
    for s in students:
        if s["id"] == sid:
            print("1. Update Course")
            print("2. Update Marks")
            choice = input("Choose option (1/2): ")

            if choice == "1":
                new_course = input("Enter new Course (CS/ECE/IT/MECH/CIVIL): ").upper()
                if new_course in ["CS", "ECE", "IT", "MECH", "CIVIL"]:
                    s["course"] = new_course
                    print("Course updated successfully")
                else:
                    print("Invalid course")

            elif choice == "2":
                new_marks = int(input("Enter new Marks: "))
                s["marks"] = new_marks
                print("Marks updated successfully")

            else:
                print("Invalid option")

            return
    print("Student not found")

def delete_student():
    sid = input("Enter Student ID: ")
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("Student deleted successfully")
            return
    print("Student not found")

while True:
    print("\n--- Student Management ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid option")
