def gensquares(n):
        for num in range(0,n):
            yield num**2
for x in gensquares(10):    
    print(x)
import random
inp = input('Enter low:')
inp2 = input('Enter high:')
def rand_num(inp, num, inp2):

    for x in range(num):
        yield random.randint(inp,inp2)
for y in rand_num(inp, 5, inp2 ):
    print(y)
s = 'hello'
interable = iter(s)
print(next(s))

