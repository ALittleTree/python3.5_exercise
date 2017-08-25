def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

print(my_abs(-2323))

def multiReturn(x,y):
    return x+1,y+1

x,y=multiReturn(1,2)
print(x,y)