def fib(indx):
    
    a = 0 
    b = 1

    for i in range(indx+1):
        yield a
        temp = a
        a = b
        b = temp + b

# print(list(fib(20)))

for x in fib(100000):
    print(x)

