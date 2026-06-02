nterms = int(input("How many terms? "))
n1,n2 = 0,1
count = 0
if nterms<=0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibinacci sequence upto",nterms,":")
    print(n1)
#generate fibinacci sequence
else:
    print("Fibinacci sequence: ")
    while count < nterms:
        print(n1)
        nth = n1+n2
        #update values
        n1=n2
        n2=nth
        count+=1
