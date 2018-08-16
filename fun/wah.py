def test(p, q, r):
    print(not (not p or q) or (not q or p))


a = 0
b = 0
c = 0
test(a, b, c)
a = 0
b = 0
c = 1
test(a, b, c)
a = 0
b = 1
c = 0
test(a, b, c)
a = 0
b = 1
c = 1
test(a, b, c)
a = 1
b = 0
c = 0
test(a, b, c)
a = 1
b = 1
c = 0
test(a, b, c)
a = 1
b = 0
c = 1
test(a, b, c)
a = 1
b = 1
c = 1
test(a, b, c)
