#To print fibonacci series
n=int(input("Enter the range : "))
first=0
second=1
print(first)
print(second)
for a in range(1,n-1):
    third=first+second
    print(third)
    first,second=second,third
