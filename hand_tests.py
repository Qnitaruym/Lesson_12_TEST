from functions import salary, hello_who

if hello_who("Max") != "Hello, Max":
   print("Error")
else:
    print("Good")
if hello_who("Ben") != "Hello, Ben":
    print("Error")
else:
    print("Good")


if salary( 7, 99) != 1386:
    print("Error")
else:
    print("Good")
