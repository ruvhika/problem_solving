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
a=int(input("a="))

if a==1:
     print('Highly Satisfied')


elif a==2:
    print('Moderately Satisfied')
elif a==3:
    print('Not Satisfied')

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
     print("Very Poor")


elif b==2:
  print("Poor")

elif b==3:
  print("Average")

elif b==4:
   print("Good")
    
elif b==5:
   print("Very Good")

else:
    None
c=0
print(" Student-teacher interaction in class :")
print("1.Very Poor")
print("2.Poor")
print("3.Average")
print("4.Good")
print("5.Very Good")
c=int(input("c="))

if c==1:
  print("Very Poor")


elif c==2:
     print("Poor")
    
elif c==3:
   print("Average")
    
elif c==4:
     print("Good")

elif c==5:
     print("Very Good")
else:
    None

d=0
print("course lead comes on time")
print("1.No")
print("2.Sometime")
print("3.Always")
d=int(input("d="))

if d==1:
     print("No")


elif d==2:
    print("Sometimes")

elif d==3:
      print("Always")
else:
    None

e=0
print("Overall rating for the Course *")
print("1.very poor")
print("2.poor")
print("3.Average")
print("4.good")
print("5.very good")
e=int(input("e="))


if e==1:
   print("Very Poor")


elif e==2:
   print("Poor")

elif e==3:
   print("Average")

elif e==4:
    print("Good")

elif e==5:
      print("Very Good")
else:
    None




