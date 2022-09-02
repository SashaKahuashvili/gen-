
def gen(val,q):
    while val<10:
        val*=q
        print(val)
        yield
gen_iter=gen(1,2)
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))