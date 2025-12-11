# Area Calculator

def area_rectangle(w, h):
    return w * h

def area_circle(r):
    return 3.14159 * r * r

print("1. Rectangle\n2. Circle")
ch = input("Choose: ")

if ch == "1":
    w = float(input("Enter width: "))
    h = float(input("Enter height: "))
    print("Area =", area_rectangle(w, h))

elif ch == "2":
    r = float(input("Enter radius: "))
    print("Area =", area_circle(r))

else:
    print("Invalid choice")
