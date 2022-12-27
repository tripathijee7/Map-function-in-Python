#map()
"""def square(n):
    return n**2
L=[2,4,6,8,10]
result=map(square,L)
sl=list(result)
print(sl)"""

def factorial(n):
    f=1
    for x in range(1,n+1):
        f=f*x
    return f
L=[2,4,6,8]
result=map(factorial,L)
FL=list(result)
print(FL)
