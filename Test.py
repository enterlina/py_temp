# x = 16
# y = 5
# print(x ^ y )
# print('x: {:b} y: {:b}'.format(x, y), x)
# print('x >> 3 : {:b}, %x'.format(x >> 2) , x >> 2)
# print('x >> 3 : {:b}, %x'.format(x << 2) , x << 2,'%invert', ~x)
def s(a, *vs, b=10, с=12):
    res = a + b + с

print(s(11, 0, 10))

print(round(.1 + .1 + .1, 10) == round(.3, 20))


def s(a, *vs, b=10, с=12):
    res = a + b + с
    print('1', res, vs)
    for v in vs:
        res += v
        print(res, v)
    return res


print(s(11, 0, 10))

print(round(.1 + .1 + .1, 10) == round(.3, 20))

print(round(.1, 10) + round(.1, 10) + round(.1, 10)  == round(.3, 1))
