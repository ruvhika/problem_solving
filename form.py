# solving a task
name=input("First Name: ")
surname=input("Last Name:")

while True:
    email=input("email: ")
    if '@' in email:
        break
    else :
        print("Invalid email id")

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
s=int(input("Enter semester:"))
h=input("Course name:")
j=input("Course code:")
k=input("Faculty name:")










print("Feedback Form")

a=0
print("Are you satisfied with the overall teaching of the course:")
print("1.Highly Satisfied")
print("2.Moderately Satisfied")
print("3.Not Satisfied")
int(input("a="))

if a==1:
    o1="Highly Satisfied"


elif a==2:
    o1="Moderately Satisfied"

elif a==3:
    o1=".Not Satisfied"

else:
    None

b=0
print("Subject knowledge of the Course Lead :")
print("1.Very Poor")
print("2.Poor")
print("3.Average")
print("4.Good")
print("3.Very Good")
b=int(input("b="))

if b==1:
    o2="Very Poor"


elif b==2:
    o2="Poor"

elif b==3:
    o2="Average"

elif b==4:
    o2="Very Good"

else:
    None

print(o2)
h=0
print("Overall rating for the course :")
print("1.Very Poor")
print("2.Poor")
print("3.Good")
print("4.very Good")
print("5.Excellent")
b=int(input("h="))

if b==1:
    o8="Very Poor"


elif b==2:
    o8="Poor"

elif b==3:
    o8="Good"

elif b==4:
    o8="Very Good"

elif b==5:
    08="Excellent"

else:
    None

print(o8)
