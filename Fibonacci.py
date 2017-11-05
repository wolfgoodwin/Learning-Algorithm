
#Fibonacci 序列时间复杂度Olog(n)

def  Fibonacci(n):

    if n>0:

        list = Fibonacci(int(n/2))
        t0 = list[0]
        t1 = list[1]

        if (n%2 == 1):
            return [t1**2 + t0**2,(2*t0+t1)*t1]
        else:
            return [(2*t1-t0)*t0,t0**2+t1**2]

    return [0,1]


print(Fibonacci(9))
	

