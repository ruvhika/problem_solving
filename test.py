n=int(input("Enter n:"))
i=1
p=1
while i<=n:
    j=1
    while j<=i:
        print(chr(ord('A')+p-1), end=' ')
        j=j+1
        p=p+1
    print()
    i=i+1
