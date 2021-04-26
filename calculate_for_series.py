class series:
    def fact(self,a):
        fact=1
        for i in range(1,a+1):
            fact*=i
        print(fact)
    
    def prime(self,b):
        for i in range(b+1):
            if i > 1:
                for j in range(2, i):
                    if (i % j) == 0:
                        break
                else:
                    print(i, end=" ")
        print()
    def fib(self,c):
        x=-1
        y=1
        for i in range(1,c+1):
            z=x+y
            print(z,end=" ")
            x=y
            y=z

f1=series()
f1.fact(5)
p1=series()
p1.prime(113)
fa1=series()
fa1.fib(10)
