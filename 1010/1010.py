name = input()

a, b, c = name.split()

a = int (a)
b = int(b)
c = float(c)

name = input()

d, e, f = name.split()

d = int (d)
e = int(e)
f = float(f)

total = b*c + e*f

print("VALOR A PAGAR: R$ %.2f" % (total))
