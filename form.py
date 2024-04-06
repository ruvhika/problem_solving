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
c=0
print("Communication skill of course lead")
print("1.very poor")
print("2.poor")
print("3.Average")
print("4.good")
print("5.very good")
c=int(input("c="))


if c==1:
    o3="Very Poor"


elif c==2:
    o3="Poor"

elif c==3:
    o3="Average"

elif c==4:
    o3="Good"

elif c==5:
    o3="Very Good"
else:
    None

print(o3)

g=0
print("The course substantially improved my knowledge level :")
print("1.Strongly Disagree")
print("2.Disagree")
print("3.Neutral")
print("4.Agree")
print("5.Strongly Agree")
b=int(input("h="))

if g==1:
    o7="Strongly Disagree"


elif g==2:
    o7="Disagree"

elif g==3:
    o7="Neutral"

elif g==4:
    o7="Agree"

elif g==5:
    o7="Strongly Agree"

else:
    None

print(o7)
