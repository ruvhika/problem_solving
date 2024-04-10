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
    d=int(input("Enter discipline: "))
    
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
a=int(input("select option="))

if a==1:
    o1="Highly Satisfied"


elif a==2:
    o1="Moderately Satisfied"

elif a==3:
    o1="Not Satisfied"

else:
    None

b=0
print("Subject knowledge of the Course Lead :")
print("1.Very Poor")
print("2.Poor")
print("3.Average")
print("4.Good")
print("5.Very Good")
b=int(input("select option="))

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
r=int(input("select option="))

if r==1:
    o3="Very Poor"


elif r==2:
    o3="Poor"

elif r==3:
    o3="Average"
    
elif r==3:
    o3="Average"

elif r==4:
    o3="Very Good"



d=0
print("Overall rating for the Course :")
print("1.very poor")
print("2.poor")
print("3.Average")
print("4.good")
print("5.very good")
d=int(input("select option="))


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
print("Course lead comes on time:")
print("1.No")
print("2.Sometime")
print("3.Always")
f=int(input("select option="))

if f==1:
    o6="No"


elif f==2:
    o6="Sometimes"

elif f==3:
    o6="Always"

else:
    None

x=0
print("Communication skill of course lead:")
print("1.very poor")
print("2.poor")
print("3.Average")
print("4.good")
print("5.very good")
x=int(input("select option="))

if x==1:
    o8="very poor"


elif x==2:
    o8="Poor"

elif x==3:
    o8="Average"

elif x==4:
    o8="Good"

elif x==5:
    o8="Very Good"

else:
    None

y=0
print("Would you like to have another course with course lead:")
print("1.Yes")
print("2.No")
y=int(input("select option="))
if y==1:
    o9="Yes"


elif x==2:
    o9="No"

else:
    None

z=0
print("The course was organized to help me to learn:")
print("1.Strongly disagree")
print("2.Disagree")
print("3.Neutral")
print("4.Agree")
print("5.Strongly agree")
z=int(input("select option="))

if z==1:
    o10="Strongly disagree"


elif z==2:
    o10="Disagree"

elif z==3:
    o10="Neutral"

elif z==4:
    o10="Agree"

elif z==5:
    o10="Strongly Agree"

else:
    None

p=0
print("The course substantially improved my knowledge level:")
print("1.Strongly disagree")
print("2.Disagree")
print("3.Neutral")
print("4.Agree")
print("5.Strongly agree")
p=int(input("select option="))

if p==1:
    o11="Strongly disagree"


elif p==2:
    o11="Disagree"

elif p==3:
    o11="Neutral"

elif p==4:
    o11="Agree"

elif p==5:
    o11="Strongly Agree"

else:
    None

print("What changes in way of course delivery will you recommend.")
ans=input("Ans=")

print("What did you like most about course instructor.")
ans1=input("Ans=")

print("What did you like least about the course instructor.")
ans2=input("Ans=")

print("Identify one thing that can help to improve the course.")
ans3=input("Ans=")


if f==1:
    print(name)
    print(email)
    print(contact)
    print(school)
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
    print(o6)
    print(o7)
    print(o8)
    print(o7)
    print(o8)
    print(o9)
    print(o10)

else:
    None







