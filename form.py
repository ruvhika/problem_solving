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
a=int(input("a="))

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
print("5.Very Good")
b=int(input("b="))

if b==1:
    o2="Very Poor"


elif b==2:
    o2="Poor"

elif b==3:
    o2="Average"

elif b==4:
    o2="Good"

elif b==5:
    o2="Very Good"

else:
    None


c=0
print("Communication skills of the Course Lead :")
print("1.Very Poor")
print("2.Poor")
print("3.Average")
print("4.Good")
print("3.Very Good")
c=int(input("b="))

if c==1:
    o3="Very Poor"


elif c==2:
    o3="Poor"

elif c==3:
    o3="Average"

elif c==4:
    o3="Very Good"

else:
    None

d=0
print("Communication skills of the Course Lead :")
print("1.Very Poor")
print("2.Poor")
print("3.Average")
print("4.Good")
print("5.Very Good")
d=int(input("b="))

if d==1:
    o4="Very Poor"


elif d==2:
    o4="Poor"

elif d==3:
    o4="Average"

elif d==4:
    o4="Good"

elif d==5:
    o4="Very Good"

else:
    None


e=0
print("Communication skills of the Course Lead :")
print("1.Very Poor")
print("2.Poor")
print("3.Average")
print("4.Good")
print("5.Very Good")
e=int(input("b="))

if e==1:
    o5="Very Poor"


elif e==2:
    o5="Poor"

elif e==3:
    o5="Average"

elif e==4:
    o5="Good"

elif e==5:
    o5="Very Good"

else:
    None


print(name)
print(email)
print(contact)
print(school)
print(n)
print(s)
print(h)
print(j)
print(k)
print()
print("Feedback Form")
print(o1)
print(o2)
print(o3)
print(o4)
print(o5)






