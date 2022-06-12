# Method 1
def add(a,b):
    while b!=0:
        data=a&b
        a=a^b
        b=data<<1
    return a
print("without add sum is:",add(int(input("enter number")),int(input("enter number"))))

# Method 2

def add1(n,n1):
    if n!=n1:
        return (n*n-n1)/(n-n1)
    else:
        return 2*n
def main():
    n=int(input("enter first number"))
    n1=int(input("enter second number"))
    print("sum is:",int(add(n,n1)))
main()