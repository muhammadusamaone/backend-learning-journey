# Student Record Manager

students = []

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        students.append({"name": name, "age": age})
        print("Student added!")

    elif choice == "2":
        print("\n--- Student List ---")
        for s in students:
            print(f"Name: {s['name']} | Age: {s['age']}")

    elif choice == "3":
        break

    else:
        print("Invalid option")
