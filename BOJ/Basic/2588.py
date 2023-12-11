a = int(input())
b = input()

mul1 = a * int(b[2])
mul2 = a * int(b[1])
mul3 = a * int(b[0])

print(mul1, mul2, mul3, mul1+mul2*10+mul3*100, sep='\n')