generator = (i ** 2 for i in range(10) if i % 2 ==0)
print(next(generator)) # exit 0
print(next(generator)) # exit 4
print(next(generator)) # exit 16
print(next(generator)) # exit 36
print(next(generator)) # exit 64
print(next(generator)) # error!