# solving a task
name=input("First Name: ")
surname=input("Last Name:")
email=input("email: ")
contact=int(input("Contact: "))
school=input("school:")
if school=="School of engineering":
    print("Select options:\nBtech\nBCA")
    n=input("Enter stream:")
    if n=="Btech" or n=="BCA":
        print(n)
    else:
        print("not available")
elif school=="School of management":
    print("Select options:\nBBA\nMBA")
    n=input("Enter stream:")
    if n=="MBA" or n=="BBA":
        print(n)
    else:
        print("not available")
a=int(input("Enter year:"))
s=int(input("Enter semester:"))
h=input("Course name:")
j=input("Course code:")
k=input("Faculty name:")

