def my_numbers():
    a = 1
    print('before yield a=', a)
    while True:
        b = yield a
        a += 1
        print('after yield a=', a)
        print('after yield b=', b)


mygen = my_numbers()

print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))

mygen = my_numbers()
next(mygen) # Для того чтобы мы дошли до yield
print(mygen.send(1))
print(mygen.send(2))
print(mygen.send(3))
print(mygen.send(4))


def flatten(nested_list):
    for sublist in nested_list:
        for item in sublist:
            yield item


nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list(flatten(nested_list)))


def flatten(nested_list):
    for sublist in nested_list:
        yield from sublist


nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list(flatten(nested_list)))