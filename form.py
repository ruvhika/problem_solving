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
school=0
print("School: \n1.School of Engineering \n2.School of Management \n3.School of Design \n4.School of laws and policy")
school=int(input("Enter school:"))
if school==1:
    print("School of Engineering")
    print("Select discipline \n 1.Btech\n 2.BCA")
    d=0
    d=int(input("Enter displine: "))
    
    if d==1:
        print("BTech")
    elif d==2:
        print("BCA")
    else:
        None
elif school==2:
    print("School of Management")
    print("Select discipline \n 1.BBA\n 2.MBA")
    d=0
    d=int(input("Enter displine: "))
    
    if d==1:
        print("BBA")
    elif d==2:
        print("MBA")
    else:
        None
elif school==3:
    print("School of Design")
    print("Select discipline \n 1.BDes\n 2.MDes")
    d=0
    d=int(input("Enter displine: "))
    
    if d==1:
        print("BDes")
    elif d==2:
        print("MDes")
    else:
        None
elif school==4:
    print("School of laws and policy")
    print("Select discipline \n 1.LLB\n ")
    d=0
    d=int(input("Enter displine: "))
    
    if d==1:
        print("LLB")
    else:
        None

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
print("5.Very Good")
b=int(input("b="))

if b==1:
    o2="Very Poor"


elif b==2:
    o2="Poor"

elif b==3:
    o2="Average"

elif b==4:
    o2="Very Good"
    
elif b==4:
    o2="Excellent"

else:
    None

print(o2)
