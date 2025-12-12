# Notes Saver

filename = "notes.txt"

while True:
    print("\n1. Write Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        note = input("Enter note: ")
        with open(filename, "a") as file:
            file.write(note + "\n")
        print("Note saved!")

    elif choice == "2":
        print("\n--- Notes ---")
        with open(filename, "r") as file:
            print(file.read())

    elif choice == "3":
        break

    else:
        print("Invalid choice")
