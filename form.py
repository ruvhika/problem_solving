# solving a task
print("Student feedback form:")
name=input("First Name: ")
surname=input("Last Name:")
email=input("email: ")
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
r=0
print(" Student-teacher interaction in class :")
print("1.Very Poor")
print("2.Poor")
print("3.Average")
print("4.Good")
print("5.Very Good")
b=int(input("d="))

if r==1:
    o3="Very Poor"


elif r==2:
    o3="Poor"

elif r==3:
    o3="Average"
    
elif r==3:
    o3="Average"

elif r==4:
    o2="Very Good"

print(o2)

d=0
print("Overall rating for the Course *")
print("1.very poor")
print("2.poor")
print("3.Average")
print("4.good")
print("5.very good")
c=int(input("c="))


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

print(o4)

f=0
printf("course lead comes on time")
print("1.No")
print("2.Sometime")
print("3.Always")
f=int(input("f="))

if f==1:
    o6="No"


elif f==2:
    o6="Sometimes"

elif f==3:
    o6="Always"

else:
    None
    
c=0
print("Teaching way of the course lead:")
print("1.Very Poor")
print("2.Poor")
print("3.Average")
print("4.Good")
print('5.Excellent")
c=int(input("c="))

if c==1:
    o2="Very Poor"

elif c==2:
    o2="Poor"
    
elif c==3:
    o2="Average"

 elif c==4
    o2="Good"

elif c==5:
    o2="Excellent"

    else :
        None




